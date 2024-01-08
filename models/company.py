from init_app import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column('ID_company', db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    name = db.Column('Name', db.VARCHAR(55), default=None)
    address = db.Column('Address', db.VARCHAR(100), default=None)

    def __init__(self, **kwargs):
        super(Company, self).__init__(**kwargs)

    def to_full_json(self):
        json_token = {
            'id_company': self.id,
            'name': self.name,
            'address': self.address
        }
        return json_token

    @staticmethod
    def from_json(json_post):
        id = json_post.get('id_company')
        name = json_post.get('name')
        address = json_post.get('address')

        company_return = Company(
            id=id,
            name=name,
            address=address
        )
        return company_return
