#aqui são os routes (caminhos)
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import login_user, logout_user
from app.models.tables import User
from app.models.forms import LoginForm, RegistrationForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = RegistrationForm()
    if form.validate_on_submit():
        if request.method == "POST":
            name= request.form['name']
            email= request.form['email']
            password= request.form['password']
            user= User(name, email, password)
            db.session.add(user)
            db.session.commit()
    return render_template("cadastro.html", form=form)    


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = User.query.filter_by(email=form.email.data).first()
            if user and user.verify_password(password):
                login_user(user)
                flash('Êxito ao logar!')
            else:
                flash('Falha ao logar!')
        else:
            print(form.errors)           
    return render_template('login2.html', form=form)

@app.route("/doar")
def doar():
    return render_template("donate.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


