import yfinance as yf                           #primarily for stocks, funds, indices etc.
import pandas as pd
from datetime import datetime, timedelta
from SignalGenerator import Buy_or_Sell_Signal

def fetchData(currency_pair, candles_back, interval): # pass string , int, string # 'EURUSD-X', 200, '15m'
    timeframe = interval[len(interval) - 1]
    interval = int(interval[:-1])
    end = datetime.today().now()
    if timeframe == 'd':
        start = end - timedelta(days=interval * candles_back)
    data = yf.download(str(currency_pair), start = start, end = end)
    dataframe = pd.DataFrame(data)
    return dataframe

if __name__ == "__main__":
    data = fetchData("BTC", 200, '1d')
    Buy = False
    Sell = False
    Neither = False

    while True:
        signal = Buy_or_Sell_Signal(data)
        if signal == 1:
            Buy = True
            Sell = False
            Neither = False
        elif signal == -1:
            Buy = False
            Sell = True
            Neither = False
        else:
            Buy = False
            Sell = False
            Neither = True

        #post(signal to the API) 



