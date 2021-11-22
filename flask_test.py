#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/home/alex/workplace_alex/interview/api/test_files')
def index():
    return "Hello, World!\n"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
