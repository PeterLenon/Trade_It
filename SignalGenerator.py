from CandleStick_Patterns import pattern_Signals, getLastCandle
from Support_and_Resistance import get_Support_and_Resistance, choose_num_of_clusters
import numpy as np


# if signal > 0(+ve) then its a buy signal else if a signal < 0 the its a sell signal else do nothing
def Buy_or_Sell_Signal(dataframe):
    def nearest_supp_and_res_lines(candle):
        Open = np.array(candle.Open)[0]
        Close = np.array(candle.Close)[0]
        High = np.array(candle.High)[0]
        Low = np.array(candle.Low)[0]
        lines = [-1, -1]
        for line in support_and_resistance_lines:
            if line in range(Close, Open):
                lines[1] = line
                return lines

        left, right = 0, len(support_and_resistance_lines)-1
        res = -1
        sup = -1
        while left <= right:
            if Close > Open:
                if support_and_resistance_lines[left] <= (Open + (Close-Open)/2):
                    res = left
                if support_and_resistance_lines[right] >= (Open + (Close - Open)/2):
                    sup = right
            else:
                if support_and_resistance_lines[left] <= (Close +(Open - Close)/2):
                    res = left
                if support_and_resistance_lines[right] >= (Close +(Open - Close)/2):
                    sup = right
            left += 1
            right -= 1
        lines = [res, sup]
        return lines


    support_and_resistance_lines = get_Support_and_Resistance(dataframe=dataframe,
                                                              optimal_cluster_size=choose_num_of_clusters(dataframe))
    candle_stick_patterns = pattern_Signals(dataframe)
    sentiment_index = sum(signal for signal in candle_stick_patterns)
    last_candle = getLastCandle(dataframe)
    supp_and_res = nearest_supp_and_res_lines(last_candle)
    if sentiment_index > 0:
        support = supp_and_res[0]
        if abs(np.array(last_candle.Lowest)[0] - support) <= (np.array(last_candle.Close)[0] + np.array(np.array(last_candle.Open))[0])/2 - np.array(last_candle.Low)[0]:
            return 1
    elif sentiment_index < 0:
        res = supp_and_res[1]
        if abs(res - np.array(last_candle.Highest)[0]) <= np.array(last_candle.Highest)[0] - (np.array(last_candle.Close)[0] + np.array(last_candle)[0])/2:
            return -1
    return 0


