from campering.shared.models import db

class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sits_available = db.Column(db.Integer)
    road_type = db.Column(db.String(10))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    # place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    # place = db.relationship('Place',
    #     backref=db.backref('roads', lazy='dinamic'))

    def __init__(self, sits_available, road_type):
        sits_available = self.sits_available
        road_type = self.road_type
