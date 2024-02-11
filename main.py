from bs4 import BeautifulSoup
import requests
import yfinance as yf
from yahoo_fin import stock_info as si
import datetime
import re
import helper


# res = set()
# for year in range(2019, 2024):
#     filename = "sbads/" + str(year) + ".html"
#     res  = res.union(get_companies(filename))

# print(res)

companies_2019 = helper.companies_2019
companies_2020 = helper.companies_2020
companies_2021 = helper.companies_2021
companies_2022 = helper.companies_2022
companies_2023 = helper.companies_2023

ticker_map = helper.ticker_map

companies_2024 = set(helper.companies_2024.keys())
companies_2024_map = helper.companies_2024

tickers_with_previous_years = set()
for companies in companies_2024:
    if companies_2024_map[companies] in set(ticker_map.values()):
        tickers_with_previous_years.add(companies_2024_map[companies])

print(tickers_with_previous_years)


