#!flask/bin/python
from flask import Flask, jsonify
from flask import render_template


from flask import make_response
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#@app.route('path', methods=['GET'])
#@app.route('path<int:task_id>', methods=['GET'])
#def get_tasks_v1():
#    return jsonify({'tasks': tasks})

path = "/home/alex/workplace_alex/interview/api/"
#@app.route(path+'test_files')
@app.route("/")
def get_files(task_id):
	#return 'files'
    	return jsonify({'file': "files"}), 201


@app.route(path+'<int:task_id>', methods=['GET'])
def get_task(task_id):
    #task = filter(lambda t: t['id'] == task_id, tasks)
    task = [ ele  for ele in tasks if ele["id"] == task_id]

    #task = tasks[ task_id]
    print(task)
    #return jsonify({'tasks': tasks})
    if len(task)  ==0:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'task': task})

@app.route(path, methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route(path,'<int:task_id>', methods=['PUT'])
def update_task(task_id):
    #task = filter(lambda t: t['id'] == task_id, tasks)
    task = [ ele  for ele in tasks if ele["id"] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    #if 'title' in request.json and type(request.json['title']) != unicode:
    #    abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

#@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
@app.route(path,'<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task =list( filter(lambda t: t['id'] == task_id, tasks) )
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)


"""
 curl -i  http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/3

 curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' 127.0.0.1:5000curl -i  http://127.0.0.1:5000/home/alex/workplace_alex/interview/api/3
"""
