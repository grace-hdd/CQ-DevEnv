import pandas as pd

def calculate_daily_returns(file_path):
    df = pd.read_csv(file_path)
    df['daily_return'] = df['close'].pct_change()

    # Show all rows
    pd.set_option('display.max_rows', None)

    print(df)
    return df

# Usage
file_path = "daily_bitcoin_ohlc.csv"
calculate_daily_returns(file_path)
