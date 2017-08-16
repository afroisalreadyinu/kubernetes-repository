from flask import Flask

app = Flask('docker-application')

@app.route("/")
def index():
    return jsonify('Hello from the dockerized app')

app.run(port=6001)
