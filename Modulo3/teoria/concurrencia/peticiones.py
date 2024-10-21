import requests
import time

def obtener_estado_request(url):
    """
    Realiza una solicitud HTTP a la URL especificada y devuelve el estado de la respuesta.

    Parameters:
        url (str): La URL de la página web a la que se realizará la solicitud.

    Returns:
        int: El código de estado HTTP de la solicitud.
    """
    # Realizamos la conexión
    res = requests.get(url)

    # Devolvemos el código de estado de la solicitud
    return res.status_code


start_time = time.time()

# Iteramos entre el número 1 y el 100
for i in range(1, 101):
    pag_start_time = time.time()
    # Añadimos el número de página a la URL
    url = f"https://www.zooplus.es/shop/tienda_gatos/pienso_gatos?p={i}"
    
    # Llamamos a la función para obtener el estado de la request
    estado = obtener_estado_request(url)
    
    # Imprimimos el estado de la request
    print(f"Página {i} - Estado de la request: {estado}")
    
    pag_end_time = time.time()
    print(f"El scrapeo de la PAGINA {i} duró {pag_end_time - pag_start_time:.2f} segundos.")
    
end_time = time.time()
print(f"\nEl scrapeo TOTAL duró {end_time - start_time:.2f} segundos.")