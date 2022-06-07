from sqlalchemy import Column, ForeignKey, String, Integer, Text, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship

from db import Base, engine


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    cities = relationship('City')

    __table_args__ = (
        UniqueConstraint('title'),
    )

    def __repr__(self):
        return f'Страна: {self.title}'


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country')
    places = relationship('Place')

    __table_args__ = (
        UniqueConstraint('title'),
    )

    def __repr__(self):
        return f'Город: {self.title}'


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    is_verified = Column(Boolean, default=False, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    __table_args__ = (
        UniqueConstraint('title'),
    )

class Categoty(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    places = relationship('Place')

    __table_args__ = (
        UniqueConstraint('title'),
    )


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
