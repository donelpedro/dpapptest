from flask import Flask

app = Flask(__name__)

@app.route("/")
def valid():
        return "successful!"

@app.route("/ping")
def ping():
        return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
