### 1 is bullish and -1 bearish and )is inconclusive
import numpy as np

def Engulfing_Bar(dataframe):
    candle_last = dataframe.iloc[-1:]
    candle_2nd_last = dataframe.iloc[-2:]
    if np.array(candle_2nd_last.Close)[0] <= np.array(candle_last.Open)[0] and np.arrray(candle_2nd_last.Open)[0] > np.array(candle_2nd_last.Close)[0]: #bearish engulfing bar
        return -1
    elif np.array(candle_2nd_last.Close)[0] >= np.array(candle_last.Open)[0] and np.array(candle_2nd_last.Open)[0] < np.array(candle_last.Close)[0]:
        return 1
    return 0

def DragonFly_Doji(dataframe):
    candle = dataframe.iloc[-1:]
    candle_body_size = abs(np.array(candle.Open)[0] - np.array(candle.Close)[0])
    candle_size = abs(np.array(candle.High)[0] - np.array(candle.Low)[0])
    if candle_body_size/candle_size <= 0.25:
        if candle_body_size/(candle.Low - candle.close) <= 0.5:
            return 1
        elif candle_body_size/(candle.High - candle.Close) <= 0.5:
            return -1
    return 0

def Morning_or_Evening_Star(dataframe):
    candle1 = dataframe.iloc[-1:]
    candle2 = dataframe.iloc[-2:]
    candle3 = dataframe.iloc[-3:]
    if np.array(candle3.Open)[0] > np.array(candle2.Open)[0] and np.array(candle3.Close)[0] >= np.array(candle2.Open)[0] and np.array(candle2.Close)[0] < np.array(candle2.Open) and np.array(candle1.Close)[0] > np.array(candle1.Open)[0] and np.array(candle1.Close)[0] > np.array(candle2.Open)[0]:
        return 1
    elif np.array(candle3.Close)[0] > np.array(candle3.Open)[0] and np.array(candle2.Close)[0] < np.array(candle2.Open)[0] and np.array(candle1.Open)[0] > np.array(candle1.Close) and np.array(candle1.Open)[0] < np.array(candle2.Close)[0]:
        return -1
    return 0

def Tweezer_Bottom_and_Top(dataframe):
    candle1 = dataframe[-1:]
    candle2 = dataframe[-2:]

    candle1_size = np.array(candle1.Close)[0] - np.array(candle1.Open)[0]
    candle2_size = np.array(candle2.Close)[0] - np.array(candle2.Open)[0]
    if candle1_size > 0 and candle2_size < 0:
         if abs(candle1_size/candle2_size) > 0.90:
             return 1
    elif candle1_size < 0 and candle2_size < 0:
        if abs(candle1_size/candle2_size) > 0.90:
            return -1
    return 0

def pattern_Signals(dataframe):
    signals = [Engulfing_Bar(dataframe), DragonFly_Doji(dataframe), Morning_or_Evening_Star(dataframe), Tweezer_Bottom_and_Top(dataframe)]
    return signals

