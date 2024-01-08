from init_app import db


class Quotes(db.Model):
    __tablename__ = 'quotes'
    id_actor = db.Column('ID_actor', db.Integer, db.ForeignKey(
        'actors.ID_actor'), nullable=False, primary_key=True)
    id_movie = db.Column('ID_movie', db.Integer, db.ForeignKey(
        'movies.ID_movie'), nullable=False, primary_key=True)
    quote = db.Column('Quote', db.VARCHAR(100), default=None)

    def __init__(self, **kwargs):
        super(Quotes, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_actor': self.id_actor,
            'id_movie': self.id_movie,
            'quote': self.quote,
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id_actor = json_post.get('id_actor')
        id_movie = json_post.get('id_movie')
        quote = json_post.get('quote')

        quote_return = Quotes(
            id_actor=id_actor,
            id_movie=id_movie,
            quote=quote
        )
        return quote_return
