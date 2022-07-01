from flask import Blueprint, redirect, render_template, url_for, flash, current_app

from allabouttravel_app.db import db
from allabouttravel_app.get_place_info import get_place_info
from allabouttravel_app.admin.decorators import admin_required
from allabouttravel_app.user.models import User
from allabouttravel_app.place.models import Place

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

admin_menu = [{'url': 'admin.show_users', 'title': 'Список пользователей'},
              {'url': 'admin.show_places', 'title': 'Список мест'}]


@blueprint.route('/')
@admin_required
def index():
    title = 'Админ-панель'
    return render_template('admin/index.html', title=title, menu=admin_menu)


@blueprint.route('/show_users')
@admin_required
def show_users():
    title = 'Пользователи сайта'
    users = User.query.all()
    return render_template('admin/show_users.html', title=title, users=users)


@blueprint.route('/show_places')
@admin_required
def show_places():
    title = 'Места'
    places = Place.query.all()
    return render_template('admin/show_places.html', title=title, places=places)


@blueprint.route('/show_place_status/<alias>')
@admin_required
def show_place_status(alias):
    place, city, category = get_place_info(alias)
    title = place.title
    return render_template('admin/show_place_status.html', title=title, place=place, city=city, category=category)


@blueprint.route('/change_place_status/<alias>')
@admin_required
def change_place_status(alias):
    try:
        place = Place.query.filter(Place.title == alias).first()
        if place.is_verified:
            place.is_verified = False
        else:
            place.is_verified = True
        flash('Статус места изменен!')
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        flash('Ошибка при изменении статуса места')
    return redirect(url_for('admin.show_places', alias=place.title))
