#aqui são os routes (caminhos)

from app import app

@app.route("/")
def index():
    return "hello world"
