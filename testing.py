from api import Api

if __name__ == "__main__":
    api = Api()
    print(api.test_connection())
    print(api.server_time())
    # print(api.exchange_info())
    print(api.order_book(symbol="TRXBTC", limit=10))
    print(api.trades(symbol="TRXBTC", limit=10))
    print(api.historical_trades(symbol="TRXBTC"))
    print(api.klines("1d", symbol="TRXBTC", limit=10))
    print(api.daily_stats(symbol="TRXBTC"))
    print(api.price_ticker(symbol="TRXBTC"))
