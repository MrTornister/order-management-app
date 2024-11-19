import requests

class TrelloService:
    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token
        self.base_url = "https://api.trello.com/1"
    
    def create_card(self, board_id, list_id, name, description, labels):
        url = f"{self.base_url}/cards"
        
        labels_map = {
            "Zostały ostatnie sztuki": "green",
            "Brak na stanie - bardzo pilne !!!": "red", 
            "Uzupełnienie magazynu": "yellow"
        }
        
        params = {
            "key": self.api_key,
            "token": self.token,
            "idList": list_id,
            "name": name,
            "desc": description,
            "idLabels": [labels_map.get(labels, "green")]
        }
        
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json()
