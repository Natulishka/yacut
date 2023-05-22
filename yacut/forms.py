from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), URL(message='Может содержать только URL')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16), Regexp(r'[a-zA-Z0-9]+', message='Указано недопустимое имя для короткой ссылки'), Optional()]
    )
    submit = SubmitField('Создать')
