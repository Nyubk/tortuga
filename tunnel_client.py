import asyncio
import websockets

TUNNEL_ID = "miproyecto123"

async def connect():
    uri = f"wss://tortuga-9fhd.onrender.com/register/{TUNNEL_ID}"
    async with websockets.connect(uri) as websocket:
        print(f"Túnel activo como {TUNNEL_ID}")
        async for message in websocket:
            print(f"Mensaje del servidor: {message}")

asyncio.get_event_loop().run_until_complete(connect())
