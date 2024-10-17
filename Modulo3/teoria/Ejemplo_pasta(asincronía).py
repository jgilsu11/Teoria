
#%%

import asyncio
import time

#%%

#cocer_pasta

async def tiempo(tarea):
    print(f"tarea: {tarea} tardo {time.time() -start_time:.5f} segundos")



async def cocer_pasta():
    print("Iniciamos tarea cocer pasta ")
    await asyncio.sleep(1)
    print("poner el agua a hervir")
    await asyncio.sleep(8)
    print("agua caliente")
    await asyncio.sleep(8)
    print("meter la pasta")
    await asyncio.sleep(8)
    print("la pasta está lista")


#preparar_salsa

async def preparar_salsa():
    print("Iniciamos tarea preparar salsa ")
    await asyncio.sleep(1)
    print("cortamos los ingredientes")
    await asyncio.sleep(2)
    print("poner la carne a cocinar")
    await asyncio.sleep(3)
    print("poner las verduras a cocinar")
    await asyncio.sleep(4)
    print("tomate")
    await asyncio.sleep(2)
    print("La salsa está lista")


#emplatar

async def main():
    #orquestamos
    await asyncio.gather(cocer_pasta(), preparar_salsa())

if __name__ == "__main__":
    start_time= time.time()
    asyncio.run(main())
    end_time= time.time()
    print(f"El proceso duró {end_time - start_time } ")

