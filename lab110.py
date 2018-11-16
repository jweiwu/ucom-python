from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/tiger')
def hello_tiger():
    return '[T] Hello Tiger'


@app.route('/lion')
def hello_lion():
    return "[L]Hello Lion"


@app.route('/new/<animal>')
def hello_new(animal):
    return '[A] hello %s' % animal


@app.route('/animal/<kind>')
def hello_animal(kind):
    if kind == 'tiger':
        return redirect(url_for('hello_tiger'))
    elif kind == 'lion':
        return redirect(url_for('hello_lion'))
    else:
        return redirect(url_for('hello_new', animal=kind))


app.run(debug=True)
