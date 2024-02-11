import helper
import pandas as pd

def main():
    df = helper.df
    print(df.sort_values(by='Average Price Increase', ascending=False))
    print(df.sort_values(by='SB Commercials Since 2019', ascending=False))

main()