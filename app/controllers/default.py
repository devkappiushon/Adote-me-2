#aqui são os routes (caminhos)
#
from app import app

@app.route("/")
def home():
    return "hello world"




