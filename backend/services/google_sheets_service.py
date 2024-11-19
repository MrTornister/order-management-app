import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsService:
    def __init__(self, spreadsheet_url):
        scope = ['https://spreadsheets.google.com/feeds', 
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'credentials.json', scope)
        self.client = gspread.authorize(credentials)
        self.spreadsheet = self.client.open_by_url(spreadsheet_url)
        
    def get_products(self):
        products_sheet = self.spreadsheet.worksheet('Produkty')
        return products_sheet.get_all_records()
    
    def add_product(self, product_name):
        products_sheet = self.spreadsheet.worksheet('Produkty')
        new_product = {
            'nazwa': product_name, 
            'status': 'aktywny'
        }
        products_sheet.append_row(list(new_product.values()))
        return new_product
    
    def get_next_order_number(self):
        orders_sheet = self.spreadsheet.worksheet('Zamówienia')
        return len(orders_sheet.get_all_records()) + 1
    
    def save_order(self, order_data, order_number):
        orders_sheet = self.spreadsheet.worksheet('Zamówienia')
        row_data = [
            order_number,
            order_data['user_name'],
            ', '.join(order_data['products']),
            order_data['priority']
        ]
        orders_sheet.append_row(row_data)
