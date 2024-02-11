import misc.tickers as tickers
import yfinance as yf

print(yf.Ticker('EVE.U').info.keys())
def get_company_name(ticker):
    res = set()
    try:
        company = yf.Ticker(ticker)
        res.add(company.info['shortName'])
        res.add(company.info['longName'])
    except:
        #throw an error if the ticker is not found
        print(f"Ticker {ticker} not found")
    return res

#parse tickers.txt to a tickers list:
with open('tickers.txt', 'r') as file:
    tickers = file.read().splitlines()

def get_company_names():
    company_names = {}
    for ticker in tickers:
        names = get_company_name(ticker)
        if names:
            company_names[ticker] = names
    return company_names

def write_company_names_to_file():
    company_names = get_company_names()
    with open('company_names.txt', 'w') as file:
        for ticker, names in company_names.items():
            file.write(ticker + ': ' + ', '.join(names) + '\n')

write_company_names_to_file()