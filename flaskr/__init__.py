from flask import Flask
from flask import render_template, request
from .keywords import getKeywords


def create_app(test_config = None):
	app = Flask(__name__)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	@app.route("/", methods=['GET'])
	def index():
		return render_template('index.html')

	@app.route("/", methods=['POST'])
	def form():
		url = request.form['url']
		response = getKeywords(url)
		print(response)
		return render_template('index.html', response=response)

	return app

