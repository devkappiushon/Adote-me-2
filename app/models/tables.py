#aqui ficarão as tabelas do banco de dados

from app import db

class User(db.Model):
    __tablename__= "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, username, password, name, email):
        self.username=username
        self.password=password
        self.name=name
        self.email=email

    def __repr__(self):
        return "<user %r>" % self.username

# Classe teste
class Post(db.Model):
    __tablename__ = "posts"

    id = db.column(db.Integer, primary_key=True)
    content = db.column(db.text)
    user_id = db.column(db.integer, db.ForeignKey("users.id"))

    user= db.relationship("animal", foreign_keys= user_id)
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<post %r>" % self.id
    
# Outra classe
    
class Follow(db.Model):
    __tablename__ = "follow"

    id =db.column(db.Integer, primary_key= True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user= db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys= follower_id)


    








