import os
import pprint
from flask import Flask

app = Flask('env-printer-app')

@app.route("/")
def index():
    return pprint.pformat(dict(os.environ))

app.run(host='0.0.0.0', port=8080)
