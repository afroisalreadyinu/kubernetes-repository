import os
import pprint
from flask import Flask

app = Flask('docker-application')

@app.route("/")
def index():
    return pprint.pformat(dict(os.environ))

app.run(host='0.0.0.0', port=8080)
