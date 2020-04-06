from app import db


association_table = db.Table('UsersClothes',
    db.Column('User_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('Clothes_id', db.Integer, db.ForeignKey('clothes.id'))
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    state = db.Column(db.Integer)
    city = db.Column(db.String(100))
    clothes = db.relationship(
        "Clothes",
        secondary=association_table,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, id, username, city=None):
        self.id = id
        self.username = username
        self.city = city

    def __repr__(self):
        return f"<User({self.id})>"


class Clothes(db.Model):
    __tablename__ = 'clothes'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(100))
    kind = db.Column(db.String(100))
    clothes_type = db.Column(db.String(100))
    points = db.Column(db.Integer)

    def __init__(self, color, kind, clothes_type='undefined', points=0):
        self.color = color
        self.kind = kind
        self.clothes_type = clothes_type
        self.points = points

    def __repr__(self):
        return f"{self.color} {self.kind} {self.points} {self.clothes_type}"



