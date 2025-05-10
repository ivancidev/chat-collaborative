import asyncio
import websockets

async def echo(websocket, path):
    print("Cliente conectado.")
    try:
        async for message in websocket:
            # Solo responde al mismo cliente
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")

async def main():
    print("Servidor WebSocket corriendo en ws://localhost:12345")
    async with websockets.serve(echo, "localhost", 12345):  # Puerto 12345
        await asyncio.Future()  # Ejecuta infinitamente

if __name__ == "__main__":
    asyncio.run(main())
