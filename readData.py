import requests
import csv
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

api_File = open('APIKEY', 'r')
api_String = api_File.readline()
# print(api_String)










