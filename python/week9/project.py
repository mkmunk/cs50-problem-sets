import yfinance as yf
import sys


def main():
    try:
        ticker = input("Stock number: ")
        info, history = get_stock_data(ticker)
        five_year_change = calculate_five_year_change(history)
        result = display_stock_info(info, five_year_change)
        print(result)
    except IndexError:
        sys.exit("Stock not found")

def get_stock_data(ticker):
    # 抓取股票基本面資料
    stock = yf.Ticker(ticker)
    info = stock.info
    history = stock.history(period = "5y").dropna()
    return (info, history)


def calculate_five_year_change(history):
    # 計算5年漲跌幅
    first_close = history["Close"].iloc[0]
    last_close = history["Close"].iloc[-1]
    five_year = (last_close - first_close) / first_close * 100
    return f"{five_year:.2f}%"

def display_stock_info(info, five_year_change):
    # 整理並顯示資訊
    # 公司名稱、產業
    result = f"Company Name: {info['longName']}\n"
    result += f"Sector: {info['sector']}\n"
    # 公司股價、年度區間
    result += f"Current Price: {info['currentPrice']}\n"
    result += f"52-Week Range: {info['fiftyTwoWeekLow']} - {info['fiftyTwoWeekHigh']}\n"
    # 公司市值、本益比
    result += f"Market Cap: {info['marketCap']}\n"
    result += f"P/E Ratio: {info['trailingPE']}\n"
    # 公司5年漲跌幅
    result += f"5-Year Change: {five_year_change}\n"
    # 公司每股盈餘+淨利率+股息殖利率
    result += f"EPS: {info['trailingEps']}\n"
    result += f"Profit Margin: {info['profitMargins']}\n"
    result += f"Dividend Yield: {info['dividendYield']}"

    return result


if __name__ == "__main__": 
    main()