#aqui são os routes (caminhos)
#flash (mensagensrápidasnoflash)
from flask import render_template, flash, redirect, url_for, request
#importando db e app
from app import app, db
#importando as validações do login e o login
from flask_login import login_user, logout_user, login_required, current_user
#import das tabelas de user e animal
from app.models.tables import User, Animal
#import dos formulários 
from app.models.forms import LoginForm, RegistrationForm, AnimalForm
#import das validações de segurança
from werkzeug.utils import secure_filename
#codificamento da senha
from werkzeug.security import check_password_hash
#import do "operational system"
import os

#verificação do "usuário atual", caso esteja logado, renderizar a página de login
@app.route("/")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        return render_template("index_logged_in.html", user=current_user)
    else:
        return render_template("index.html")


#rota de cadastro de usuário
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    #se o usuário ja estiver logado, ao clicar em cadastro, retornará a tela principal
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
            #checagem das credenciais do usuário logado, caso não existam aparece mensagem de erros
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
#rota de anuncio de animais
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

#rota de adoção, cada novo animal criado, tem uma url única, url essa que é mostrada após o "/adotar..., que garante a individualidade deles"
@app.route('/adotar', defaults={'especie' : None})
@app.route('/adotar/<especie>')
def adotar(especie):
    if especie:
        animais = Animal.query.filter_by(especie=especie).all()
    else:
        animais = Animal.query.all()  # Busque todos os animais do banco de dados
    if current_user.is_authenticated:
        return render_template('adotar_logged_in.html', user=current_user, animais=animais)
    return render_template('adotar.html', animais=animais)
#caso clique no cartãozinho do animal, ele mostra as informações, separadas por ID
@app.route('/animal_detalhes/<int:animal_id>', methods=['GET'])
def animal_detalhes(animal_id):
    # Faça uma consulta para obter o animal pelo id
    animal = Animal.query.get(animal_id)

    # Renderize um template com os detalhes do animal
    return render_template('animal.html', animal=animal)


