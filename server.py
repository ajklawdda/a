from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def hello_world():
	return redirect("https://r9.whiteboardfox.com/93880596-9036-6989")


if __name__ == '__main__':
	app.run(debug=True)
