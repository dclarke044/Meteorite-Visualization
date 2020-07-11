def create_classes(db):
    class meteorites(db.Model):
        __tablename__ = 'meteorites'

        index = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        id = db.Column(db.Integer)
        recclass = db.Column(db.String(64))
        mass = db.Column(db.Float)
        fall = db.Column(db.String(64))
        year = db.Column(db.Integer)
        reclat = db.Column(db.Float)
        reclong = db.Column(db.Float)
        mainCategory = db.Column(db.String(64))

        def __repr__(self):
            return '<meteorites %r>' % (self.name)
            
    return meteorites