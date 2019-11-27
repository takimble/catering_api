from . import bcrypt

def generate_password_hash(password):
    get_hash = bcrypt.generate_password_hash(password)
    return get_hash