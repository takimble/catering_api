from models.client_model import Client

def create_client(email, password,client_name):

    new_client = Client(email, password, client_name)
    return new_client.save()