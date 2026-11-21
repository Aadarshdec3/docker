from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask App running in Docker!"

@app.route("/orders")
def orders():
    return "place ur order"

@app.route("/cart")
def cart():
    return "cart items"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)