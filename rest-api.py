#!flask/bin/python
from flask import Flask, jsonify, send_file
from flask import render_template
from flask import make_response
from flask import request

from werkzeug.utils import secure_filename

import os
from os import listdir
from os.path import isfile, join, isdir
from operator import itemgetter
import io


app = Flask(__name__)
path = "/home/alex/workplace_alex/interview/api/"
"""
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
"""

@app.route(path+'<path:target>', methods=['POST','PATCH'])
def post_files(target):
	full_path = path + "/"+ target
	print(full_path)
	if  os.path.isdir(full_path ) ==False:
		return jsonify( {"error:":"'target not a directory"} )

	app.config['UPLOAD_FOLDER'] = full_path
	f = request.files['file']
	print( secure_filename(f.filename) )
	if request.method == 'POST':
		#https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
		# ImmutableMultiDict([('data', <FileStorage: 'upload.txt' ('text/plain')>)])
		print("POST!!")
		files = [f for f in listdir(full_path) if isfile(join(full_path, f))]
		if secure_filename(f.filename) in files:
			return "existed file! 404 \n"
		f.save( join( app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)) )
		return 'file uploaded successfully\n'
	
	elif request.method == 'PATCH':
		files = [f for f in listdir(full_path) if isfile(join(full_path, f))]
		if (secure_filename(f.filename) in files) == False:
			return "can not patch, not existed file! 404 \n"
		os.remove( full_path + "/" + f.filename  )
		f.save( join( app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)) )
		return 'file patched successfully\n'

@app.route(path+'<path:target>', methods=['DELETE'])
def delete_files(target):
	full_path = path + "/"+ target
	
	print(full_path)
	if  os.path.isfile(full_path ) ==False:
		return jsonify( {"error:":"'target not a file"} )

	elif request.method == 'DELETE':
		print("DELETE!")
		if os.path.isfile(full_path) ==False:
			return "can not deleted, no  such file! 404 \n"
		os.remove( full_path   )
		return 'file deleted successfully\n'


@app.route(path+'<path:target>', methods=['GET'])
def get_files(target):
	full_path = path + "/"+ target
	print(full_path)

	d = request.args.to_dict()
	#
#	print( request.args)
	print("target:",target)

	if isfile(path + target):
		return send_file(  path +"/"+target,as_attachment = True,
			attachment_filename = "dl.txt")
		with open( path +"/"+target, 'rb' ) as f:
			f_bin = io.BytesIO( f.read() )
			return send_file (f_bin,
					# mimetype = "", #('text/plain')
					as_attachment = True,
					 attachment_filename = "dl.txt"
					
					 )
#		return jsonify( {"return":"isfile"} )
		return res
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




		reverse = False
		if "orderByDirection" in  d.keys():
			if d["orderByDirection"] == "Descending":
				reverse = True

			elif d["orderByDirection"] == "Ascending":
				reverse = False
			else:

				return jsonify( {"error":"bad orderByDirection keyword"} )

				

		if "orderby" in  d.keys():
			print("sortby", d["orderby"])
			if d["orderby"] == "size":
				onlyfiles = sorted(onlyfiles, key=itemgetter(1),reverse=reverse)  
			elif d["orderby"] == "fileName":
				onlyfiles = sorted(onlyfiles, key=itemgetter(0),reverse=reverse)  
			elif d["orderby"] == "lastModified":
				onlyfiles = sorted(onlyfiles, key=itemgetter(2),reverse=reverse)  
			else:
				return jsonify( {"error":"bad orderBy keyword",

						"accept key": ["size","lastModified","fileName"]} )

			
		else:
			print("no order!!")

		if "filterByName" in  d.keys():
			onlyfiles = [ele for ele in onlyfiles if d["filterByName"] in ele[0] ]


		#output = [ele[0] for ele in onlyfiles if isfile(join(full_path, ele[0]))  ] +  [ele[0]+"/" for ele in onlyfiles if os.path.isdir(join(full_path, ele[0]))  ]
		output = [ele[0] for ele in onlyfiles ]

		return jsonify( {"isDirectory": True,
			"files": output

			} )
	else:	
		return jsonify( {"error:":"HTTP code not found, no such file or directory!"} )

	return jsonify( d )
	#curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files?orderby=size&orderByDirection=Descending&filterByName=32"
#	return jsonify({'file': "123"})



if __name__ == '__main__':
    #app.run(host='127.0.0.1', debug=True, threaded = True)
    app.run(host='127.0.0.1', debug=True, threaded = True)
#    app.run(host='140.113.120.141', debug=True, threaded = True, port = 5001)


"""
curl -i  http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/3

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' 127.0.0.1:5000curl -i  http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/3
"""
