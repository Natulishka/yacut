from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsageError
from .models import URLMap
from .utils import ckeck_url, get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsageError('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsageError('"url" является обязательным полем!')
    if ('custom_id' not in data or data['custom_id'] == '' or
            data['custom_id'] is None):
        url = URLMap.query.filter_by(original=data['url']
                                     ).order_by(URLMap.timestamp.desc()
                                                ).first()
        if url:
            return jsonify(url.to_dict(request.host_url)), 201
        data['custom_id'] = get_unique_short_id()
    else:
        if not ckeck_url(data['custom_id']):
            raise InvalidAPIUsageError(
                'Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(short=data['custom_id']
                                  ).first() is not None:
            raise InvalidAPIUsageError(
                f'Имя "{data["custom_id"]}" уже занято.')
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict(request.host_url)), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsageError('Указанный id не найден', 404)
    return jsonify(url.to_dict_short()), 200
