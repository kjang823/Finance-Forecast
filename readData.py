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
        
"""

api_File = open('APIKEY', 'r')
api_String = api_File.readline()
# print(api_String)

class core_Stock_API:

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

class alpha_Intelligence:

    def news_Sentiment(self):
        url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def winning_Portfolio(self):
        url = 'https://www.alphavantage.co/query?function=TOURNAMENT_PORTFOLIO&season=2021-09&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

class fundamentals:

    def company_Overview(self):
        url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def income_Statement(self):
        url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def balance_Sheet(self):
        url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def cash_Flow(self):
        url = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def earnings(self):
        url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=demo'
        url = url.replace("demo",api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def listing_Delisting(self):
        CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo'
        CSV_URL = CSV_URL.replace('demo',api_String)
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            return my_list

    def earnings_Calendar(self):
        CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=demo'
        CSV_URL = CSV_URL.replace('demo',api_String)
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            return my_list

    def ipo_Calendar(self):
        CSV_URL = 'https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey=demo'
        CSV_URL = CSV_URL.replace('demo',api_String)
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            return my_list

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

class cryptocurrencies:
    def crypto_Exchange_Rates(self):
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def crypto_Daily(self):
        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def crypto_Weekly(self):
        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=CNY&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def crypto_Monthly(self):
        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=CNY&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

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

class technical_Indicators:

    def simple_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def exponential_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=EMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def weighted_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=WMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def double_Exponential_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=DEMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def triple_Exponential_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=TEMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def triangular_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=TRIMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def kaufman_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=KAMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def mesa_Adaptive_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=MAMA&symbol=IBM&interval=daily&series_type=close&fastlimit=0.02&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def voluma_Weighted_Average_Price(self):
        url = 'https://www.alphavantage.co/query?function=VWAP&symbol=IBM&interval=15min&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def triple_Exponential_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=T3&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data
