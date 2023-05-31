import requests
import csv

API_KEY = '<API_KEY>'
FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
DATATYPE = 'csv'

BIG_TECH_SYMBOL = ['AAPL', 'GOOGL', 'MSFT']


for symbol in BIG_TECH_SYMBOL:
    file_path = f'{symbol}_daily_full.csv'
    csv_url = f'https://www.alphavantage.co/query?function={FUNCTION}&symbol={symbol}&outputsize=full&datatype={DATATYPE}&apikey={API_KEY}'

    with requests.Session() as s:
        download = s.get(csv_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in my_list:
            writer.writerow(row)

