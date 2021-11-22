import aiohttp
import asyncio


def do_requests(session):
	#return session.get('https://example.com')
	return session.get('http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/')


async def main():
	async with aiohttp.ClientSession() as session:
		tasks = []
		for _ in range(0, 10):
			tasks.append(do_requests(session))

		results = await asyncio.gather(*tasks)
		for r in results:
			#print('example.com =>', r.status)
			print('example.com =>', r)


if __name__ == '__main__':
	asyncio.run(main())
