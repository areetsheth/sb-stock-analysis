from bs4 import BeautifulSoup
import requests
import yfinance as yf
from yahoo_fin import stock_info as si
import datetime
import re
def get_companies(filename):
    companies = set()
    with open(filename, "r", encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    info_divs = soup.find_all('div', class_='info')
    for info_div in info_divs:
        a_tag = info_div.find('a')
        if a_tag:
            if ':' in a_tag.text and '\"' not in a_tag.tsext:
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
    'Paramount+': 'VIAC',
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
    'Paramount+': 'VIAC',
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
    'Popeyes': 'PLKI',
    'Dunkin': 'DNKN'
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
