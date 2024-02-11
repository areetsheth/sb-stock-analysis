from bs4 import BeautifulSoup
import requests
import yfinance as yf
from yahoo_fin import stock_info as si
import datetime

resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})

sp_500_tickers = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    sp_500_tickers.append(ticker)
sp_500_tickers = [s.replace('\n', '') for s in sp_500_tickers]

dow_tickers = si.tickers_dow()
nasdaq_tickers = si.tickers_nasdaq()
other_tickers = si.tickers_other()

#convert each to set and then find the intersection
sp_500_set = set(sp_500_tickers)
dow_set = set(dow_tickers)
nasdaq_set = set(nasdaq_tickers)
other_tickers_set = set(other_tickers)

#union all the sets
#all_tickers = sp_500_set.union(dow_set, nasdaq_set, other_tickers_set)
all_tickers = sp_500_set.union(dow_set, nasdaq_set, other_tickers_set)

def write_tickers_to_file():
    with open('tickers.txt', 'w') as file:
        for ticker in all_tickers:
            file.write(ticker + '\n')

def retreive_tickers():
    return all_tickers

write_tickers_to_file()