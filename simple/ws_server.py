import asyncio
import websockets
import json

# new_dict = {
# 	'Order' : 'accept'
# }
# json_object = json.dumps(new_dict, indent = 4) 
# new_dict = 'Test'

async def response(websocket, path):
	message = await websocket.recv()
	print(f"We got the message from the client: {message}")
	order_req = CheckOrder(message)
	# await websocket.send("I can confirm I got your message!")
	await websocket.send(json.dumps(order_req, indent = 4) )

def CheckOrder(v):
	if v == '1':
		return {'Order' : 'accept'}
	if v == '2':
		return {'Order' : 'item'}

start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()