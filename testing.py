"""This is not (yet) a unit test module."""
from api import Api

if __name__ == "__main__":
    key = ""
    secret = ""
    api = Api(key=key, secret=secret)
    print(api.test_connection())
    print(api.server_time())
    print(api.exchange_info())
    print(api.order_book(symbol="BTCUSDT", limit=10))
    print(api.trades(symbol="BTCUSDT", limit=10))
    print(api.historical_trades(symbol="BTCUSDT"))
    print(api.klines("1h", symbol="BTCUSDT", limit=10))
    print(api.daily_stats(symbol="BTCUSDT"))
    print(api.price_ticker(symbol="BTCUSDT"))
    print(api.order_book_ticker(symbol="BTCUSDT"))
    print(api.open_orders(symbol="TRXBTC"))
