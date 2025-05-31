from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return "<p>Hello, World!</p>"

@app.route("/exchange/<exchange>")
def exchange(exchange: str) -> str:
    return f"<p>Yoke for {exchange}"