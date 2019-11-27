from flask import Flask
import os
from controllers import client_blueprint, events_blueprint, jwt
from services import bcrypt
from models import db 




app = Flask (__name__)


app.config.from_object('config.Development')

db.init_app(app)
# ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)


app.register_blueprint(client_blueprint, url_prefix='/clients')
app.register_blueprint(events_blueprint, url_prefix='/events')





if __name__ == '__main__':
    app.run()