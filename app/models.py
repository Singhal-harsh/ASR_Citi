from app import db


class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_string = db.Column(db.Text, index=True, unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return '<Query {}>'.format(self.query_string)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Department {}>'.format(self.department_name)


class QueryWAV(db.Model):
    # __tablename__ = 'querywav'
    id = db.Column(db.Integer, primary_key=True)
    wav_location = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<WAV recording {}>'.format(self.wav_location)


recordings = db.Table('recordings',
                      db.Column('query_id', db.Integer, db.ForeignKey('query.id')),
                      db.Column('recording_id', db.Integer, db.ForeignKey('queryWAV.id'))
                      )
