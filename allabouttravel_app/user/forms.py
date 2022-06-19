from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    name = StringField(
        'Введите имя: ', validators=[DataRequired()], render_kw={'class': 'form-control'}
    )
    second_name = StringField(
        'Введите фамилию: ', validators=[DataRequired()], render_kw={'class': 'form-control'}
    )
    email = StringField(
        'Введите email: ', validators=[Email(message='Некорректный email')],
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        'Введите пароль: ', validators=[DataRequired(message='Введите пароль')],
        render_kw={'class': 'form-control'}
    )
    password2 = PasswordField(
        'Повторите пароль: ', validators=[EqualTo('password', message='Пароли не совпадают')],
        render_kw={'class': 'form-control'}
    )
    submit = SubmitField('Отправить')


class LoginForm(FlaskForm):
    email = StringField(
        'Введите email', validators=[DataRequired(message='Введите Ваш email')],
        render_kw={'class': 'form-control'}
    )
    password = PasswordField('Введите пароль', validators=[DataRequired(message='Введите пароль')],
        render_kw={'class': 'form-control'}
    )
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
