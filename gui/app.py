from flask import Flask , jsonify, render_template, request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	print "Here"
	return render_template('data.html')

@app.route('/api/gateway',methods=['POST'])
def gateway():
	print "Ha"
	data = json.loads(request.form['data'])
	print data
	print data[0]['arrivaltime']

	return render_template('results.html')
if __name__ == "__main__":
	app.run(debug=True)