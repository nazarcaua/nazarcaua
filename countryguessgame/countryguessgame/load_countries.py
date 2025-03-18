import json
from django.conf import settings
import os

def load_countries():
    file_path = os.path.join(settings.BASE_DIR, 'countryguessgame/data/countries.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

countries = load_countries()