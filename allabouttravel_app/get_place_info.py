from allabouttravel_app.db import db
from allabouttravel_app.place.models import Place, City, Category


def get_place_info(place_title):
    place, city, category = db.session.query(
        Place, City.title, Category.title
    ).join(City, Place.city_id == City.id
    ).join(Category, Place.category_id == Category.id).filter(
    Place.title == place_title).first()
    return (place, city, category)
