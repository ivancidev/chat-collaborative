import asyncio
import websockets
import json

connected_clients = set()

async def broadcast(message):
    """Envía un mensaje a todos los clientes conectados."""
    for client in connected_clients:
        try:
            await client.send(message)
        except websockets.exceptions.ConnectionClosed:
            connected_clients.remove(client)

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"Cliente conectado. Total: {len(connected_clients)}")
    
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                
                if data.get('type') == 'system':
                    # Notificar a todos sobre conexión/desconexión
                    await broadcast(json.dumps(data))
                    print(f"Sistema: {data['username']} {data['event']}ed")
                else:
                    # Reenviar mensaje normal a todos
                    await broadcast(message)
                    
            except json.JSONDecodeError:
                # Para compatibilidad con mensajes antiguos
                await broadcast(message)
                
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")
    finally:
        connected_clients.remove(websocket)
        print(f"Cliente desconectado. Total: {len(connected_clients)}")

async def main():
    print("Servidor WebSocket corriendo en ws://localhost:12345")
    async with websockets.serve(handler, "localhost", 12345):
        await asyncio.Future()  # Ejecuta infinitamente

if __name__ == "__main__":
    asyncio.run(main())