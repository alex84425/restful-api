from sanic import Sanic
from sanic_restful_api import reqparse, abort, Api, Resource
from werkzeug.utils import secure_filename

import os
from os import listdir
from os.path import isfile, join, isdir
from operator import itemgetter
import io


path = "/home/alex/workplace_alex/interview/api/"

app = Sanic(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')

# Todo
#   show a single todo item and lets you delete them


class Todo(Resource):
    async def get(self, request, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    async def delete(self, request, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    async def put(self, request, todo_id):
        args = parser.parse_args(request)
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    async def get(self, request):
        return TODOS

    async def post(self, request):
        args = parser.parse_args(request)
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class restful_api(Resource):
	def get(target):
	        full_path = path + "/"+ target
	        print(full_path)
	
	        d = request.args.to_dict()
	        #
	#       print( request.args)
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
	#               return jsonify( {"return":"isfile"} )
	                return res
	        elif  os.path.isdir(path + target):
	                # include dir
	                onlyfiles = [ [f+"/"
	                                ,os.path.getsize(full_path+"/"+f)
	                                ,os.path.getmtime(full_path+"/"+f)
	                                ,os.path.getctime(full_path+"/"+f)
	                              ]
	
	                        for f in listdir(full_path) if isdir(join(full_path, f))  ] +    [ [f
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
	                        #print("no order!!")
	                        pass
	
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
##
# Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/home/alex/workplace_alex/interview/api/test_files/')
api.add_resource(Todo, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')
#api.add_resource(restful_api, path+'<path:target>')


if __name__ == '__main__':
    app.run(debug=True,port=5000,host="127.0.0.1")
