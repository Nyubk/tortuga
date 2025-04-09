# servidor.py
from flask import Flask, request
import asyncio
import websockets

app = Flask(__name__)

# Manejador del túnel (servidor central)
async def manejar_tunel(websocket, path):
    # Aquí se maneja la recepción y reenvío del tráfico.
    while True:
        mensaje = await websocket.recv()
        # Aquí deberías reenviar el mensaje a tu servidor local
        print(f"Mensaje recibido: {mensaje}")
        # Reenviar la respuesta o realizar alguna acción

# Ruta para WebSockets
@app.route('/tunnel', methods=['GET', 'POST'])
def tunnel():
    return 'Servidor de túneles funcionando'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # El servidor escuchará en el puerto 5000