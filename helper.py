from bs4 import BeautifulSoup
import requests
import yfinance as yf
from yahoo_fin import stock_info as si
import datetime
import re
import pandas as pd

def get_companies(filename):
    companies = set()
    with open(filename, "r", encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    info_divs = soup.find_all('div', class_='info')
    for info_div in info_divs:
        a_tag = info_div.find('a')
        if a_tag:
            if ':' in a_tag.text and '\"' not in a_tag.text:
                companies.add(a_tag.text.strip().split(':')[0])
            else:
                companies.add(a_tag.text.strip().split(' \"')[0].strip())

    return companies

companies_2019 = get_companies("sbads/2019.html")
companies_2020 = get_companies("sbads/2020.html")
companies_2021 = get_companies("sbads/2021.html")
companies_2022 = get_companies("sbads/2022.html")
companies_2023 = get_companies("sbads/2023.html")

ticker_map = {
    'WeatherTech': 'Unknown',
    'State Farm': 'Unknown',
    'Sabra': 'Unknown',
    'Olay': 'PG',
    "Lay's": 'PEP',
    'Hulu': 'DIS',
    'Stella Artois': 'BUD',
    'Google': 'GOOGL',
    'Hologic': 'HOLX',
    'Bud Light': 'BUD',
    'Robinhood': 'HOOD',
    'Crown Royal': 'Unknown',
    'Michael Bloomberg': 'Unknown',
    'Disney Plus': 'DIS',
    'Microsoft': 'MSFT',
    'Dr. Squatch': 'Unknown',
    'TurboTax': 'Unknown',
    'Crypto.com': 'Unknown',
    'Heinz': 'KHC',
    'Planters': 'HRL',
    'Skechers': 'SKX',
    'Cheetos': 'PEP',
    'BMW': 'BMWYY',
    'Toyota Supra': 'TM',
    'Rémy Martin': 'Unknown',
    'Polestar': 'Unknown',
    'Kia': 'KIMTF',
    'Turkish Airlines': 'TKHLY',
    'T-Mobile': 'TMUS',
    'Budweiser': 'BUD',
    'Carvana': 'CVNA',
    'Rakuten': 'RKUNY',
    'M&M’s': 'MNBP',
    'Klarna': 'Unknown',
    'Michelob Ultra': 'BUD',
    'Mtn Dew': 'PEP',
    'Microsoft': 'MSFT',
    'Colgate': 'CL',
    'DraftKings': 'DKNG',
    'Uber': 'UBER',
    'Quicken Loans': 'RKT',
    'Hyundai': 'HYMTF',
    'Bass Pro Shops and Cabela’s': 'Unknown',
    'Logitech': 'LOGI',
    'Oatly': 'OTLY',
    'Mercedes-Benz': 'DDAIF',
    'Vroom': 'VRM',
    'Microban 24': 'Unknown',
    'ADT': 'ADT',
    'The Farmer’s Dog': 'Unknown',
    'Dunkin': 'DNKN',
    'Intuit QuickBooks and Mailchimp': 'INTU',
    'Scotts Miracle-Gro': 'SMG',
    'DoorDash': 'DASH',
    'Gillette': 'Unknown',
    'Coinbase': 'COIN',
    'Coke Energy': 'KO',
    'Dexcom': 'DXCM',
    'Planet Fitness': 'PLNT',
    'Amazon': 'AMZN',
    'Paramount+': 'PARA',
    'Sketchers': 'SKX',
    'Taco Bell': 'YUM',
    'Meta': 'META',
    'Sodastream': 'SODA',
    'TurboTax': 'Unknown',
    'Greenlight': 'Unknown',
    'Cutwater Spirits': 'Unknown',
    'Hard Rock': 'Unknown',
    'CrowdStrike': 'CRWD',
    'Wix': 'WIX',
    'Mint Mobile': 'Unknown',
    'Cadillac': 'GM',
    'Verizon': 'VZ',
    'FanDuel': 'Unknown',
    'Guaranteed Rate': 'Unknown',
    'Molson Coors': 'TAP',
    'Booking.com': 'BKNG',
    'Shift4 Payments': 'FOUR',
    'Wallbox': 'Unknown',
    'Expensify': 'Unknown',
    'Huggies': 'KMB',
    'Porsche': 'POAHY',
    'Intuit, TurboTax': 'INTU',
    'Quibi': 'Unknown',
    'Pepsi': 'PEP',
    'Workday': 'WDAY',
    'Toyota': 'TM',
    'Walmart': 'WMT',
    'Persil ProClean': 'HENKY',
    'Anheuser-Busch InBev': 'BUD',
    'Devour': 'Unknown',
    'Discover': 'DFS',
    'Rocket Mortgage': 'RKT',
    'Amazon Alexa': 'AMZN',
    'Norwegian cruise line': 'NCLH',
    'New York Life': 'Unknown',
    'Mercari': 'MRCR',
    'eToro': 'Unknown',
    'Pringles': 'K',
    'Heineken': 'HEINY',
    'Amazon Studios': 'AMZN',
    'Netflix': 'NFLX',
    'SimpliSafe': 'Unknown',
    'Snickers': 'HSY',
    'General Motors': 'GM',
    'Jimmy John’s': 'Unknown',
    'Fiverr': 'FVRR',
    'Amazon Prime Video': 'AMZN',
    'E-Trade': 'Unknown',
    'Expedia': 'EXPE',
    'Downy': 'PG',
    "Reese's Take 5": 'HSY',
    'Facebook "Facebook Groups': 'FB',
    'Google Pixel 6': 'GOOGL',
    'Salesforce': 'CRM',
    'Nissan': 'NSANY',
    'Avocados From Mexico': 'CVGW',
    'Audi': 'AUDVF',
    'Limit Break': 'Unknown',
    'Bumble': 'BMBL',
    'Ram Trucks': 'FCAU.VI',
    'Disney': 'DIS',
    'PopCorners': 'PIP',
    "Sam's Club": 'WMT',
    'Pop-Tarts': 'K',
    'Busch Light': 'BUD',
    'Hummer': 'GM',
    'Chevrolet': 'GM',
    'Sprint': 'TMUS',
    'Hellmann’s': 'UL',
    'Jeep': 'FCAU.VI',
    'Astellas': 'Unknown',
    'Doritos': 'PEP',
    'Tide': 'PG',
    'Cue Health': 'Unknown',
    'Indeed': 'RCRRF',
    'Caesars Sportsbook': 'CZR',
    'Cheetos and Doritos': 'PEP',
    'Chipotle': 'CMG',
    'Burger King': 'QSR',
    'Irish Spring': 'CPB',
    'Squarespace': 'SQSP',
    'Washington Post': 'Unknown',
    'Peacock': 'CMCSA',
    'Hyundai Genesis': 'HYMTF',
    'Bon & Viv Spiked Seltzer': 'BUD',
    'Little Caesars': 'Unknown',
    'Temu': 'Unknown',
    'Bubly': 'PEP',
    'Google Translate': 'GOOGL',
    'NFL': 'Unknown',
    'Uber Eats': 'UBER',
    'Michelob Ultra Pure Gold': 'BUD',
    'M&M’ s': 'MNBP',
    'M&M\'s': 'MNBP',
    'Bud Light/Game of Thrones': 'BUD',
}

companies_2024 = {
    'Paramount+': 'PARA',
    'Google': 'GOOGL',
    'M&M’s': 'MNBP',
    'OREO': 'MDLZ',
    'Booking.com': 'BKNG',
    'Doritos': 'PEP',
    'Mountain Dew': 'PEP',
    'Starry': 'PEP',
    'Pringles': 'K',
    'Dove': 'UL',
    'Budweiser': 'BUD',
    'Bud Light': 'BUD',
    'T-Mobile': 'TMUS',
    'Michelob Ultra': 'BUD',
    'Hellmann’s': 'UL',
    'Kawasaki': 'KWHIY',
    'Uber Eats': 'UBER',
    'DoorDash': 'DASH',
    'Popeyes': 'PLKI'
}

def generate_year_map():
    companies_2019_map = {}
    for company in companies_2019:
        if company in ticker_map:
            companies_2019_map[company] = ticker_map[company]
        
    companies_2020_map = {}
    for company in companies_2020:
        if company in ticker_map:
            companies_2020_map[company] = ticker_map[company]

    companies_2021_map = {}
    for company in companies_2021:
        if company in ticker_map:
            companies_2021_map[company] = ticker_map[company]

    companies_2022_map = {}
    for company in companies_2022:
        if company in ticker_map:
            companies_2022_map[company] = ticker_map[company]

    companies_2023_map = {}
    for company in companies_2023:
        if company in ticker_map:
            companies_2023_map[company] = ticker_map[company]
    return companies_2019_map, companies_2020_map, companies_2021_map, companies_2022_map, companies_2023_map

company_2019_map, company_2020_map, company_2021_map, company_2022_map, company_2023_map = generate_year_map()

superbowl_dates = {
    '2019': datetime.datetime(2019, 2, 3),
    '2020': datetime.datetime(2020, 2, 2),
    '2021': datetime.datetime(2021, 2, 7),
    '2022': datetime.datetime(2022, 2, 13),
    '2023': datetime.datetime(2023, 2, 12),
    '2024': datetime.datetime(2024, 2, 11)
}

following_monday_dates = {
    '2019': datetime.datetime(2019, 2, 4),
    '2020': datetime.datetime(2020, 2, 3),
    '2021': datetime.datetime(2021, 2, 8),
    '2022': datetime.datetime(2022, 2, 14),
    '2023': datetime.datetime(2023, 2, 13),
    '2024': datetime.datetime(2024, 2, 12)

}

previous_friday_dates = {
    '2019': datetime.datetime(2019, 2, 1),
    '2020': datetime.datetime(2020, 1, 31),
    '2021': datetime.datetime(2021, 2, 5),
    '2022': datetime.datetime(2022, 2, 11),
    '2023': datetime.datetime(2023, 2, 10),
    '2024': datetime.datetime(2024, 2, 9)
}

company_to_year_count = {}
new_companies = set()
for company in companies_2024:
    ticker = companies_2024[company]
    if ticker in set(ticker_map.values()):
        if ticker not in company_to_year_count:
            company_to_year_count[ticker] = set()
        if ticker in set(company_2019_map.values()):
            company_to_year_count[ticker].add(2019)
        if ticker in set(company_2020_map.values()):
            company_to_year_count[ticker].add(2020)
        if ticker in set(company_2021_map.values()):
            company_to_year_count[ticker].add(2021)
        if ticker in set(company_2022_map.values()):
            company_to_year_count[ticker].add(2022)
        if ticker in set(company_2023_map.values()):
            company_to_year_count[ticker].add(2023)
    else:
        new_companies.add(company)

ticker_to_price_increase = {}
for ticker in company_to_year_count:
    if ticker not in ticker_to_price_increase:
        ticker_to_price_increase[ticker] = []
    for year in company_to_year_count[ticker]:
        start_date = previous_friday_dates[str(year)]
        one_day_after_start = start_date + datetime.timedelta(days=1)
        end_date = following_monday_dates[str(year)]
        one_day_after_end = end_date + datetime.timedelta(days=1)

        close_price = yf.Ticker(ticker).history(start=start_date, end=one_day_after_start)['Close'].iloc[0]
        max_price = yf.Ticker(ticker).history(start=end_date, end=one_day_after_end)['Open'].iloc[0]

        price_increase = (max_price - close_price) / close_price
        ticker_to_price_increase[ticker].append(price_increase)


ticker_to_avg_price_increase = {}
for ticker in ticker_to_price_increase:
    ticker_to_avg_price_increase[ticker] = 100*(sum(ticker_to_price_increase[ticker]) / len(ticker_to_price_increase[ticker]))

#sort the dictionary by descending order
ticker_to_avg_price_increase = dict(sorted(ticker_to_avg_price_increase.items(), key=lambda item: item[1], reverse=True))

data = []

for ticker in ticker_to_avg_price_increase:
    data.append({
        'Ticker': ticker,
        'Average Price Increase': ticker_to_avg_price_increase[ticker],
        'SB Commercials Since 2019': len(company_to_year_count[ticker])
    })

df = pd.DataFrame(data)

actual_ticker_to_price_increase = {}
for ticker in company_to_year_count:
    if ticker == 'MNBP':
        continue
    start_date = datetime.datetime(2024, 2, 9)
    one_day_after_start = start_date + datetime.timedelta(days=1)
    end_date = datetime.datetime(2024, 2, 12)
    one_day_after_end = end_date + datetime.timedelta(days=1)

    close_price = yf.Ticker(ticker).history(start=start_date, end=one_day_after_start)['Close'].iloc[0]
    open_price = yf.Ticker(ticker).history(start=end_date, end=one_day_after_end)['Open'].iloc[0]

    price_increase = 100*(open_price - close_price) / close_price
    actual_ticker_to_price_increase[ticker] = price_increase

df['Actual Price Increase'] = df['Ticker'].map(actual_ticker_to_price_increase)
print(df.sort_values(by='Actual Price Increase', ascending=False))
