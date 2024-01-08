from init_app import db


class Act(db.Model):
    __tablename__ = 'act'
    id_movie = db.Column('ID_movie', db.Integer, db.ForeignKey(
        'movies.ID_movie'), nullable=False, primary_key=True)
    id_actor = db.Column('ID_actor', db.Integer, db.ForeignKey(
        'actors.ID_actor'), nullable=False, primary_key=True)
    role = db.Column('Role', db.VARCHAR(45), default=None)

    def __init__(self, **kwargs):
        super(Act, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_movie': self.id_movie,
            'id_actor': self.id_actor,
            'role': self.role
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id_movie = json_post.get('id_movie')
        id_actor = json_post.get('id_actor')
        role = json_post.get('role')

        act_return = Act(
            id_actor=id_actor,
            id_movie=id_movie,
            role=role,
        )
        return act_return
