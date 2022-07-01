from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

from allabouttravel_app.place.models import Category, City


class AddPlaceForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.select_city.choices = [(city.id, city.title) for city in City.query.all()]
        self.select_category.choices = [(cat.id, cat.title) for cat in Category.query.all()]

    place_name = StringField(
        'Введите название места', validators=[DataRequired()], render_kw={'class': 'form-control'})
    description = TextAreaField('Опишите место', validators=[DataRequired()], render_kw={'class': 'form-control'})
    select_city = SelectField('Выберете город', coerce=str)
    select_category = SelectField('Выберите категорию', coerce=str)
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
