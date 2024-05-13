from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)
#URI DE CONEXÃO
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)


Manager= manager(app)


from app.controllers import default



