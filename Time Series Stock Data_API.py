"""
Be aware that in order to properly use this file, the developer should request and API Key from the Alphavantage website.
Simply use the following url to request an API key.
URL: https://www.alphavantage.co/support/#api-key
Once you have generated your API key, simply create a text file within the same project called APIKEY and
copy paste the API key into the text file.
NOTE: most comments with print statements are meant for debugging purposes.
NOTE: There are no API calls made for Premium features. The list of these features includes:
        TIME_SERIES_DAILY
"""

import requests
import csv

api_File = open('APIKEY', 'r')
api_String = api_File.readline()
class time_Series:

    def time_Series_Intraday(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def time_Series_Intraday_Extended(self):
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo'
        CSV_URL = CSV_URL.replace("demo",api_String)
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            return my_list

    def time_Series_Daily_Adjusted(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def time_Series_Weekly(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def time_Series_Weekly_Adjusted(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def time_Series_Monthly(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def time_Series_Monthly_Adjusted(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def quote_Endpoint(self):
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data
    def ticker_Search(self):
        url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def market_Open_Close(self):
        url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data