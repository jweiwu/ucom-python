from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world, python flask!"


app.run(port=5550, host='0.0.0.0', debug=True)
