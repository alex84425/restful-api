
from werkzeug.utils import secure_filename
from argparse import ArgumentParser
import os
from os import listdir
from os.path import isfile, join, isdir
from operator import itemgetter

from sanic import Sanic
from sanic_restful_api import reqparse, abort, Api, Resource
from sanic import response
from sanic.response import json

import io
import aiofiles
from aiofiles.os import remove
import asyncio
import shutil
from async_files.utils import async_wraps
import time
async_rmtree = async_wraps(shutil.rmtree)



app = Sanic(__name__)
api = Api(app)

#path = "/home/alex/workplace_alex/interview/api/"
#path ="/"
#print("os.getcwd():", os.getcwd())

parser = ArgumentParser()
parser.add_argument('--root_path', dest='root_path', action='store', help='Path to serve.',
	default= "/home/alex/workplace_alex/interview/api/" )
parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='Run in debug mode.')
parser.add_argument('--host', action='store', nargs='?', help='Host to bind to.',default = "127.0.0.1")
parser.add_argument('--port', action='store', type=int, nargs='?', help='Port to listen on.',default = "5000")
parser.add_argument('--w', action='store', type=int, nargs='?', help='worker num',default = "1")

args = parser.parse_args()
if args.root_path is not None:
	path = args.root_path


#path = os.getcwd()+"/"

"""
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
	return '.' in filename and \
	   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
"""

async def run_deletion(f_name):
   await remove(f_name)
#@app.route(path+'<path:target>', methods=['POST','PATCH'])
#def post_files(target):
@app.route(path+"<target:path>", methods=['POST','PATCH'])
async def post_files(request, target: str):
	d = request.args
	print(d)
	full_path = path +  target
	print(full_path)

	if   os.path.isfile(full_path ):
		return json( {"error:":"'target is a file, not a directory"} )
	app.config['UPLOAD_FOLDER'] = full_path

	f = request.files.get('file')
	if request.method == 'POST':
		""" not exist dir, try create if fail return exception"""
		if  not os.path.isdir(full_path ):
			try:
#				os.mkdir( app.config['UPLOAD_FOLDER']  )
				await aiofiles.os.mkdir( app.config['UPLOAD_FOLDER'])
			except OSError as exc:
				return json( {"error:":"fail to create dir, existed file or bad path"} )
				if exc.errno != errno.EEXIST:
					raise
				pass


		print("POST!!")
		print(full_path + f.name)
		if  isfile( full_path + f.name):
			return json( {"error:":"existed file! 404 \n"} )
		async with aiofiles.open(app.config['UPLOAD_FOLDER']+"/"+request.files["file"][0].name, 'wb') as f:
			await f.write(request.files["file"][0].body)
		return json( {"OK:":"upload file! \n"} )
	
	elif request.method == 'PATCH':
		if not isfile( full_path + f.name):
			return json( {"error:":"not existed file! 404 \n"} )
		else:
	#		os.remove( full_path + "/" + f.name  )
			await aiofiles.os.remove(full_path + "/" + f.name)
			async with aiofiles.open(app.config['UPLOAD_FOLDER']+"/"+request.files["file"][0].name, 'wb') as f:
				await f.write(request.files["file"][0].body)
			return json( {"OK:":"patch file! \n"} )



@app.route(path+"<target:path>", methods=['DELETE'])
async def delete_files(request, target: str):
	d = request.args
	full_path = path + target
	
	
	print(full_path)
	if  os.path.exists(full_path ) ==False:
		return json( {"error:":"'target not a file or dir"} )

	#print("DELETE!")
	if os.path.isfile(full_path) :
#		os.rmdir( full_path   )
		await aiofiles.os.remove( full_path )
	if os.path.isdir(full_path) :
#		shutil.rmtree(full_path)
#		await aiofiles.os.rmdir(directory)
		await async_rmtree (full_path)
	return json( {"ok:":"remove whole dir or file "} )


@app.route(path+"<target:path>", methods=['GET'])
async def get_files(request, target: str):
	print("path:",path)
	d = request.args
	full_path = path + "/"+ target
	print(full_path)
	print("target:",target)
	print(d)

	if isfile(path + target):
#		return await response.file_stream(path +"/"+target)
		return await response.file(path +"/"+target)
	elif  os.path.isdir(path + target):
		# include dir
		onlyfiles = [ [f+"/"
				,os.path.getsize(full_path+"/"+f) 
				,os.path.getmtime(full_path+"/"+f) 
				,os.path.getctime(full_path+"/"+f) 
				  ] 

			for f in listdir(full_path) if isdir(join(full_path, f))  ] +	 [ [f
				,os.path.getsize(full_path+"/"+f)
				,os.path.getmtime(full_path+"/"+f)
				,os.path.getctime(full_path+"/"+f)
				  ]

			for f in listdir(full_path) if isfile(join(full_path, f))  ]


#		return response.text('Hello world!')


		reverse = False
		if "orderByDirection" in  d.keys():
			if d["orderByDirection"][0] == "Descending":
				reverse = True

			elif d["orderByDirection"][0] == "Ascending":
				reverse = False
			else:

				return json( {"error":"bad orderByDirection keyword"} )

				

		if "orderby" in  d.keys():
			print("sortby", d["orderby"])
			if d["orderby"][0] == "size":
				onlyfiles = sorted(onlyfiles, key=itemgetter(1),reverse=reverse)  
			elif d["orderby"][0] == "fileName":
				onlyfiles = sorted(onlyfiles, key=itemgetter(0),reverse=reverse)  
			elif d["orderby"][0] == "lastModified":
				onlyfiles = sorted(onlyfiles, key=itemgetter(2),reverse=reverse)  
			else:
				return json( {"error":"bad orderBy keyword",

						"accept key": ["size","lastModified","fileName"]} )

			
		else:
			#print("no order!!")
			pass

		if "filterByName" in  d.keys():
			onlyfiles = [ele for ele in onlyfiles if d["filterByName"][0] in ele[0] ]


		output = [ele[0] for ele in onlyfiles ]
#		return response.text('Hello world!')
		return json( {"isDirectory": True,
			"files": output

			} )
	else:	
		return json( {"error:":"HTTP code not found, no such file or directory!"} )

	return json( d )
	#curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files?orderby=size&orderByDirection=Descending&filterByName=32"
#	return json({'file': "123"})



if __name__ == '__main__':
	#import multiprocessing
	#workers = multiprocessing.cpu_count()
	#app.run(..., workers=workers)
	#app.run(host='127.0.0.1', debug=True,port=5000)
	print("path:",path)
	app.run( host=args.host, port=args.port, debug=args.debug, workers = args.w)


"""
curl -i  http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/3

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' 127.0.0.1:5000curl -i  http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/3
"""
