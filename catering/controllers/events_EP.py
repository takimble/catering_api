from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.event_services import new_event_post, fetch_events, fetch_one, delete_event, edit_event

from models.event_model import Events

events_blueprint = Blueprint ('event_api', __name__)

@events_blueprint.route ('/new', methods=['POST'])
# @jwt_required
def new_event ():
    user = get_jwt_identity()
    data = request.json
    return new_event_post(data, user)


@events_blueprint.route('/all', methods=['GET'])
# @jwt_required
def all_events ():
    x = fetch_events()
    return custom_response(x, 200)


@events_blueprint.route('/<int:event_id>', methods = ['GET', 'PUT', 'DELETE'])
# @jwt_required
def single_event(event_id):
    if request.method == 'GET':
        event = fetch_one(event_id)
        if event:
            return custom_response(event, 200)
    
    elif request.method == 'PUT':
        data = request.json
        user =1
        event = fetch_one(event_id)
        if user == event['client_id']:
            return custom_response(edit_event(event_id,data),200)
    
    elif request.method == 'DELETE':
        user = 1
        event= fetch_one(event_id)
        if user == event['client_id']:
            return custom_response(delete_event(event),200)
    
    else:
        return 'method'



def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
