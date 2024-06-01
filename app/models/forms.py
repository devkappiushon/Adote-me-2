from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, FileField, SubmitField, ValidationError, validators, BooleanField
from wtforms.validators import DataRequired, Email, Length
from app.models.tables import User
from flask_wtf.file import FileRequired, FileAllowed


class RegistrationForm(FlaskForm):
    name = StringField('Nome', [validators.DataRequired(), validators.Length(min=2, max=25)])
    email = StringField('Email', [Email(), validators.Length(min=6, max=35)])
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email já está em uso')
        
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha Não Confere')
    ])
    confirm = PasswordField('Repita a Senha', [validators.DataRequired()])
    accept_tos = BooleanField('Eu Aceito os Termos de Serviço', [validators.DataRequired()])



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])



#animais
class AnimalForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=20)])
    especie = StringField('Espécie', validators=[DataRequired(), Length(max=50)])
    cor = StringField('Cor', validators=[DataRequired(), Length(max=50)])
    idade = IntegerField('Idade', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    foto = FileField('Foto', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Arquivo Não Suportado')])
    esterilizado = BooleanField('Esterilizado')
    submit = SubmitField('Registrar')