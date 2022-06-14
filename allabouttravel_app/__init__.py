import logging
from flask import Flask, render_template, request, url_for, redirect

from allabouttravel_app.models import db, Category, Place, City

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
        try:
            cities = City.query.all()
            categories = Category.query.all()
        except:
            print('Ошибка при чтении из БД')
        if request.method == 'POST':
            title = request.form.get('place_name')
            description = request.form.get('description')
            try:
                city = City.query.filter_by(title=request.form.get('city')).first()
                category = Category.query.filter_by(title=request.form.get('category')).first()
                place = Place(title=title, description=description, city_id=city.id, category_id=category.id)
                db.session.add(place)
                db.session.commit()
                return(redirect(url_for('index')))
            except:
                db.session.rollback()
                logger.exception('exception')

        return render_template('add_place.html', title='Добавить место', cities=cities, categories=categories)

    return app
