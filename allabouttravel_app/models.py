from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    cities = db.relationship('City')

    def __repr__(self):
        return f'{self.title}'


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    places = db.relationship('Place')

    def __repr__(self):
        return f'{self.title}'


class Place(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text)
    is_verified = db.Column(db.Boolean, default=False, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return f'{self.title}'


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    places = db.relationship('Place')

    def __repr__(self):
        return f'{self.title}'
