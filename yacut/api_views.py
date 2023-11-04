from flask import jsonify, request

from . import app, db
from .models import URLMap
from .utils import get_unique_short_id, check_unique_url, check_symbols_url
from settings import URL, LENGTH
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    custom_id = data.get('custom_id')
    if custom_id and (not check_symbols_url(custom_id) or len(custom_id) > 16):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    custom_id = custom_id or get_unique_short_id()
    if check_unique_url(custom_id):
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    query = URLMap(original=data['url'],
                   short=custom_id)
    db.session.add(query)
    db.session.commit()
    return jsonify({'url': query.original, 'short_link': URL + query.short}), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_urls(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original}), 200
