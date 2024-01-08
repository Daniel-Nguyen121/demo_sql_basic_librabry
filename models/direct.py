from init_app import db


class Direct(db.Model):
    __tablename__ = 'direct'
    id_director = db.Column('ID_director', db.Integer, db.ForeignKey(
        'directors.ID_director'), nullable=False, primary_key=True)
    id_movie = db.Column('ID_movie', db.Integer, db.ForeignKey(
        'movies.ID_movie'), nullable=False, primary_key=True)
    act = db.Column('Act', db.VARCHAR(45), default=None)

    def __init__(self, **kwargs):
        super(Direct, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_director': self.id_director,
            'id_movie': self.id_movie,
            'act': self.act,
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id_director = json_post.get('id_director')
        id_movie = json_post.get('id_movie')
        act = json_post.get('act')

        direct_return = Direct(
            id_director=id_director,
            id_movie=id_movie,
            act=act,
        )
        return direct_return
