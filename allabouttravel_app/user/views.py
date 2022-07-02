from flask import Blueprint, current_app, render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user

from allabouttravel_app.db import db
from allabouttravel_app.user.models import User
from allabouttravel_app.user.forms import RegisterForm, LoginForm

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        flash('Вы уже авторизованы')
        return redirect(url_for('place.index'))

    title = 'Авторизация'
    form = LoginForm()

    flash('Неправильное имя или пароль')
    return render_template('user/login.html', title=title, form=form)


@blueprint.route('process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        print(user)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me)
            flash('Вы вошли в аккаунт')
            return redirect(url_for('place.index'))
    
    flash('Неправильное имя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/register', methods=['GET'])
def register():
    form = RegisterForm()
    title = 'Регистрация на сайте'
    return render_template('user/register.html', title=title, form=form)


@blueprint.route('/process-register', methods=['POST'])
def process_register():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = User(
                name=form.name.data, second_name=form.second_name.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Вы зарегестрировались')
            return redirect(url_for('user.login'))
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            flash('Ошибка при регистрации')
            return redirect(url_for('user.register'))
    else:
        print(form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(getattr(form, field).label.text, error))
        return redirect(url_for('user.register'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из аккаунта')
    return redirect(url_for('place.index'))
