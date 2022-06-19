from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user

from allabouttravel_app.db import db
from allabouttravel_app.user.models import User
from allabouttravel_app.user.forms import RegisterForm, LoginForm

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        flash('Вы уже авторизованы')
        return redirect(url_for('place.index'))

    title = 'Авторизация'
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        print(user)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me)
            flash('Вы вошли в аккаунт')
            return redirect(url_for('place.index'))

    flash('Неправильное имя или пароль')
    return render_template('user/login.html', title=title, form=form)



@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    title = 'Регистрация на сайте'

    if form.validate_on_submit():
        user = User(
            name=form.name.data, second_name=form.second_name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы зарагестрировались')
        return redirect(url_for('user.login'))

    return render_template('user/register.html', title=title, form=form)


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из аккаунта')
    return redirect(url_for('place.index'))
