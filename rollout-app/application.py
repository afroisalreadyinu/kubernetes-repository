import os
import pprint
from flask import Flask

app = Flask('rollout-app')

@app.route("/")
def index():
    host = os.environ['HOSTNAME']
    return "<html><body><h1>{}</h1></body></html>".format(host)

app.run(host='0.0.0.0', port=8080)
