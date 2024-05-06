#aqui ficarão as tabelas do banco de dados

from app import db

class Animal(db.Model):
    __tablename__= "animal" #nome da tabela já definida
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    cor = db.Column(db.String(35), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text)
    foto = db.Column(db.String(200))

    def __init__(self, nome, especie, cor, idade, descricao, foto):
        self.nome= nome
        self.especie= especie
        self.cor= cor
        self.idade= idade
        self.descricao= descricao
        self.foto= foto







class User(db.Model):
    __tablename__= "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.Integer, nullable=False, unique=True)
