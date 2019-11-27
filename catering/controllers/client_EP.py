from flask import Blueprint, request

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from services import bcrypt
from services.client_service import create_client

from models.client_model import Client


client_blueprint = Blueprint('client_api', __name__ )


@client_blueprint.route('/login', methods=['POST'])
def login ():
    body = request.json
    # email = body['email']
    # password = body['password']

    check_client = Client.query.filter_by(email = body['email']).first()
    if bcrypt.check_password_hash(check_client.password, password=body['password']):

        access_token = create_access_token(check_client.id)

        return {
            'message': 'logged in',
            'token': access_token
        }

    else:
        return {
            'message': 'try again'
        }
    


@client_blueprint.route('/register', methods=['POST'])
def register ():
   
    body = request.json

    email = body['email']
    password =bcrypt.generate_password_hash(body['password']).decode('utf-8')
    client_name = body['client_name']
    message = create_client(email, password, client_name)

    return {
        'message': message
    }


@client_blueprint.route('/logout', methods=['POST'])
def logout ():
    '''
    session token required
    purpose: de authenticate a clients token by blacklisting the token
    '''
    return 'user is logged out '



