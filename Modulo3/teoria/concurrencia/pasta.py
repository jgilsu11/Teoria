import asyncio
import aiohttp
import time

async def count(tarea):
    """ Función para contar el tiempo que tarda una tarea en realizarse.

    Args:
        tarea (str): Nombre de la tarea a contar.
    """
    print(f"\n la tarea {tarea} tardo en realizarse {time.time() - start_time:.5f} segundos.")
    
async def cocer_pasta():
    """ Función para cocer la pasta.

    """
    print("INICIO PROCESO: cocer_pasta")
    await asyncio.sleep(1) 
    print("Poniendo el agua a hervir...")
    await asyncio.sleep(8) 
    print("\n cocer_pasta: El agua está hirviendo. Añadiendo la pasta...")
    await asyncio.sleep(8)  
    print("\n cocer_pasta: La pasta está cocida y lista.")
    await asyncio.gather(count("cocer_pasta"))

async def preparar_salsa_bolonesa():
    """ Función para preparar la salsa boloñesa.

    """
    print("INICIO PROCESO: preparar_salsa_bolonesa")
    await asyncio.sleep(1) 
    print("Cortando los ingredientes para la salsa boloñesa...")
    await asyncio.sleep(1)  
    print("\npreparar_salsa_bolonesa: Sofriendo la carne y los vegetales...")
    await asyncio.sleep(4)  
    print("\n preparar_salsa_bolonesa: Añadiendo tomate y condimentos...")
    await asyncio.sleep(2)  
    print("\npreparar_salsa_bolonesa:  La salsa boloñesa está lista.")
    await asyncio.gather(count("preparar_salsa_bolonesa"))


async def preparar_plato():
    """ Función principal para orquestar la preparación de la pasta con salsa boloñesa.

    """
    print("Comenzando la preparación de la pasta con salsa boloñesa...")
    await asyncio.sleep(2)
    # Ejecutar las dos tareas de forma concurrente
    await asyncio.gather(cocer_pasta(),
                         preparar_salsa_bolonesa())
    print("\npreparar_plato:  ¡Pasta con salsa boloñesa lista para servir!")
    await asyncio.gather(count("preparar_plato"))



if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(preparar_plato())
    end_time = time.time()
    print(f"\n La preparacion de la pasta duro {end_time - start_time:.2f} segundos.")
    
