import asyncio
from websockets.server import serve, WebSocketServerProtocol


async def echo(websocket: WebSocketServerProtocol):
	print(f"Someone connected: ")
	
	async def auto_send_loop():
		x = 1
		while websocket.open:
			await websocket.send(f"Ping! * {x}")
			x += 1
			await asyncio.sleep(10)
	looping_task = asyncio.create_task(auto_send_loop())
	async for message in websocket:
		print(message)
		await websocket.send(message)


async def main():
	async with serve(echo):
		await asyncio.Future()


asyncio.run(main())
