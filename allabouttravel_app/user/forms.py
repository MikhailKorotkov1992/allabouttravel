from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from allabouttravel_app.user.models import User


class RegisterForm(FlaskForm):
    name = StringField(
        'Введите имя: ',
        validators=[DataRequired(message='Заполните поле')],
        render_kw={'class': 'form-control'}
    )
    second_name = StringField(
        'Введите фамилию: ',
        validators=[DataRequired(message='Заполните поле')],
        render_kw={'class': 'form-control'}
    )
    email = StringField(
        'Введите email: ', validators=[Email()],
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

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError('Этот email уже используется')


class LoginForm(FlaskForm):
    email = StringField(
        'Введите email', validators=[DataRequired()],
        render_kw={'class': 'form-control'}
    )
    password = PasswordField('Введите пароль', validators=[DataRequired()],
        render_kw={'class': 'form-control'}
    )
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
