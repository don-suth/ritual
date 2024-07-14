import asyncio
import redis.asyncio as redis
import websockets

HOST = "0.0.0.0"
PORT = 80

CONNECTIONS = set()


async def register(websocket: websockets.WebSocketServerProtocol):
	print(f"Client connected")
	CONNECTIONS.add(websocket)
	try:
		async def auto_send_loop():
			x = 1
			while websocket.open:
				await websocket.send(f"Ping! * {x}")
				x += 1
				await asyncio.sleep(10)
		looping_task = asyncio.create_task(auto_send_loop())
		await websocket.wait_closed()
	finally:
		CONNECTIONS.remove(websocket)


async def reader(channel: redis.client.PubSub):
	while True:
		message = await channel.get_message(ignore_subscribe_messages=True)
		if message is not None:
			print(f"(Reader) Message Received: {message}")
			websockets.broadcast(CONNECTIONS, message=message["data"].decode())


async def main():
	r = await redis.from_url("redis://redis:6379")
	async with r.pubsub() as pubsub:
		future = asyncio.create_task(reader(pubsub))
		async with websockets.serve(register, HOST, PORT):
			await asyncio.Future()

asyncio.run(main())
