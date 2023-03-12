import asyncio
import websockets
import json

async def message():
	async with websockets.connect("ws://localhost:1234") as socket:
		msg = input("What do you want to send: ")
		await socket.send(msg)
		recv_json = await socket.recv()
		recv_dict = json.loads(recv_json)
		# print(await socket.recv())
		# print(type(await socket.recv()))
		# print(recv_dict)
		# print(type(recv_dict))
		if recv_dict['Order'] == 'accept':
			accept()
		elif recv_dict['Order'] == 'item':
			item()

def accept():
	 print('accept')

def item():
	 print('item')

while(True):
	asyncio.get_event_loop().run_until_complete(message())