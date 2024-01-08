from models.movies import Movies, db
from datetime import datetime
from sqlalchemy import func

# Get all Movies


def get(id=None):
    if id is not None:
        movie = find_by_id(id).to_full_json()
        return [movie]
    else:
        list_movie = find_all()
        list_movie = list(map(lambda x: x.to_full_json(), list_movie))
        return list_movie

# Add data


def add(data):
    try:
        data['year'] = int(data['year'])
        data['id_company'] = int(data['id_company'])
        rs = insert(data)
        return True
    except:
        return False
# Update data


def update(id, data):
    try:
        update_by_id(id, data)
        return True
    except:
        return False
# Delete data


def delete(id):
    try:
        delete_by_id(id)
        return True
    except:
        return False
# Search movie


def search_movie(kwargs):
    list_movie = search(kwargs)
    list_movie = list(map(lambda x: x.to_full_json(), list_movie))
    return list_movie if list_movie else []


def static_category():
    list_count = count_movie_by_company()
    return list_count

# Find all the Movies


def find_all():
    return Movies.query.all()

# Get Movies by Filtering:
#   By ID


def find_by_id(id_movie):
    return Movies.query.filter_by(id=id_movie).first()

#   By title


def find_by_title(title):
    return Movies.query.filter(Movies.title.like(f'%{title}%')).all()

#   By published year between
# By price between (minPrice, maxPrice)


def find_by_year(minYear=1800, maxYear=datetime.now().year):
    return Movies.query.filter(Movies.year >= minYear, Movies.year <= maxYear).all()

# Get Movies in order
#   By title (1: ascending, 2:descending)


def get_order_by_title(type=1):
    if type == 1:
        return Movies.query.order_by(Movies.title.asc())
    else:
        return Movies.query.order_by(Movies.title.desc())

# Insert data


def insert(json_data):
    try:
        movie = Movies.from_json(json_data)
        db.session.add(movie)
        db.session.commit()
        return True
    except:
        return False

# Update data


def update_by_id(id_movie, data):
    try:
        movie = Movies.query.filter_by(id=id_movie).update(data)
        db.session.commit()
        return True
    except:
        return False

# Delete data


def delete_by_id(id_movie):
    try:
        movie = find_by_id(id_movie)
        db.session.delete(movie)
        db.session.commit()
        return True
    except:
        return False


def count_movie_by_company():
    data_count = db.session.query(Movies.id_company, func.count(
        Movies.id_company)).group_by(Movies.id_company).all()
    return data_count


def search(kwargs):
    base = Movies.query

    if kwargs.get('title'):
        title = kwargs['title']
        title = title.capitalize()
        base = base.filter(Movies.title == title)
    if kwargs.get('keyword'):
        clause = '%' + kwargs['keyword'] + '%'
        base = base.filter(Movies.title.like(clause)).distinct()
    if kwargs.get('year_min'):
        base = base.filter(Movies.year >= int(kwargs['year_min']))
    if kwargs.get('year_max'):
        base = base.filter(Movies.year <= int(kwargs['year_max']))
    if kwargs.get('sort_by_year'):
        if kwargs.get('sort_by_year') == 'desc':
            base = base.order_by(Movies.year.desc())
        elif kwargs.get('sort_by_year') == 'asc':
            base = base.order_by(Movies.year.asc())
    return base.all()
