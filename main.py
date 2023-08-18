import yfinance as yf                           #primarily for stocks, funds, indices etc.
import pandas as pd
from datetime import datetime, timedelta
from Support_and_Resistance import choose_num_of_clusters, get_Support_and_Resistance, plot_clusters
from CandleStick_Patterns import DragonFly_Doji

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
    number_of_clusters = choose_num_of_clusters(data)
    sup_and_res = get_Support_and_Resistance(data, number_of_clusters)
    # plot_clusters(data, sup_and_res=sup_and_res)
    # print(DragonFly_Doji(data))
