import asyncio
import socket

import websockets

from desencriptar import desencriptar
from encriptar import encriptar

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


def iniciar_como_servidor():
    print(f"La dirección IP del servidor es: {ip} y el Puerto es el: 8765")

    async def hello(websocket):
        name = await websocket.recv()
        print(f"Este es el mensaje sin decifrar: {name}")
        desencriptar(name)

        greeting = encriptar()
        await websocket.send(greeting)
        print("Mensaje enviado con exito")

    async def main():
        async with websockets.serve(hello, ip, 8765):
            await asyncio.Future()  # El servidor sigue funcionando indefinidamente

    asyncio.run(main())


def iniciar_como_cliente():
    print(f"La dirección IP del cliente es: {ip} y el Puerto es el: 8765")

    async def hello():
        async with websockets.connect(f"ws://{ip}") as websocket:
            name = encriptar()

            await websocket.send(name)
            print("mensaje enviado con exito")

            greeting = await websocket.recv()
            print(f"Este es el mensaje sin decifrar: {greeting}")
            mensajedecifrado = desencriptar(greeting)
            print(f"Mensaje recibido: {mensajedecifrado}")

    print('Si deseas acabar la conversacion escriba "salir"')
    while True:
        asyncio.run(hello())


def opcioneswebsocket():
    opcionesdeservidores = {"1": iniciar_como_servidor, "2": iniciar_como_cliente}
    var = input("Escoge entre la opciones. \n1: serviddor \n2: cliente\n")
    opcionesdeservidores.get(var)()
