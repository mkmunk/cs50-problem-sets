# Stock Fundamentals Lookup Tool
#### Video Demo: https://youtu.be/k8Hhlq8RdqM
#### Description:

Stock Fundamentals Lookup Tool is a command-line Python program that lets a user look up the key fundamental information of a publicly traded company simply by typing in its stock ticker symbol (e.g., "AAPL" for Apple Inc. or "2409.TW" for AUO Corporation on the Taiwan Stock Exchange). The goal of this project is to give someone with little or no financial background a quick, readable snapshot of a company's fundamentals, without needing to dig through a full financial report or a cluttered finance website.

When run, the program prompts the user for a stock ticker, fetches real-time data from Yahoo Finance using the `yfinance` library, and prints out a concise summary covering five categories of information:

1. Company Name and Sector — who the company is and what industry it belongs to
2. Current Price and 52-Week Range — where today's price sits relative to the past year's high and low
3. Market Cap and P/E Ratio — the company's size and how "expensive" its stock is relative to earnings
4. 5-Year Change — the stock's long-term price trend
5. EPS, Profit Margin, and Dividend Yield — how profitable the company actually is, and what it pays back to shareholders

## How to Use

Run the program from the terminal with:

```
python project.py
```

The program will prompt:

```
Stock number:
```

Type in any valid ticker symbol, such as `AAPL`, `NVDA`, `MSFT`, or a Taiwan-listed stock like `2409.TW`, and press Enter. The program will then print a formatted summary of that stock's fundamentals. If an invalid or non-existent ticker is entered, the program exits gracefully with an error message instead of crashing.

## File Structure and What Each File Does

### `project.py`

This file contains the `main` function along with three required custom functions:

- **`get_stock_data(ticker)`**: Takes a stock ticker as input and uses the `yfinance` library to fetch two things: the company's fundamental info (as a dictionary) and its daily historical price data going back 5 years from today (open, high, low, close, volume). It returns both as a tuple. Any rows with missing values in the historical data are dropped using `.dropna()`, to ensure the closing prices used later in calculations are always valid.

- **`calculate_five_year_change(history)`**: Takes the historical price data and calculates the percentage change between the earliest and the most recent closing price over the past 5 years, returning it as a formatted string (e.g., `"109.36%"`).

- **`display_stock_info(info, five_year_change)`**: Takes the fundamental data dictionary and the calculated 5-year change, and formats them into a single readable multi-line string covering company name, sector, current price, 52-week range, market cap, P/E ratio, 5-year change, EPS, profit margin, and dividend yield. This function returns the formatted string rather than printing it directly, so that it can be tested independently with `pytest`.

The `main()` function ties these three functions together: it prompts the user for a ticker, calls `get_stock_data()`, passes the resulting history into `calculate_five_year_change()`, passes both the info and the calculated change into `display_stock_info()`, and finally prints the result. If the ticker is invalid, an `IndexError` is raised when the historical data turns out to be empty, and `main()` catches this exception and exits the program with a clear error message instead of showing a traceback.

### `test_project.py`

This file contains three test functions, one for each custom function in `project.py`:

- **`test_get_stock_data()`**: Calls the function with four different real, well-known ticker symbols (`AAPL`, `NVDA`, `MSFT`, `GOOGL`) and asserts that the `symbol` field in the returned info dictionary matches the ticker that was requested, confirming that the function retrieves data for the correct company.

- **`test_calculate_five_year_change()`**: Uses fabricated `Close` price data (not real market data) to verify the percentage calculation is correct in three scenarios: a 50% gain (100 → 150), a 50% loss (50 → 25), and an 80% loss (100 → 20). Each case checks that the function correctly applies the formula `(last - first) / first * 100` and formats the result to two decimal places with a percent sign.

- **`test_display_stock_info()`**: Uses a fabricated `info` dictionary along with a fixed 5-year change string (`"100%"`) to call the function, then checks that every expected value (company name, sector, price, market cap, etc.) appears somewhere in the returned string, confirming that all fields are correctly incorporated into the final formatted output.

### `requirements.txt`

Lists the external libraries this project depends on: `yfinance`, `pandas`, and `pytest`.

## Design Choices

**Why these particular fundamentals?** These five categories were chosen because they each answer a different question an investor typically asks when first looking at an unfamiliar stock: Company Name/Sector establishes context (who is this company, what do they do); Current Price/52-Week Range shows where today's price sits relative to its recent range; Market Cap indicates company size; P/E Ratio is a quick valuation gauge (is the stock expensive relative to earnings); 5-Year Change reveals long-term growth trend; and EPS, Profit Margin, and Dividend Yield together describe how profitable the company actually is and what it returns to shareholders. The overall structure moves from "who is this company" to "is the price reasonable" to "is the company actually profitable" to "is it worth holding long-term" — essentially a simplified fundamental health check for a stock.

**Why call `.dropna()` on the historical data?** Yahoo Finance sometimes returns an incomplete row for the current trading day if the market is still open or data hasn't fully settled yet, resulting in `NaN` (missing) values for that day's open/high/low/close. Without removing these rows, `calculate_five_year_change()` could end up computing with a missing value, producing a `"nan%"` result instead of a real number. Calling `.dropna()` immediately after fetching the data ensures that all downstream calculations are only ever performed on complete, valid rows.

**Why does `display_stock_info()` return a string instead of printing directly?** Keeping `print()` calls confined to `main()` makes the other functions easier to test with `pytest`, since a returned string can be checked with `assert`, whereas printed output cannot be captured and verified as easily.

## AI Assistance

This project was developed with assistance from Claude (Anthropic), an AI assistant, which helped with debugging, code review, and polishing this README's writing. The core logic, design decisions, and implementation are my own.