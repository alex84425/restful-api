#!flask/bin/python
from flask import Flask, jsonify
from flask import render_template


from flask import make_response
#import requests
from flask import request


app = Flask(__name__)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

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
#@app.route('/home/alex/workplace_alex/interview/api/', methods=['GET'])
#@app.route('/home/alex/workplace_alex/interview/api/<int:task_id>', methods=['GET'])
@app.route('/home/alex/workplace_alex/interview/api/', methods=['POST'])
#def get_tasks_v1():
#    return jsonify({'tasks': tasks})

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' 127.0.0.1:5000/home/alex/workplace_alex/interview/api/1
