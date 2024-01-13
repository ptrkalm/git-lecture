import requests
import json
from src.models.user import User

base_path = "https://randomuser.me/api"

def generate_user(gender=None):
    if (gender == None):
        user = requests.get(base_path).json()['results'][0]
        first_name = user['name']['first']
        last_name = user['name']['last']
        return User(first_name + ' ' + last_name)
    else:
        return None