import asyncio
import websockets

TUNNEL_ID = "miproyecto123"
#Identificador de tunel

async def connect():
    # Define la función asincrónica `connect` que establecerá una conexión WebSocket con el servidor central.
    
    uri = f"wss://tortuga-9fhd.onrender.com/register/{TUNNEL_ID}"
    # Construye la URI del servidor WebSocket, incluyendo el ID del túnel (TUNNEL_ID) para registrarse con un identificador único.

    async with websockets.connect(uri) as websocket:
        # Establece una conexión WebSocket con el servidor. `websocket` es el canal de comunicación.
        # El uso de `async with` asegura que la conexión se cierre correctamente al terminar el bloque.

        print(f"Túnel activo como {TUNNEL_ID}")
        # Muestra en consola que el túnel está activo y conectado con ese ID.

        async for message in websocket:
            # Espera mensajes entrantes desde el servidor WebSocket de forma continua (bucle asincrónico).
            # Cada vez que llega un mensaje, se ejecuta el siguiente bloque.

            print(f"Mensaje del servidor: {message}")
            # Imprime el mensaje recibido desde el servidor.

