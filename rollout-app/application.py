import os
import time

import pprint
from flask import Flask

app = Flask('rollout-app')

@app.route("/")
def index():
    host = os.environ['HOSTNAME']
    return "<html><body><h1>{}</h1></body></html>".format(host)

@app.route("/healthz")
def health():
    return "OK"

time.sleep(5)
app.run(host='0.0.0.0', port=8080)
