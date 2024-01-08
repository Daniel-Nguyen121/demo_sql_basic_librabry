from init_app import db


class Genres(db.Model):
    __tablename__ = 'genres'
    id = db.Column('ID_genres', db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column('Name', db.VARCHAR(55), default=None)

    def __init__(self, **kwargs):
        super(Genres, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_genres': self.id,
            'name': self.name,
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id = json_post.get('id_genres')
        name = json_post.get('name')

        genre_return = Genres(
            id=id,
            name=name,
        )
        return genre_return
