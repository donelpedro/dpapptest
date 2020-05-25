from flask import Flask
app = Flask(__name__)

@app.route("/")
def valid():
        return "Valid URL /app /ping"

@app.route("/ping")
def ping():
        return "OK"

@app.route("/app")
def application():
        return "app"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
