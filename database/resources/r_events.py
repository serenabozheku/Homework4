from flask_restful import Resource
from flask import jsonify

events_list = [
    {'id': 1, 'name_event': 'Spring Fest'},
    {'id': 2, 'name_event': 'Colors Festivals'},
    {'id': 3, 'name_event': 'Carnivals'}
]

class First(Resource):
    
    def put(self,event_id,name):   
        for m in events_list:
            if m['id'] == event_id:
                m.update({'name_event': name})
                return jsonify(m)

        events_list.append(dict({'id': event_id, 'name_event': name}))
        return jsonify(events_list)

def post(self,event_id,name):  
        id_exist = False
        for n in range(len(events_list)):
            if events_list[n-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name_event': name}))
            return jsonify(events_list)
        else:
            return 'ID already exist'

    

class Second(Resource):

    def get(self, event_id):  #Get Method
        flag = False
        for event in events_list:
            if event['id'] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return 'ID not Found!'
       
    def delete(self, event_id):      #Delete method
        flag = False
        for a in range(len(events_list)): 
            if events_list[a]['id'] == event_id: 
                del events_list[a]
                flag = True
                return 'Event deleted successfully!'

        if flag == False:
            return 'Not able to find ID!'

class all_events(Resource):
    def get(self):
        return jsonify(events_list)