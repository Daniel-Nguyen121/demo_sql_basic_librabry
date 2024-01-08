from init_app import db
# from datetime import datetime


class Actors(db.Model):
    __tablename__ = 'actors'
    id = db.Column('ID_actor', db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column('Name_actor', db.VARCHAR(55), default=None)
    dob = db.Column('DOB_actor', db.DateTime, default=None)

    def __init__(self, **kwargs):
        super(Actors, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_actor': self.id,
            'name_actor': self.name,
            'dob_actor': self.dob
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id = json_post.get('id_actor')
        name = json_post.get('name_actor')
        dob = json_post.get('dob_actor')

        actor_return = Actors(
            id=id,
            name=name,
            dob=dob
        )
        return actor_return
