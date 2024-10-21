import pandas as pd
import numpy as np
import asyncio
import aiofiles
import os
from io import StringIO # StringIO es un módulo de Python que permite trabajar con cadenas de texto como si fueran archivos. 
import time


async def leer_archivo_asincrono(archivo):
    """Lee un archivo de forma asíncrona y retorna el contenido."""
    async with aiofiles.open(archivo, mode='r', encoding='latin1') as f:
        content = await f.read()
    return content

async def escribir_archivo_asincrono(archivo, df):
    """Escribe el DataFrame en un archivo de forma asíncrona."""
    async with aiofiles.open(archivo, mode='w', encoding='latin1') as f:
        await f.write(df.to_csv(sep=';', index=False))

async def aplicar_ruido(df, col, proporcion_ruido):
    """Aplica ruido a una columna específica."""
    df.loc[df.sample(frac=proporcion_ruido).index, col] = np.nan

async def aplicar_ruido_asincrono(df, lista_col):
    """Aplicar ruido a las columnas seleccionadas de forma asíncrona."""
    tasks = []
    for col in lista_col:
        # Generamos un valor aleatorio entre 0.05 y 0.01
        proporcion_ruido = np.random.uniform(0.01, 0.05)
        # Crear una tarea asincrónica para aplicar ruido
        task = asyncio.create_task(aplicar_ruido(df, col, proporcion_ruido))
        tasks.append(task)
    await asyncio.gather(*tasks)

async def editar_df(archivo):
    """Función para editar el DataFrame y manipular los datos."""
    
    # Leer archivo de manera asíncrona
    content = await leer_archivo_asincrono(archivo)
    df = pd.read_csv(StringIO(content), sep=';')

    print(df.info())
    print("##############################################")

    # Sobreescribimos el 25% de los registros de la columna 'ANO EXERCÍCIO'
    df.loc[df.sample(frac=0.25).index, 'ANO EXERCÍCIO'] = np.nan
    df.loc[df.sample(frac=0.35).index, 'NOME ÓRGÃO SUPERIOR'] = np.nan
    df.loc[df.sample(frac=0.05).index, 'VALOR PREVISTO ATUALIZADO'] = np.nan

    print(df.info())
    print("##############################################")

    # Criba de las columnas que no se les va a aplicar más ruido
    lista_col_eliminada = ['ANO EXERCÍCIO', 'NOME ÓRGÃO SUPERIOR', 'VALOR PREVISTO ATUALIZADO']
    lista_col = df.columns.tolist()
    for col in lista_col_eliminada:
        lista_col.remove(col)

    # Aplicar ruido de manera concurrente
    await aplicar_ruido_asincrono(df, lista_col)

    print(df.info())
    print("##############################################")

    # Guardar el DataFrame de forma asíncrona
    output_file = f'datos_finales_asincrono/{archivo}'
    await escribir_archivo_asincrono(output_file, df)
    print(f"##########___FINAL: {archivo}___##################")


    return df



async def procesar_archivos():
    """Procesar todos los archivos CSV de la carpeta actual."""
    # Listar archivos CSV
    lista_csv = [i for i in os.listdir() if i.endswith('.csv')]
    lista_csv.sort()

    # Ejecutar la función editor_df de forma concurrente para cada archivo
    tasks = [editar_df(archivo) for archivo in lista_csv[:-1]]
    await asyncio.gather(*tasks)

# Ejecutar el bucle de eventos para procesar los archivos
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(procesar_archivos())
    end_time = time.time()
    print(f"Tiempo total del programa {end_time - start_time:.2f} seconds.")