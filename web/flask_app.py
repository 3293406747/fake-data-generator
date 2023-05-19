from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from web import faker

app = Flask(__name__, template_folder='static')
CORS(app)  # 允许所有来源的请求


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/sources')
def sources():
	return render_template('sources.js')


@app.route('/data', methods=['GET'])
def get():
	try:
		response = request.args
		value = faker(response["target"])
		return jsonify({"value": value, "message": "success", "status": 200}), 200
	except Exception as e:
		return jsonify({"value": "", "message": str(e), "status": 500}), 500


if __name__ == '__main__':
	app.run()
