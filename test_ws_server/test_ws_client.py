import websockets


async def main():
	with open("TOKEN.txt", "r") as token_file:
		token = token_file.read().strip()
	async for websocket in websockets.connect(
			"wss://ritual.gozz.id.au",
			extra_headers={"Authorization": f"Bearer {token}"}
	):
		try:
			async for message in websocket:
				print(message)
		except websockets.ConnectionClosedError:
			continue
