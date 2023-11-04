from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=(DataRequired(message='Обязательное поле'),
                    Length(1, 255),
                    URL(message='Ошибка ввода URL-адреса.'))
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(1, 6, message='Недопустимый размер ссылки.'),
            Optional()
        ))
    submit = SubmitField('Создать')
