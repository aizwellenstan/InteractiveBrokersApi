from ib_insync import *
import pandas as pd

def GetDataDf(contract):
    data = ib.reqHistoricalData(
        contract, endDateTime='', durationStr='9 D',
        barSizeSetting='5 mins', whatToShow='TRADES', useRTH=False)
    df = pd.DataFrame(data)
    return df

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
symbol = "7203" # TOYOTA MOTOR CORPORATION
contract = Stock(symbol, 'TSEJ', 'JPY')
df = GetDataDf(contract)
print(df)

