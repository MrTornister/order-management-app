import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from services.google_sheets import GoogleSheetsService
from services.trello_service import TrelloService
from datetime import datetime

app = Flask(__name__)
CORS(app)

GOOGLE_SHEETS_URL = "https://docs.google.com/spreadsheets/d/1Lj3IJeVzfor_B35Jxo_nPQ6AREx27SlTBosZ-uwxOt0/edit#gid=0"
TRELLO_BOARD_ID = "your_trello_board_id"
TRELLO_LIST_ID = "your_trello_list_id"

google_sheets = GoogleSheetsService(GOOGLE_SHEETS_URL)
trello_service = TrelloService(os.getenv('TRELLO_API_KEY'), os.getenv('TRELLO_TOKEN'))

@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = google_sheets.get_products()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add-product', methods=['POST'])
def add_product():
    data = request.json
    try:
        new_product = google_sheets.add_product(data['name'])
        return jsonify(new_product)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submit-order', methods=['POST'])
def submit_order():
    order_data = request.json
    try:
        # Generowanie numeru zamówienia
        now = datetime.now()
        order_number = f"ZAM/{now.year % 100:02d}/{now.month:02d}/{google_sheets.get_next_order_number()}"
        
        # Zapis zamówienia do arkusza
        google_sheets.save_order(order_data, order_number)
        
        # Wysłanie do Trello
        trello_service.create_card(
            board_id=TRELLO_BOARD_ID, 
            list_id=TRELLO_LIST_ID,
            name=order_number,
            description=order_data['description'],
            labels=order_data['priority']
        )
        
        return jsonify({"order_number": order_number})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
