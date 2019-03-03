from flask import Blueprint, request, render_template
from flask import jsonify

courses_list = [
    {'id': 1, 'name': 'ECO311'},
    {'id': 2, 'name': 'ECO400'},
    {'id': 3, 'name': 'INF310'}
]

courses_blueprint = Blueprint('courses_blueprint', __name__, template_folder='templates')
  
@courses_blueprint.route('/<int:course_id>/<name>', methods=['PUT', 'POST'])  
def c_put_post(course_id,name): 
    if request.method == 'POST':
        id_exist = False
        for m in range(len(courses_list)):
            if courses_list['id'][m-1] == course_id:
                course_id = True

        if id_exist == False:
                courses_list.append(dict({'id': course_id, 'name': name}))
                return jsonify(courses_list)
        return jsonify(courses_list)
        
    if request.method == 'PUT':
        for n in courses_list:
            if n['id'] == event_id:
                n.update({'name': name})
                return jsonify(n)

        events_list.append(dict({'id:': course_id, 'name': name}))
        return jsonify(courses_list)


@courses_blueprint.route('/<int:course_id>', methods=['GET', 'DELETE'])

def c_get_delete(course_id): 
    if request.method == 'GET':
        flag = False
        for courses in courses_list:
            if courses['id'] == course_id:
                flag = True
                return jsonify(courses)
        if flag == False:    
            return 'Not able to find ID!'
    
    if request.method == 'DELETE':
        flag = False
        for a in range(len(courses_list)): 
            if courses_list[a]['id'] == course_id: 
                del courses_list[a]
                flag = True
                return 'Course deleted successfully!'

        if flag == False:
            return 'Not able to find ID!'

@courses_blueprint.route('/all', methods=['GET'])
def get_all():
    return render_template('courses.html', course=courses_list)