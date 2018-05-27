"""Binance API wrapper."""
import requests


class Base(object):
    """Base API class."""

    def __init__(self):
        """Base constructor."""
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
        """API constructor."""
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
        """Return `limit` most recent trades."""
        return self.get_api("trades", {"symbol": symbol, "limit": limit})

    def historical_trades(self, symbol="BTCUSDT", limit=None, fromId=None):
        """Return `limit` historical trades. Can query trades based on ID."""
        # TODO Needs API key!
        params = {"symbol": symbol, "limit": limit, "fromId": fromId}
        pass

    def agg_trades(
        self, symbol="BTCUSDT", limit=None, fromId=None, startTime=None, endTime=None
    ):
        """Return `limit` aggregated trades.
        Can query trades based on ID and time intervals (ms).
        """
        params = {
            "symbol": symbol,
            "limit": limit,
            "fromId": fromId,
            "startTime": startTime,
            "endTime": endTime,
        }
        return self.get_api("aggTrades", params)

    def klines(
        self, interval="1d", symbol="BTCUSDT", limit=None, startTime=None, endTime=None
    ):
        """Return `limit` klines. Intervals are: '1m', '5m', '1h', '1d', etc.
        Can query klines based on time intervals (ms).
        """
        params = {
            "symbol": symbol,
            "limit": limit,
            "interval": interval,
            "startTime": startTime,
            "endTime": endTime,
        }
        return self.get_api("klines", params)

    def daily_stats(self, symbol=None):
        """Return daily statistics of a symbol.
        If symbol is none, return statistics for all symbols.
        """
        return self.get_api("ticker/24hr", {"symbol": symbol})

    def price_ticker(self, symbol="BTCUSDT"):
        """Return latest price ticker of a symbol."""
        return self.get_api("ticker/price", {"symbol": symbol})

    def order_book_ticker(self, symbol="BTCUSDT"):
        """Return best price/quantity on the order book of a symbol."""
        return self.get_api("ticker/bookTicker", {"symbol": symbol})
