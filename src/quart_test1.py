from quart import Quart

app = Quart(__name__)

path = "/home/alex/workplace_alex/interview/api/"

#app.route(path+'<path:target>', methods=['GET'])
#@app.route("/")
@app.route(path+'<path:target>', methods=['GET'])
async def get_files(target):
    return 'hello\n'

app.run()


"""

@app.route('/')
async def hello():
    return 'hello\n'

app.run()
"""
