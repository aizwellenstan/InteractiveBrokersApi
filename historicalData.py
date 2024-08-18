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


# contractMNQ = Future(conId=637533593, symbol='MNQ', lastTradeDateOrContractMonth='20240920', multiplier='2', currency='USD', localSymbol='MNQU4', tradingClass='MNQ')
# ib.qualifyContracts(contractMNQ)
# contractN225M = Future(conId=618688988, symbol='N225M', lastTradeDateOrContractMonth='20240912', multiplier='100', currency='JPY', localSymbol='169090019', tradingClass='225M')
# contractN225 = Future(conId=618689007, symbol='N225', lastTradeDateOrContractMonth='20240912', multiplier='1000', currency='JPY', localSymbol='169090018', tradingClass='225')
# ib.qualifyContracts(contractN225)
# print(contractN225)
# contractMNTPX = Future(conId=670498961, symbol='MNTPX', lastTradeDateOrContractMonth='20240912', multiplier='1000', currency='JPY', localSymbol='169090006', tradingClass='TPXM')
# ib.qualifyContracts(contractMNTPX)
# contractN225MC = Future(conId=689341737, symbol='N225MC', lastTradeDateOrContractMonth='20240912', multiplier='10', currency='JPY', localSymbol='169090023', tradingClass='225MC')
# ib.qualifyContracts(contractN225MC)
# contractDJIA = Future(conId=654708006, symbol='DJIA', lastTradeDateOrContractMonth='20240920', multiplier='100', currency='JPY', localSymbol='169090073', tradingClass='DJIA')
# ib.qualifyContracts(contractDJIA)
# contractMGC = Future(conId=605552423, symbol='MGC', lastTradeDateOrContractMonth='20241227', multiplier='10', currency='USD', localSymbol='MGCZ4', tradingClass='MGC')
# # contractGC = Future(conId=347896248, symbol='GC', lastTradeDateOrContractMonth='20241227', multiplier='100', currency='USD', localSymbol='GCZ4', tradingClass='GC')
# ib.qualifyContracts(contractMGC)
# contractN225 = contractN225MC
# contractSCHG = Stock("SCHG", 'SMART', 'USD')
# ib.qualifyContracts(contractSCHG)
# contractQQQ = Stock("QQQ", 'SMART', 'USD')
# ib.qualifyContracts(contractQQQ)

# contractMES = Future(conId=637533398, symbol='MES', lastTradeDateOrContractMonth='20240920', multiplier='5', currency='USD', localSymbol='MESU4', tradingClass='MES')
# ib.qualifyContracts(contractMES)
contract = Stock("7203", 'TSEJ', 'JPY') # TSEJ / TOYOTA MOTOR CORPORATION
# contract = Stock(symbol, 'SMART', 'EUR') # Netherlands / ASML
ib.qualifyContracts(contract)
df = GetDataDf(contract)
print(df)

