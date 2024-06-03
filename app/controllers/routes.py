#aqui são os routes (caminhos)
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import login_user, logout_user, login_required, current_user
from app.models.tables import User, Animal
from app.models.forms import LoginForm, RegistrationForm, AnimalForm
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
import os

@app.route("/")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        return render_template("index_logged_in.html", user=current_user)
    else:
        return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if request.method == "POST":
            name= request.form['name']
            email= request.form['email']
            password= request.form['password']
            user= User(name, email, password)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('login'))
    return render_template("cadastro.html", form=form)    


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Email ou Senha Inválidos')
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

@app.route('/anunciar', methods=['GET', 'POST'])
@login_required
def registro():
    form = AnimalForm()
    if form.validate_on_submit():
        foto = form.foto.data
        foto_filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_filename))
        animal = Animal(
            nome=form.nome.data,
            raca=form.raca.data,
            especie=form.especie.data,
            cor=form.cor.data,
            idade=form.idade.data,
            descricao=form.descricao.data,
            esterilizado=form.esterilizado.data,
            foto=foto_filename
        )
        db.session.add(animal)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('registro.html', form=form, user=current_user)


@app.route('/adotar')
def adotar():
    animais = Animal.query.all()  # Busque todos os animais do banco de dados
    return render_template('adotar.html', animais=animais)

@app.route('/animal_detalhes/<int:animal_id>', methods=['GET'])
def animal_detalhes(animal_id):
    # Faça uma consulta para obter o animal pelo id
    animal = Animal.query.get(animal_id)

    # Renderize um template com os detalhes do animal
    return render_template('animal.html', animal=animal)


