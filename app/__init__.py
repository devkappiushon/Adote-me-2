from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("config")


login_manager=LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

from app.models import tables, forms
from app.controllers import routes

