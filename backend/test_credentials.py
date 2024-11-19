import os
from dotenv import load_dotenv
import requests
import google.auth

# Załaduj zmienne środowiskowe
load_dotenv()

def test_trello():
    auth_params = {
        'key': os.getenv('TRELLO_API_KEY'),
        'token': os.getenv('TRELLO_TOKEN')
    }
    response = requests.get('https://api.trello.com/1/members/me/boards', params=auth_params)
    print("Trello status:", response.status_code)
    if response.status_code == 200:
        print("Trello API działa poprawnie!")
    else:
        print("Problem z Trello API")

def test_google():
    try:
        credentials, project = google.auth.default()
        print("Google credentials załadowane poprawnie!")
    except Exception as e:
        print("Problem z Google credentials:", str(e))

if __name__ == "__main__":
    test_trello()
    test_google()
