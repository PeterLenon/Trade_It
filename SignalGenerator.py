from CandleStick_Patterns import pattern_Signals, getLastCandle
from Support_and_Resistance import get_Support_and_Resistance, choose_num_of_clusters
import numpy as np


# if signal > 0(+ve) then its a buy signal else if a signal < 0 the its a sell signal else do nothing
def Buy_or_Sell_Signal(data):
    def nearest_supp_and_res_lines(candle):
        Open = np.array(candle.Open)[0]
        Close = np.array(candle.Close)[0]
        High = np.array(candle.High)[0]
        Low = np.array(candle.Low)[0]
        lines = [-1, -1, -1]
        for line in support_and_resistance_lines:
            if line in range(Close, Open):
                lines[1] = line
                return lines

        left, right = 0, len(support_and_resistance_lines)-1
        while left <= right:
            if Low <= support_and_resistance_lines[left]: # this logic requires use of pip ranges not raw numbers
                pass





    support_and_resistance_lines = get_Support_and_Resistance(dataframe=data,
                                                              optimal_cluster_size=choose_num_of_clusters(data))
    candle_stick_patterns = pattern_Signals(data)
    sentiment_index = sum(signal for signal in candle_stick_patterns)
    if sentiment_index > 0:
        last_candle = getLastCandle(data)

