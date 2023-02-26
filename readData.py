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

    def moving_Average_Convergence_Divergence(self):
        url = 'https://www.alphavantage.co/query?function=MACD&symbol=IBM&interval=daily&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def moving_Average_Converge_Diverge_Control_Average(self):
        url = 'https://www.alphavantage.co/query?function=MACDEXT&symbol=IBM&interval=daily&series_type=open&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def stochastic_Fast(self):
        url = 'https://www.alphavantage.co/query?function=STOCHF&symbol=IBM&interval=daily&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def stochastic_Relative_Strength_Index(self):
        url = 'https://www.alphavantage.co/query?function=STOCHRSI&symbol=IBM&interval=daily&time_period=10&series_type=close&fastkperiod=6&fastdmatype=1&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def williams_Percentage(self):
        url = 'https://www.alphavantage.co/query?function=WILLR&symbol=IBM&interval=daily&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def average_Directional_Movement_Index_Rating(self):
        url = 'https://www.alphavantage.co/query?function=ADXR&symbol=IBM&interval=daily&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def absolute_Price_Oscillator(self):
        url = 'https://www.alphavantage.co/query?function=APO&symbol=IBM&interval=daily&series_type=close&fastperiod=10&matype=1&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def percentage_Price_Oscillator(self):
        url = 'https://www.alphavantage.co/query?function=PPO&symbol=IBM&interval=daily&series_type=close&fastperiod=10&matype=1&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def momentum(self):
        url = 'https://www.alphavantage.co/query?function=MOM&symbol=IBM&interval=daily&time_period=10&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def balance_Of_Power(self):
        url = 'https://www.alphavantage.co/query?function=BOP&symbol=IBM&interval=daily&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def chande_Momentum_Oscillator(self):
        url = 'https://www.alphavantage.co/query?function=CMO&symbol=IBM&interval=weekly&time_period=10&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def rate_Of_Change(self):
        url = 'https://www.alphavantage.co/query?function=ROC&symbol=IBM&interval=weekly&time_period=10&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def rate_Of_Change_Ratio(self):
        url = 'https://www.alphavantage.co/query?function=ROCR&symbol=IBM&interval=daily&time_period=10&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def aroon(self):
        url = 'https://www.alphavantage.co/query?function=AROON&symbol=IBM&interval=daily&time_period=14&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def aroon_Oscillator(self):
        url = 'https://www.alphavantage.co/query?function=AROONOSC&symbol=IBM&interval=daily&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def money_Flow_Index(self):
        url = 'https://www.alphavantage.co/query?function=MFI&symbol=IBM&interval=weekly&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def triple_Smooth_Exponential_Moving_Average(self):
        url = 'https://www.alphavantage.co/query?function=TRIX&symbol=IBM&interval=daily&time_period=10&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def ultimate_Oscillator(self):
        url = 'https://www.alphavantage.co/query?function=ULTOSC&symbol=IBM&interval=daily&timeperiod1=8&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def directional_Movement_Index(self):
        url = 'https://www.alphavantage.co/query?function=DX&symbol=IBM&interval=daily&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def minus_Directional_Indicator(self):
        url = 'https://www.alphavantage.co/query?function=MINUS_DI&symbol=IBM&interval=weekly&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def plus_Directional_Indicator(self):
        url = 'https://www.alphavantage.co/query?function=PLUS_DI&symbol=IBM&interval=daily&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def bollinger_Brands(self):
        url = 'https://www.alphavantage.co/query?function=BBANDS&symbol=IBM&interval=weekly&time_period=5&series_type=close&nbdevup=3&nbdevdn=3&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def midpoint(self):
        url = 'https://www.alphavantage.co/query?function=MIDPOINT&symbol=IBM&interval=daily&time_period=10&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def midprice(self):
        url = 'https://www.alphavantage.co/query?function=MIDPRICE&symbol=IBM&interval=daily&time_period=10&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def parabolic_Stop_And_Reverse(self):
        url = 'https://www.alphavantage.co/query?function=SAR&symbol=IBM&interval=weekly&acceleration=0.05&maximum=0.25&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def true_Range(self):
        url = 'https://www.alphavantage.co/query?function=TRANGE&symbol=IBM&interval=daily&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def average_True_Range(self):
        url = 'https://www.alphavantage.co/query?function=ATR&symbol=IBM&interval=daily&time_period=14&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def normalized_Average_True_Range(self):
        url = 'https://www.alphavantage.co/query?function=NATR&symbol=IBM&interval=weekly&time_period=14&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def chaikin_Accumulation_Distribution_Line(self):
        url = 'https://www.alphavantage.co/query?function=AD&symbol=IBM&interval=daily&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def chaikin_Accumulation_Distribution_Oscillator(self):
        url = 'https://www.alphavantage.co/query?function=ADOSC&symbol=IBM&interval=daily&fastperiod=5&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def onbalance_Volume(self):
        url = 'https://www.alphavantage.co/query?function=OBV&symbol=IBM&interval=weekly&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def hilbert_Transform_Instantaneous_Trendline(self):
        url = 'https://www.alphavantage.co/query?function=HT_TRENDLINE&symbol=IBM&interval=daily&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def hilbert_Transform_Sine_Wave(self):
        url = 'https://www.alphavantage.co/query?function=HT_SINE&symbol=IBM&interval=daily&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def hilbert_Transform_Trend_Cycle(self):
        url = 'https://www.alphavantage.co/query?function=HT_TRENDMODE&symbol=IBM&interval=weekly&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def hilbert_Transform_Dominant_Cycle(self):
        url = 'https://www.alphavantage.co/query?function=HT_DCPERIOD&symbol=IBM&interval=daily&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data

    def hilbert_Transform_Phasor_Componenets(self):
        url = 'https://www.alphavantage.co/query?function=HT_PHASOR&symbol=IBM&interval=weekly&series_type=close&apikey=demo'
        url = url.replace("demo", api_String)
        r = requests.get(url)
        data = r.json()
        return data


