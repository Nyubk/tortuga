import asyncio
import websockets

clients = {}

async def handler(websocket, path):
    if path.startswith("/register/"):
        client_id = path.split("/")[-1]
        clients[client_id] = websocket
        print(f"Cliente registrado: {client_id}")
        try:
            async for message in websocket:
                print(f"[{client_id}] {message}")
        finally:
            clients.pop(client_id, None)
            print(f"Cliente desconectado: {client_id}")

start_server = websockets.serve(handler, "0.0.0.0", 10000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()