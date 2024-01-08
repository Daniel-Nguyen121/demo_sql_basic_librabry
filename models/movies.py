from init_app import db
# from company import Company


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column('ID_movie', db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    title = db.Column('Title', db.VARCHAR(45), default=None)
    year = db.Column('Year', db.Integer, default=None)
    id_company = db.Column('ID_company', db.Integer, db.ForeignKey(
        'company.ID_company'), nullable=False)

    def __init__(self, **kwargs):
        super(Movies, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_movie': self.id,
            'title': self.title,
            'year': self.year,
            'id_company': self.id_company
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id = json_post.get('id_movie')
        title = json_post.get('title')
        year = json_post.get('year')
        id_company = json_post.get('id_company')

        movie_return = Movies(
            id=id,
            title=title,
            year=year,
            id_company=id_company
        )
        return movie_return
