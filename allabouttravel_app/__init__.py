import logging
from flask import Flask, render_template, url_for, redirect

from allabouttravel_app.models import db, Place, City, Category
from allabouttravel_app.forms import AddPlaceForm

logging.basicConfig(filename='app.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html', title='Главная страница')

    @app.route('/add_place', methods=['POST', 'GET'])
    def add_place():
        form = AddPlaceForm()
        form.select_city.choices = [(city.id, city.title) for city in City.query.all()]
        form.select_category.choices = [(cat.id, cat.title) for cat in Category.query.all()]

        if form.validate_on_submit():
            try:
                place = Place(title=form.place_name.data, description=form.description.data,
                              city_id=form.select_city.data, category_id=form.select_category.data)
                db.session.add(place)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logger.exception(e)
            return redirect(url_for('index'))

        return render_template('add_place.html', title='Добавить место', form=form)

    return app
