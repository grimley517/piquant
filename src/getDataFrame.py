from openbb import obb

def getDataFrameForSymbol(symbol):
    obb.user.preferences.output_type = "dataframe"
    data = obb.equity.price.historical(
        symbol, 
        provider = "yfinance")
    return (data)

def getFundamentalMetricsForSymbols(symbols:list):
    stringList = ",".join(symbols)
    obb.user.preferences.output_type = "dataframe"
    data = obb.equity.fundamental.metrics(
        stringList, 
        provider = "yfinance")
    return (data)

if __name__ == "__main__":
    print(getDataFrameForSymbol("SPY"))
    print(getFundamentalMetricsForSymbols(["AAPL", "MSFT", "GOOGL"]))