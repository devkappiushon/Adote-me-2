#aqui são os routes (caminhos)
from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        
    return render_template("login2.html", form=form)

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/doar")
def doar():
    return render_template("donate.html")


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i= User("jp", "1234", "joão", "kkkkk@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "ok"



