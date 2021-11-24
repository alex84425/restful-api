#https://pgjones.gitlab.io/quart/reference/cheatsheet.html

from quart import request
from quart import Quart, render_template, websocket

app = Quart(__name__)
@app.route("/hello")
async def hello():
    request.method
    request.url
#    request.headers["X-Bob"]
    request.args.get("a")  # Query string e.g. example.com/hello?a=2
    d = request.get_data()  # Full raw body
    print("!!!!!!",d)
    #request.args.to_dict()


#    (await request.form)["name"]
#    (await request.get_json())["key"]
#    request.cookies.get("name")
    return "hello!!\n"
  


app.run(host='127.0.0.1', debug=True, threaded = False, port = 5000)

