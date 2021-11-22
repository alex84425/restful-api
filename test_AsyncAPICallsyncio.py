import requests
from aiohttp import ClientSession

async def count():
	for i in [1,2,3,4,5]:
		print(i)
		await asyncio.sleep(1)


base_url  ='http://httpbin.org'
def get_delay(seconds):
	endpoint = f'/delay/{seconds}'
	print(f'delay {seconds}...')
	data = requests.get(base_url + endpoint).json()
#	print(resp)
#	data = resp.json
	print(data)
	#print(data.json())
#	print(data.content)

get_delay(1)
print("done!")
