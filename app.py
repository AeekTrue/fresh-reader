from flask import Flask, render_template, request, render_template_string, redirect

import tools
from config import TEMPLATE_DIR, STATIC_DIR

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/read")
def read():
	path = request.args.get('path')
	if path is None:
		return redirect("/")
	text = tools.render_file(path)
	return render_template_string(text)
