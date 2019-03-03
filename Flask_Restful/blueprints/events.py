from flask import Blueprint, request, render_template
from flask import jsonify

events_list = [
    {'id': 1, 'name_event': 'Spring Fest'},
    {'id': 2, 'name_event': 'Colors Festivals'},
    {'id': 3, 'name_event': 'Carnivals'}
]

events_blueprint = Blueprint('events_blueprint', __name__, template_folder='templates')

@events_blueprint.route('/<int:event_id>/<name>', methods=['PUT', 'POST'])
    
def put_post(event_id,name):
    if request.method == 'POST':
        id_exist = False
        for m in range(len(events_list)):
            if events_list['id'][m-1] == event_id:
                id_exist = True
                    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name_event': name_event}))
            return jsonify(events_list)
        return jsonify(events_list)

    if request.method == 'PUT':
            for n in events_list:
                if n['id'] == event_id:
                    n.update({'name_event': name_event})
                    return jsonify(n)

            events_list.append(dict({'id:': event_id, 'name_event': name_event}))
            return jsonify(events_list)

@events_blueprint.route('/<int:event_id>', methods=['GET', 'DELETE'])
def get_delete(event_id): 
    if request.method == 'GET':
        flag = False
        for event in events_list:
            if event['id'] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return 'ID not Found!'

    if request.method == 'DELETE':
        flag = False
        for a in range(len(events_list)): 
            if events_list[a]['id'] == event_id: 
                del events_list[a]
                flag = True
                return 'Event deleted successfully!'

        if flag == False:
            return 'Not able to find ID!'

@events_blueprint.route('/all', methods=['GET'])
def get_all():
    return render_template('events.html', events=events_list)