from models.event_model import Events, EventSchema

event_schema = EventSchema()


def new_event_post(data,user):
    new_event = Events(
        title = data['title'],
        menu_choice = data['menu_choice'],
        date = data['date'],
        client_id = data['client_id']
    )

    try:
        new_event_post.save()
        message = {
            'message': 'event saved'
        }
        return message,200
    except Exception as e:
        return str(e),400 

def fetch_events():
    x = Events.get_all_events()
    event_posts = event_schema.dump(x, many=True)
    return event_posts

def fetch_one(event_id):
    x = Events.get_single_event(event_id)
    event_posts= event_schema.dump(x)
    return event_posts

def edit_event(event_id, data):
    x =Events.get_single_event(event_id)
    updated = x.update(x,data)
    new_event= event_schema.dump(updated)
    return new_event

def delete_event(event):
    x =Events.get_single_event(event['id'])
    x.delete()
    return 'event is deleted '
