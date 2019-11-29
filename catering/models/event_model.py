import datetime
from . import db
from marshmallow import Schema, fields

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    menu_choice = db.Column(db.Integer,nullable = False)
    date = db.Column(db.DateTime)
    client_id = db.Column(db.ForeignKey('client.id'))


    def __init__(self, title, menu_choice, client_id):
        self.title = title
        self.menu_choice = menu_choice
        self.client_id  = client_id

    def save_event (self):
        db.session.add(self)
        db.session.commit()
        return ' event saved'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    @staticmethod
    def get_all_events():
        return Events.query.all()
   
   
    @staticmethod
    def get_single_event (event_id):
        return Events.query.filter_by(id=event_id).first()
    
class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    client_id = fields.Int(dump_only =True)
    title = fields.Str(required=True)
    menu_choice = fields.Str(required=True)
    date=fields.Int(required=True)

       

