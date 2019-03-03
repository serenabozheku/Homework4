from flask import Blueprint, request, render_template
from flask import jsonify

students_list = [
    {'id': 1, 'student': 'Lil Fame'},
    {'id': 2, 'student': 'Jacopo Sala'},
    {'id': 3, 'student': 'Ilda Duke'}
]

students_blueprint = Blueprint('students_blueprint', __name__, template_folder='templates') 

@students_blueprint.route('/<int:student_id>/<name>', methods=['PUT', 'POST'])
def s_put_post(student_id,name):   
    if request.method == 'POST':
        id_exist = False
        for m in range(len(students_list)):
            if students_list['id'][m-1] == student_id:
                id_exist=True

        if id_exist ==  False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        return jsonify(students_list)

    if request.method == 'DELETE':
        for n in students_list:
            n.update({'name': name})
            return jsonify(n)
    
        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)

@students_blueprint.route('/<int:student_id>', method=['GET', 'DELETE'])
def s_delete_get(student_id):  
    if request.method == 'GET':
        flag = False
        for student in students_list:
            if student['id'] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return 'Not able to find ID!'
       
    else: 
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True
                return 'Student deleted successfully!'

        if flag == False:
            return 'Not able to find ID!'

@students_blueprint.route('/all', methods=['GET'])
def get_all():
    return render_template('students.html', students=students_list)
    