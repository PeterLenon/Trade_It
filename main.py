import yfinance as yf  # primarily for stocks, funds, indices etc.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from SignalGenerator import Buy_or_Sell_Signal
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails, MarketOrderRequest
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from AccountConfig import API_access_token, account_ID, currency_pair, chart_granularity, timeframe, timeInterval
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def fetchData(trading_instrument, candles_back, interval):  # pass string , int, string # 'EURUSD-X', 200, '15m'
    timeframe = interval[len(interval) - 1]
    interval = int(interval[:-1])
    end = datetime.today().now()
    if timeframe == 'd':
        start = end - timedelta(days=interval * candles_back)
    data = yf.download(str(trading_instrument), start=start, end=end)
    dataframe = pd.DataFrame(data)
    return dataframe


if __name__ == "__main__":
    def tradeIt():
        def takeProfit(buy, sell):
            candle = data.iloc[-1:]
            if buy:
                for line in support_and_resistance_lines:
                    if np.array(candle['High'])[0] + 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0])) < line:
                        return line
                return np.array(candle['High'])[0] + 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0]))
            elif sell:
                for index in range(len(support_and_resistance_lines) - 1, -1, -1):
                    if support_and_resistance_lines[index] < np.array(candle['Low'])[0] - 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0])):
                        return support_and_resistance_lines[index]
                return np.array(candle['Low'])[0] - 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0]))

        def stopLoss(buy, sell):
            candle = data.iloc[-1:]
            if buy:
                for index in range(len(support_and_resistance_lines) - 1, -1, -1):
                    if support_and_resistance_lines[index] < np.array(candle['Low'])[0] - 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0])):
                        return support_and_resistance_lines[index]
                return np.array(candle['Low'])[0] - 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0]))
            elif sell:
                for line in support_and_resistance_lines:
                    if line > np.array(candle['High'])[0] + 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0])):
                        return line
                return np.array(candle['High'])[0] + 2 * (
                    abs(np.array(candle['Close'])[0] - np.array(candle['Open'])[0]))

        support_and_resistance_lines = []
        Buy = False
        Sell = False
        Neither = False
        data = fetchData(currency_pair, 200, chart_granularity)
        signal = Buy_or_Sell_Signal(data, support_and_resistance_lines)
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

        # post(signal to the API)
        client = API(API_access_token)

        if Buy:
            TPBuy = takeProfit(Buy, Sell)
            SLBuy = stopLoss(Buy, Sell)
            mo = MarketOrderRequest(instrument="BTC", units=1000, takeProfitOnFill=TakeProfitDetails(price=TPBuy),
                                    stopLossOnFill=StopLossDetails(price=SLBuy))
            r = orders.OrderCreate(account_ID, data=mo.data)
            rv = client.request(r)
            print(rv)
        elif Sell:
            TPSell = takeProfit(Buy, Sell)
            SLSell = stopLoss(Buy, Sell)
            mo = MarketOrderRequest(instrument="BTC", units=-1000, takeProfitOnFill=TakeProfitDetails(price=TPSell),
                                    stopLossOnFill=StopLossDetails(price=SLSell))
            r = orders.OrderCreate(account_ID, data=mo.data)
            rv = client.request(r)
            print(rv)
        elif Neither:
            print("waiting for the right time to enter the market!")


    scheduler = BlockingScheduler()
    if timeframe == 'm':
        scheduler.add_job(tradeIt, "interval", minutes= timeInterval)
    elif timeframe == 'h':
        scheduler.add_job(tradeIt, "interval", hours=timeInterval)
    elif timeframe == 'd':
        scheduler.add_job(tradeIt, "interval", days=timeInterval)
    elif timeframe == 'W':
        scheduler.add_job(tradeIt, "interval", weeks=timeInterval)
    elif timeframe == 'Mo':
        scheduler.add_job(tradeIt, "interval", months=timeInterval)
    scheduler.start()
