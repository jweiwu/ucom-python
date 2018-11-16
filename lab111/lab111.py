from flask import Flask, render_template
import os

print os.getcwd()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./hello.html')


app.run(debug=True)
