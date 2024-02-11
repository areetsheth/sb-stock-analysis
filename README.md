# sb-stock-analysis
Analyzing / modeling historical data of the effect of companies' SuperBowl commercials on their respective stock prices. 

## Getting Started

To run this project, you will need to have Python 3 installed on your system. You can download Python 3 from the official website: [Python.org](https://www.python.org/downloads/).

After installing Python 3, make sure to download all the project dependencies listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage

You can obtain results by runing 'main.py'. Calculations are done in 'helper.py'. Feel free to tinker with both files. 

- 'main.py': executes analysis
- 'helper.py': Contains calculations and helper functions used in analysis
- 'retrieve_html.py': Utilizes webscraping techniques to gather past years' SuperBowl ads.
- 'misc/company_names.py' and 'misc/tickers.py': Obtain tickers of S&P 500, NASDAQ, DJIA, and other exchanges, as well as company names.