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

class economic_Indicators:
    def real_GDP(self):
        url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def real_GDP_Per_Capita(self):
        url = 'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def treasury_Yield(self):
        url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def federal_Funds_Rate(self):
        url = 'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def consumer_Price_Index(self):
        url = 'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def inflation_Rates(self):
        url = 'https://www.alphavantage.co/query?function=INFLATION&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def retail_Sales(self):
        url = 'https://www.alphavantage.co/query?function=RETAIL_SALES&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def durables(self):
        url = 'https://www.alphavantage.co/query?function=DURABLES&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def unemployment_Rates(self):
        url = 'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def total_Non_Farm_Payroll(self):
        url = 'https://www.alphavantage.co/query?function=NONFARM_PAYROLL&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data