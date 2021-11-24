import aiohttp
import asyncio

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--root_path', dest='root_path', action='store', help='Path to serve.',default = "/home/alex/workplace_alex/interview/api/test_files/")
parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='Run in debug mode.')
parser.add_argument('--host', action='store', nargs='?', help='Host to bind to.',default = "127.0.0.1")
parser.add_argument('--port', action='store', type=int, nargs='?', help='Port to listen on.',default = "5000")
parser.add_argument('--r_num', action='store', type=int, nargs='?', help='request numuber',default = "10")
args = parser.parse_args()



def do_requests(session):
	#return session.get('https://example.com')
#	return session.get('http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/test_files/')
	return session.get('http://{}:{}{}'.format(args.host, args.port,args.root_path ))


async def main():
	async with aiohttp.ClientSession() as session:
		tasks = []
		for _ in range(0, args.r_num):
			tasks.append(do_requests(session))

		results = await asyncio.gather(*tasks)
		for r in results:
			#print('example.com =>', r.status)
			print('example.com =>', r)


if __name__ == '__main__':
	#app.run(host='127.0.0.1', debug=True,port=5000)
	asyncio.run(main())
