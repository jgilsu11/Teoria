import asyncio
import requests
import time

async def obtener_estado_request(url):
    """
    Realiza una solicitud HTTP de manera asíncrona utilizando requests en un hilo separado.

    Parameters:
        url (str): La URL de la página web a la que se realizará la solicitud.

    Returns:
        int: El código de estado HTTP de la solicitud.
    """
    # Ejecutamos requests.get en un hilo separado para no bloquear el bucle de eventos
    res = await asyncio.to_thread(requests.get, url)
    return res.status_code

async def main():
    """
    Función principal que realiza solicitudes HTTP asíncronas a 100 páginas de manera concurrente.
    """
    start_time = time.time()
    url_base = "https://atrezzovazquez.es/shop.php?search_type=-1&search_terms=&limit=48&page={}"
    
    # Creamos una lista de tareas para realizar solicitudes a 100 páginas
    tareas = []
    for i in range(1, 101):
        url = url_base.format(i)
        tareas.append(obtener_estado_request(url))

    # Ejecutamos todas las solicitudes de manera concurrente
    resultados = await asyncio.gather(*tareas)

    # Imprimimos los resultados
    for i, estado in enumerate(resultados, 1):
        print(f"Página {i} - Estado de la request: {estado}")

    end_time = time.time()
    print(f"\nEl scrapeo TOTAL duró {end_time - start_time:.2f} segundos.")

# Ejecutar el script de manera asíncrona
if __name__ == "__main__":
    asyncio.run(main())