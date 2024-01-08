from init_app import db
# from datetime import datetime


class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column('ID_director', db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column('Name', db.VARCHAR(55), default=None)
    dob = db.Column('DOB', db.DateTime, default=None)

    def __init__(self, **kwargs):
        super(Directors, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_director': self.id,
            'name': self.name,
            'dob': self.dob
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id = json_post.get('id_director')
        name = json_post.get('name')
        dob = json_post.get('dob')

        director_return = Directors(
            id=id,
            name=name,
            dob=dob
        )
        return director_return
