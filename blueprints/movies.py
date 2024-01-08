from flask import Blueprint, request
from repository import movies_repo

mod = Blueprint('movies', __name__, url_prefix='/movie')


@mod.route('/', methods=['GET'])
def get_movies():
    id = request.args.get('id')
    list_movies = movies_repo.get(id)
    return {'data': list_movies}, 200


@mod.route('/', methods=['POST', 'PUT', 'DELETE'])
def movie_handle():
    if request.method == 'POST':
        data = request.json
        result = movies_repo.add(data)
        if result:
            return {'status': 0}, 200
        else:
            return {'status': 1, 'error': 'can not add'}, 400
    elif request.method == 'PUT':
        data = request.json
        id = data.get('id')
        data['year'] = int(data['year'])
        result = movies_repo.update(id, data)
        if result:
            return {'status': 0}, 200
        else:
            return {'status': 1, 'error': 'can not update'}, 200
    elif request.method == 'DELETE':
        id = request.json
        result = movies_repo.delete(id)
        if result:
            return {'status': 0}, 200
        else:
            return {'status': 1, 'error': 'can not delete'}, 200
    return


@mod.route('/search', methods=['GET'])
def search():
    param = request.args
    result = movies_repo.search_movie(param)
    return {'data': result}, 200


@mod.route('/count-by-company', methods=['GET'])
def count_by_company():
    result = movies_repo.static_category()
    return {'data': dict(result)}, 200
