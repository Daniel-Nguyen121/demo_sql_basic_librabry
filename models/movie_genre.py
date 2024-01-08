from init_app import db


class MovieGenre(db.Model):
    __tablename__ = 'movie_genre'
    id_movie = db.Column('ID_movie', db.Integer, db.ForeignKey(
        'movies.ID_movie'), nullable=False, primary_key=True)
    id_genre = db.Column('ID_genre', db.Integer, db.ForeignKey(
        'genres.ID_genres'), nullable=False, primary_key=True)

    def __init__(self, **kwargs):
        super(MovieGenre, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_movie': self.id_movie,
            'id_genre': self.id_genre,
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id_movie = json_post.get('id_movie')
        id_genre = json_post.get('id_genre')

        movie_genre_return = MovieGenre(
            id_movie=id_movie,
            id_genre=id_genre,
        )
        return movie_genre_return
