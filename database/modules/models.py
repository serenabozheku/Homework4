from ext import db


class StudentsModel(db.Model):
    
    id_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class CoursesModel(db.Model):
    
    id_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class EventsModel(db.Model):
   
    id_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()