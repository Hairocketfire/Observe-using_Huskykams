import asyncio
import serial_asyncio
import websockets

class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False  # You may need to set this depending on your device

    def data_received(self, data):
        message = data.decode('utf-8')
        print('data received', repr(message))
        asyncio.create_task(self.broadcast(message))

    def connection_lost(self, exc):
        print('port closed')

    async def broadcast(self, message):
        for ws in connected:
            await ws.send(message)

connected = set()

async def server(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:  # This will keep the connection alive
            print(message)
    finally:
        connected.remove(websocket)

loop = asyncio.get_event_loop()
coro = serial_asyncio.create_serial_connection(loop, Output, '/dev/ttyACM0', baudrate=115200)
serial_conn = asyncio.run_coroutine_threadsafe(coro, loop)
websocket_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(websocket_server)
asyncio.get_event_loop().run_forever()
