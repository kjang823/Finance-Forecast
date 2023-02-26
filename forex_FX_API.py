"""
Be aware that in order to properly use this file, the developer should request and API Key from the Alphavantage website.
Simply use the following url to request an API key.
URL: https://www.alphavantage.co/support/#api-key
Once you have generated your API key, simply create a text file within the same project called APIKEY and
copy paste the API key into the text file.
NOTE: most comments with print statements are meant for debugging purposes.
NOTE: There are no API calls made for Premium features. The list of these features includes:
        FOREX_INTRADAY

"""

import requests

api_File = open('APIKEY', 'r')
api_String = api_File.readline()

class forex:

    def currency_Exchange_Rates(self):
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def fx_Daily(self):
        url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def fx_Weekly(self):
        url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def fx_Monthly(self):
        url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data