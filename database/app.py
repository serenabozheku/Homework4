''' Docstring '''

from flask import Flask, jsonify, render_template
from ext import db
from modules.models import StudentsModel
from modules.models import CoursesModel
from modules.models import EventsModel
import json
from flask import request
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'string'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/v1/event/<int:id_number1>/<name1>', methods=["POST", "PUT"])    
def create_event(id_number1, name1):
    if request.method == "POST":
        event = EventsModel(id_number=id_number1, name=name1)
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Event created.'}), 200
    else:
        event = EventsModel.query.get(id_number1)
        event.name = name1
        db.session.commit()
        return jsonify({'message': 'Event updated.'}), 200

@app.route('/v1/event/<int:id_number1>', methods=["GET", "DELETE"])
def get_event(id_number1):
    if request.method == "GET":
        return render_template('home.html', item = EventsModel.query.filter_by(id_number=id_number1) )
    else:
        EventsModel.query.filter_by(id_number=id_number1).delete()
        db.session.commit()
        return jsonify({'message': 'Event deleted.'}), 200

@app.route('/v1/event/all', methods=['GET'])
def get_all_events():
    return render_template('home_all.html', items = EventsModel.query.all() )
    

@app.route('/v2/student/<int:id_number1>/<name1>', methods=["POST", "PUT"]) 
def create_student(id_number1, name1):
    if request.method == "PUT":
        student = StudentsModel.query.get(id_number1)
        student.name = name1
        db.session.commit()
        return jsonify({'message': 'Student updated.'}), 200
    else:
        student = StudentsModel(id_number=id_number1, name=name1)
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'New student created.'}), 200
        

@app.route('/v2/student/<int:id_number1>', methods=["GET", "DELETE"])
def get_student(id_number1):
    if request.method == "DELETE":
        StudentsModel.query.filter_by(id_number=id_number1).delete()
        db.session.commit()
        return jsonify({'message': 'Student deleted.'}), 200
    else:
         return render_template('home.html', items = StudentsModel.query.filter_by(id_number=id_number1) )
        

@app.route('/v2/student/all', methods=['GET'])
def get_all_students():
    return render_template('home_all.html', items = StudentsModel.query.all() )

@app.route('/v3/course/<int:id_number1>/<name1>', methods=["POST", "PUT"]) 
def create_course(id_number1, name1):
    if request.method == "PUT":
        course = CoursesModel.query.get(id_number1)
        course.name = name1
        db.session.commit()
        return jsonify({'message': 'Course updated.'}), 200
    else:
        course = CoursesModel(id_number=id_number1, name=name1)
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'New course created.'}), 200
        

@app.route('/v3/course/<int:id_number1>', methods=["GET", "DELETE"])
def get_course(id_number1):
    if request.method == "DELETE":
        CoursesModel.query.filter_by(id_number=id_number1).delete()
        db.session.commit()
        return jsonify({'message': 'Student deleted.'}), 200
    else:
        return render_template('home.html', items = CoursesModel.query.filter_by(id_number=id_number1) )
        

@app.route('/v3/course/all', methods=['GET'])
def get_all_courses():
    return render_template('home_all.html', items = CoursesModel.query.all() )