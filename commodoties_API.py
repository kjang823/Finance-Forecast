"""
Be aware that in order to properly use this file, the developer should request and API Key from the Alphavantage website.
Simply use the following url to request an API key.
URL: https://www.alphavantage.co/support/#api-key
Once you have generated your API key, simply create a text file within the same project called APIKEY and
copy paste the API key into the text file.
NOTE: most comments with print statements are meant for debugging purposes.
NOTE: There are no API calls made for Premium features. The list of these features includes:
        TIME_SERIES_DAILY
        FOREX_INTRADAY
        CRYPTOCURRENCIES_INTRADAY
        TECHNICAL_INDICATORS_STOCHASTIC_OSCILLATOR
        TECHNICAL_INDICATORS_RELATIVE_STRENGTH_INDEX
        TECHNICAL_INDICATORS_AVERAGE_DIRECTIONAL_MOVEMENT_INDEX
        TECHNICAL_INDICATORS_COMMODITY_CHANNEL_INDEX_VALUES
"""

import requests

api_File = open('APIKEY', 'r')
api_String = api_File.readline()

class commodoties:

    def crude_Oil_WTI(self):
        url = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def crude_Oil_Brent(self):
        url = 'https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def natural_Gas(self):
        url = 'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Copper(self):
        url = 'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Aluminum(self):
        url = 'https://www.alphavantage.co/query?function=ALUMINUM&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Wheat(self):
        url = 'https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Corn(self):
        url = 'https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Cotton(self):
        url = 'https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Sugar(self):
        url = 'https://www.alphavantage.co/query?function=SUGAR&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Of_Coffee(self):
        url = 'https://www.alphavantage.co/query?function=COFFEE&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def global_Price_Index_All_Commmodities(self):
        url = 'https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data