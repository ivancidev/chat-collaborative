import asyncio
import websockets

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print("Cliente conectado.")
    try:
        async for message in websocket:
            print(f"Mensaje recibido: {message}")
            # Enviar el mensaje a todos los clientes conectados
            for client in connected_clients:
                await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")
    finally:
        connected_clients.remove(websocket)

async def main():
    print("Servidor WebSocket corriendo en ws://localhost:12345")
    async with websockets.serve(handler, "localhost", 12345):
        await asyncio.Future()  # Ejecuta infinitamente

if __name__ == "__main__":
    asyncio.run(main())
