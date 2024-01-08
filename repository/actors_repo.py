from models.actors import Actors, db

# Get all Actors


def find_all():
    return Actors.query.all()

# Get Actors by filtering
# By id


def find_by_id(id):
    return Actors.query.filter_by(id=id).first()

# By name


def find_by_name(name):
    return Actors.query.filter_by(name=name).first()

# Get Actors in order
# By name (1: ascending, 2:descending)


def get_order_by_name(type=1):
    if type == 1:
        return Actors.query.order_by(Actors.name.asc())
    else:
        return Actors.query.order_by(Actors.name.desc())


# Insert data
def insert(json_data):
    try:
        actor = Actors.from_json(json_data)
        db.session.add(actor)
        db.session.commit()
        return True
    except:
        return False

# Update data


def update_by_id(id, data):
    try:
        actor = Actors.query.filter_by(id=id).update(data)
        db.session.commit()
        return True
    except:
        return False

# Delete data


def delete_by_id(id):
    try:
        actor = find_by_id(id)
        db.session.delete(actor)
        db.session.commit()
        return True
    except:
        return False
