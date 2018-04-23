from flask import Flask

app = Flask('simple-python-app')

@app.route("/")
def index():
    return 'Hello from the simple python app\n'

app.run(host='0.0.0.0', port=8080)
