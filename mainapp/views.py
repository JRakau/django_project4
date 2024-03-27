from django.http.response import HttpResponse
from django.shortcuts import render
import requests


from typing import List

# dX4gER*E6GN!yEZ */


api_key = "74fee5c279404d629efab122626502bb"


# Create your views here
def stockPicker(request):
    stock_picker = ['AAPL', 'TSLA', 'AMZN', 'NFLX']
    return render(request, 'mainapp/stockpicker.html', {'stockpicker': stock_picker})


def stockTracker(request):
   #

    stockpicker = request.GET.getlist('stockpicker')
    stockshare = str(stockpicker)[1:-1]
    txt = "Symbol:"
    i = 0

    print(stockpicker)
    for ticker_input in stockpicker:
        if i == 0:
            txt = "{}{}".format(txt, ticker_input)
        else:
            txt = "{},{}".format(txt, ticker_input)

        i += 1

    data = get_stock_quote('symbol', 'stockpicker')

    print(txt)

    print(stockshare)
    print("\n L1")
    test1 = data['AAPL']
    print(test1)
    print("\n L2")
    print(test1['meta'])
    print("\n L3")
    test1 = test1['meta']
    print(test1['symbol'])

    return render(request, 'mainapp/stocktracker.html', {'data': data, 'selectedstock': stockshare})


class MyStock:
    """
    My Stock class
    """

    def __init__(self, symbol, name, high_price):
        # instance attribute
        self.symbol = symbol
        self.name = name
        self.high_price = high_price


def get_stock_quote(ticker, key):
    """Get a quote for a given ticker symbol using API

    Args:
        ticker (String): AAPL Apple stocks or  MSFT Microsoft stocks
        key (String): API Key to access the API

    Returns:
        _type_: This request will return JSON with the following structure
        {
            "symbol": "AAPL",
            "name": "Apple Inc",
            "exchange": "NASDAQ",
            "mic_code": "XNAS",
            "currency": "USD",
            "datetime": "2021-09-16",
            "timestamp": 1631772000,
            "open": "148.44000",
            "high": "148.96840",
             "low": "147.22099",
            "close": "148.85001",
            "volume": "67903927",
            "previous_close": "149.09000",
            "change": "-0.23999",
            "percent_change": "-0.16097",
            "average_volume": "83571571",
            "rolling_1d_change": "123.123",
            "rolling_7d_change": "123.123",
            "rolling_period_change": "123.123"
            "is_market_open": false,
            "fifty_two_week": {
                "low": "103.10000",
                "high": "157.25999",
                "low_change": "45.75001",
                "high_change": "-8.40999",
                "low_change_percent": "44.37440",
                "high_change_percent": "-5.34782",
                "range": "103.099998 - 157.259995"
            },
            "extended_change": "0.09",
            "extended_percent_change": "0.05",
            "extended_price": "125.22",
            "extended_timestamp": 1649845281
            }
    """
    url = f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={key}"
    url = 'https://api.twelvedata.com/time_series?symbol=AAPL,EUR/USD,IXIC&interval=1min&apikey=demo'

    json_resp = 0
    try:
        json_resp = requests.get(url).json()
        print("Request: " + json_resp)

    except OSError as err:
        print("OS error:", err)

    except ValueError:
        print("Could not convert data.")

    except Exception as err:
        print(f"Unexpected on get_stock_quote() {err=}, {type(err)=}")
        print("Oops! Try again...")

    return json_resp
