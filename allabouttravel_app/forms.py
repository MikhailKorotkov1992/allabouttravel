from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddPlaceForm(FlaskForm):
    place_name = StringField('Введите название места', validators=[DataRequired()], render_kw={'class': 'form-control'})
    description = TextAreaField('Опишите место', validators=[DataRequired()], render_kw={'class': 'form-control'})
    select_city = SelectField('Выберете город', coerce=str)
    select_category = SelectField('Выберите категорию', coerce=str)
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
