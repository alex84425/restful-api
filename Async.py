import requests
from aiohttp import ClientSession
import asyncio

async def count():
	for i in [1,2,3,4,5]:
		print(i)
		await asyncio.sleep(1)


base_url  ='http://httpbin.org'

j_arr = []
async def get_delay(seconds):
	endpoint = f'/delay/{seconds}'
	print(f'delay {seconds}...')
#	data = requests.get(base_url + endpoint).json()
#	print(data)
	async with ClientSession() as session:
		async with session.get(base_url + endpoint) as response:
			response = await response.read()
#			print(response)
			j_arr.append(response)

async def main():
	await asyncio.gather( get_delay(5), count() )

asyncio.run( main() )

print("done!")
print(j_arr)
