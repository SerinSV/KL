import asyncio
import websockets

async def handle_connection(websocket):
  print("A client has connected.")

  while True:
      try:
        message = await websocket.recv()
        print("Received message from client:", message)
        response = "Server received your message: " + message
        await websocket.send(response)
      except websockets.exceptions.ConnectionClosed:
        print("Client closed the connection.")
        break


start_server = websockets.serve(handle_connection, 'localhost', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
