from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

stores =[
{
'name':'Cool Stire',
'items':[
	{'name':'Cool Item',
	'price':9.99
	}
	]


}

]
@app.route('/')
def home():
	return render_template('index.html')
home()
