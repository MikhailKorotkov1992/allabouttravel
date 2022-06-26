from flask import Blueprint, render_template, redirect, flash, url_for, current_app
from flask_login import login_required, current_user

from allabouttravel_app.db import db
from allabouttravel_app.get_place_info import get_place_info
from allabouttravel_app.place.models import Category, City, Place
from allabouttravel_app.place.forms import AddPlaceForm

blueprint = Blueprint('place', __name__)


def create_place_form():
    """Создает форму для добавления места в БД"""
    form = AddPlaceForm()
    form.select_city.choices = [(city.id, city.title) for city in City.query.all()]
    form.select_category.choices = [(cat.id, cat.title) for cat in Category.query.all()]
    return form


@blueprint.route('/')
def index():
    places = Place.query.filter(Place.is_verified == True).all()
    return render_template('places/index.html', title='Главная страница', places=places)


@blueprint.route('/place/<alias>')
def show_place(alias):
    place, city, category = get_place_info(alias)
    return render_template('places/show_place.html', place=place, city=city, category=category)


@blueprint.route('/add_place')
@login_required
def add_place():
    form = create_place_form()

    return render_template('places/add_place.html', title='Добавить место', form=form)


@blueprint.route('/process-add-place', methods=['POST'])
@login_required
def process_add_place():
    form = create_place_form()

    if form.validate_on_submit():
        try:
            place = Place(title=form.place_name.data, description=form.description.data,
                city_id=form.select_city.data, category_id=form.select_category.data,
                user_id=current_user.get_id()
            )
            db.session.add(place)
            db.session.commit()
            flash('Место добавлено, после модерации админом сайта оно появится на главной странице')
            current_app.logger.info(f"место добавлено {place}")
            return redirect(url_for('place.index'))
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            flash('Ошибка при добавлении в БД')
            return redirect(url_for('place.add_place'))
