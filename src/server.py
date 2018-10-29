from flask import Flask, request
app = Flask(__name__)

counter = 0

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/echo")
def echo():
    text = request.args.get("text", "")
    return text

@app.route("/incr", methods=["POST"])
def incr():
    global counter
    counter += 1
    return str(counter)

@app.route("/boom")
def boom():
    raise RuntimeError("BOOM")
