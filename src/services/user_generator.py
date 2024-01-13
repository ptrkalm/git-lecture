import requests
from src.models.user import User

base_path = "https://randomuser.me/api"

def generate_user(gender=None):
    path = base_path
    if gender!=None:
        path = path + '/?gender=' + gender

    user = requests.get(path).json()['results'][0]
    first_name = user['name']['first']
    last_name = user['name']['last']
    gender = user['gender']
    return User(first_name + ' ' + last_name, gender)
