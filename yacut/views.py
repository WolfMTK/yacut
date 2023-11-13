from flask import render_template, flash, redirect

from settings import URL
from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id, check_unique_url, check_symbols_url


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if custom_id and not check_symbols_url(custom_id):
        flash('Данные символы не допустимы.')
        return render_template('index.html', form=form)
    if check_unique_url(custom_id):
        flash('Предложенный вариант короткой ссылки уже существует.')
        return render_template('index.html', form=form)
    custom_id = custom_id or get_unique_short_id()
    db.session.add(URLMap(original=form.original_link.data,
                          short=custom_id))
    db.session.commit()
    return render_template('index.html',
                           form=form,
                           short_url=URL + custom_id)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_short_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
