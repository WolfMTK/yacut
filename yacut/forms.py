from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional, Regexp

from settings import LENGTH_MAX, LENGTH_MIN


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=(DataRequired(message='Обязательное поле.'),
                    Length(max=255),
                    URL(message='Ошибка ввода URL-адреса.'))
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(min=LENGTH_MIN,
                   max=LENGTH_MAX,
                   message='Недопустимый размер ссылки.'),
            Regexp(r'^[a-zA-Z0-9]*$',
                   message='Указано недопустимое имя для короткой ссылки.'),
            Optional()
        ))
    submit = SubmitField('Создать')
