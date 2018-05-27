import requests


class Base(object):
    """Base API class."""

    def __init__(self):
        """Base Constructor."""
        self.host = "api.binance.com"

    def get_api(self, action, params=None):
        """Default get method"""
        response = requests.get(
            "https://%s/api/v1/%s" % (self.host, action), params=params
        )
        return response.json()


class Api(Base):
    """API Class."""

    def __init__(self):
        """API Constructor."""
        Base.__init__(self)

    def test_connection(self):
        """Ping server."""
        return self.get_api("ping")

    def server_time(self):
        """Return server time."""
        return self.get_api("time")

    def exchange_info(self):
        """Return exchange info."""
        return self.get_api("exchangeInfo")

    def order_book(self, symbol="BTCUSDT", limit=None):
        """Return order book."""
        return self.get_api("depth", {"symbol": symbol, "limit": limit})

    def trades(self, symbol="BTCUSDT", limit=None):
        return self.get_api("trades", {"symbol": symbol, "limit": limit})

    def historical_trades(self, symbol="BTCUSDT", limit=None, fromId=None):
        # TODO Needs API key!
        params = {"symbol": symbol, "limit": limit, "fromId": fromId}
        pass

    def agg_trades(
        self, symbol="BTCUSDT", limit=None, fromId=None, startTime=None, endTime=None
    ):
        params = {
            "symbol": symbol,
            "limit": limit,
            "fromId": fromId,
            "startTime": startTime,
            "endTime": endTime,
        }
        return self.get_api("aggTrades", params)

    def klines(
        self, interval, symbol="BTCUSDT", limit=None, startTime=None, endTime=None
    ):
        params = {
            "symbol": symbol,
            "limit": limit,
            "startTime": startTime,
            "endTime": endTime,
        }
        return self.get_api("klines", params)

    def daily_stats(self, symbol="BTCUSDT"):
        return self.get_api("ticker/24hr", {"symbol": symbol})

    def price_ticker(self, symbol="BTCUSDT"):
        return self.get_api("ticker/price", {"symbol": symbol})

    def order_book_ticker(self, symbol="BTCUSDT"):
        return self.get_api("ticker/bookTicker", {"symbol": symbol})
