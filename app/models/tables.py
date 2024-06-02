#aqui ficarão as tabelas do banco de dados
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<user %r>" % self.name

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
    



class Animal(db.Model):
    __tablename__= "animal" #nome da tabela já definida
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    raca = db.Column(db.String(50), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    esterilizado = db.Column(db.Boolean)
    foto = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, raca, especie, cor, idade, descricao, foto, esterilizado):
        #animal("amora", "rotwalley", "branco", "12",...)
        self.nome= nome
        self.raca= raca
        self.especie= especie
        self.cor= cor
        self.idade= idade
        self.descricao= descricao
        self.esterilizado= esterilizado
        self.foto= foto
    def __repr__(self):
        return "<Animal %r>" % self.nome
    








