from flask import Flask, jsonify, render_template
from blueprints.students import students_blueprint
from blueprints.courses import courses_blueprint
from blueprints.events import events_blueprint


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

    
app.register_blueprint(students_blueprint, url_prefix='/v1/student')

app.register_blueprint(events_blueprint, url_prefix='/v2/event')

app.register_blueprint(courses_blueprint, url_prefix='/v3/course')