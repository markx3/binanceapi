# Binance API wrapper
This is a work in progress Binance API wrapper. As of now, you can use it to
access Binance's public endpoints.

## Requirements
* `requests`

## Example
Let's say you're interested in getting candlesticks data for `BTCUSDT` pair on
Binance. You want to work with 5-minute interval candles, with a maximum amount
of 2 candles in your analysis. Here's what you need to do:
```python
api = Api()
klines = api.klines(symbol="BTCUSDT", interval="5m", limit=2)
```
Inspecting `klines`, you would get:
```json
[  
   [  
      1527403500000,
      "7291.08000000",
      "7293.65000000",
      "7277.70000000",
      "7289.54000000",
      "68.23215800",
      1527403799999,
      "497165.85993717",
      1311,
      "36.40716700",
      "265274.27469882",
      "0"
   ],
   [  
      1527403800000,
      "7287.11000000",
      "7289.54000000",
      "7281.23000000",
      "7288.38000000",
      "4.93415000",
      1527404099999,
      "35951.85631080",
      737,
      "4.00030500",
      "29151.86755480",
      "0"
   ]
]
```