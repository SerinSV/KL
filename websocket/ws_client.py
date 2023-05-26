import asyncio
import websockets


async def connect_to_server():
  
  async with websockets.connect('ws://localhost:8080') as websocket:
    print("Connected to the server.")
    
    while True:
      message = input("Enter a message to send to the server: ")
      await websocket.send(message)
      print("Sent message to server:", message)
      response = await websocket.recv()
      print("Received response from server:", response)

asyncio.get_event_loop().run_until_complete(connect_to_server())
