from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from allabouttravel_app.db import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, index=True, unique=True, nullable=False)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean, index=True, default=False)
    added_places = db.relationship('Place')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.id}: {self.name} {self.second_name}'
