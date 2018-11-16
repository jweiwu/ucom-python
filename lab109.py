from flask import Flask

app = Flask(__name__)


@app.route('/<int:count>/hi/<name>')
def hello_name(count, name):
    str = 'hello'
    for i in range(0, count):
        str += '%s ' % name
    return str


@app.route('/mypath/<float:weight>/<path:goal>')
def hello_name2(goal, weight):
    str = 'hello %f, %s' % (weight, goal)
    return str


app.run(port=5552, host='0.0.0.0', debug=True)
