import yfinance as yf
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

# Define your tickers
companies = [
    'SQ', 'SPGI', 'SYK', 'PFE', 'BMY',
    'ABT', 'MDT', 'TXN', 'BAX', 'ISRG', 'ROST', 'AMGN', 'COST', 'TRV', 'WMT', 'WBA', 'CSX', 'SCHW', 'NEM', 'CHTR', 'ZTS', 'EXC', 'VLO', 'FIS', 'AIG',
    'ANTM', 'COP', 'MCK', 'MRNA', 'BIDU', 'MO', 'DISCK', 'SYY', 'HCA', 'OXY', 'EQIX', 'FISV', 'PGR', 'ICE', 'ADP', 'PXD', 'ALNY', 'AON', 'EOG', 'AME',
    'STZ', 'TROW', 'ALL', 'VFC', 'KHC', 'O', 'SPG', 'DE', 'PRU', 'ABMD', 'MSCI', 'CHD', 'WDC', 'NXPI', 'RMD', 'EQH', 'PPL', 'XEL', 'ES', 'MAR', 'TAP',
    'CL', 'CTSH', 'NUE', 'PKI', 'KMB', 'BKR', 'COF', 'DHR', 'WELL', 'DD', 'FMC', 'AEP', 'AVGO', 'IP', 'ITW', 'ADSK', 'STT', 'MKC', 'EXPE', 'SHW', 'TRIP',
    'UAL', 'JCI', 'CLX', 'WEC', 'IRM', 'GILD', 'ALB', 'LUV', 'F', 'GPC', 'PSA', 'DLR', 'NSC', 'KLAC', 'LNC', 'EQR', 'SO', 'TSCO', 'NCLH', 'HUM', 'K',
    'CNC', 'APD', 'ROK', 'PH', 'ZBRA', 'NTRS', 'ED', 'FE', 'OKE', 'MTB', 'WMB', 'ETR', 'CMS', 'PCG', 'NI', 'AEE', 'PNW', 'AES', 'NRG', 'DTE', 'AEP',
    'AWK', 'LNT', 'ATO', 'SRE', 'PEG', 'XEL', 'ES', 'NEE', 'D', 'DUK', 'EXC', 'EIX', 'CEG', 'ED', 'VST', 'HIG', 'GL', 'UNM', 'CINF', 'LNC', 'PFG',
    'RJF', 'AMP', 'IVZ', 'CFG', 'FITB', 'RF', 'HBAN', 'KEY', 'ZION', 'ALLY', 'MTG', 'PBCT', 'FHN', 'TFSL', 'CMA', 'SNV', 'CFR', 'PNFP', 'WTFC',
    'BOKF', 'CUBI', 'CASH', 'NYCB', 'TFC', 'USB', 'BK', 'NTR', 'CF', 'MOS', 'IPI', 'CCJ', 'NUE', 'STLD', 'X', 'RS', 'CMC', 'TX', 'ATI', 'CLF',
    'AA', 'SCCO', 'FCX', 'HL', 'PAAS', 'AG', 'EXK', 'AUY', 'WPM', 'RGLD', 'FNV', 'GOLD', 'NEM', 'BTG', 'SSRM', 'SA', 'NG', 'KGC', 'AU', 'YRI.TO',
    'WCN', 'WM', 'RSG', 'CLH', 'ECOL', 'CWST', 'SRCL', 'HCCI', 'TTEK', 'PWR', 'EME', 'FLR', 'DY', 'FIX', 'MDR', 'ACM', 'J', 'MTZ', 'KBR', 'TPC', 'GBX',
    'TRN', 'WAB', 'GNRC', 'CMI', 'PCAR', 'NAV', 'FSS', 'AGCO', 'DE', 'CAT', 'TEX', 'OSK', 'CNHI', 'LECO', 'PNR', 'IEX', 'XYL', 'FELE', 'AWI', 'TREX',
    'BLDR', 'MAS', 'FBHS', 'JELD', 'DOOR', 'LPX', 'LL', 'HD', 'LOW', 'TSCO', 'BBY', 'BBWI', 'DG', 'DLTR', 'ROST', 'TJX', 'BURL', 'KSS', 'JWN', 'M',
    'DDS', 'GPS', 'ANF', 'URBN', 'AEO', 'RL', 'PVH', 'VFC', 'LEVI', 'UAA', 'COLM', 'DECK', 'SHOO', 'SKX', 'CROX', 'FL', 'FINL', 'DKS', 'HIBB', 'YETI',
    'NKE', 'ADDYY', 'PUMA', 'LULU', 'ASO', 'GOOS', 'GIII', 'CRON', 'CGC', 'ACB', 'TLRY', 'SNDL', 'VFF', 'HEXO', 'OGI', 'APHA', 'GRWG', 'IIPR', 'TCNNF',
    'CURLF', 'GTBIF', 'TRSSF', 'CCHWF', 'AYRWF', 'CLVR', 'INCR', 'PRPL', 'TPX', 'SNBR', 'ZZZ.TO', 'LEG', 'LZB', 'HVT', 'ETH', 'WSM', 'RH', 'LOVE', 'PRGO'
]


start_date = '2023-01-01'
end_date = '2025-01-01'

# Create output directory
output_dir = 'financial_charts-dataset'
os.makedirs(output_dir, exist_ok=True)


def generate_charts(company, start_date, end_date):
    # Download stock data
    stock_data = yf.download(company, start=start_date, end=end_date, auto_adjust=False)

    if len(stock_data) < 100:
        print(f"Warning: Not enough data for {company}. Only {len(stock_data)} rows found.")
        return
    # Debug print
    #print(f"\nDebug info for {company}:")
    #print(f"Type of stock_data: {type(stock_data)}")
    #print(f"Columns: {stock_data.columns}")


    if isinstance(stock_data.columns, pd.MultiIndex):
        # Flatten the MultiIndex columns
        stock_data.columns = ['_'.join(col).strip() for col in stock_data.columns.values]
        print(f"\nFlattened columns: {stock_data.columns}")


    close_col = [col for col in stock_data.columns if 'Close' in col][0]
    volume_col = [col for col in stock_data.columns if 'Volume' in col][0]

    # Converting  to numeric
    stock_data[close_col] = pd.to_numeric(stock_data[close_col], errors='coerce')
    stock_data[volume_col] = pd.to_numeric(stock_data[volume_col], errors='coerce')

    # Dropping NA values
    stock_data = stock_data.dropna(subset=[close_col, volume_col])

    # Chart file names
    stock_price_chart = f'{output_dir}/{company}_stock_price.png'
    volume_bar_chart = f'{output_dir}/{company}_volume_bar.png'
    volume_pie_chart = f'{output_dir}/{company}_volume_pie.png'

    # Plotting stock price chart
    plt.figure(figsize=(10, 6))
    stock_data[close_col].plot(title=f'{company} Stock Price')
    plt.savefig(stock_price_chart)
    plt.close()

    # Resample volume data
    quarterly_volume = stock_data[volume_col].resample('QE').sum()

    # Plotting volume bar chart
    plt.figure(figsize=(10, 6))
    quarterly_volume.plot(kind='bar', title=f'{company} Quarterly Volume')
    plt.xlabel("Quarter")
    plt.ylabel("Total Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(volume_bar_chart)
    plt.close()

    # Plot volume pie chart
    if not quarterly_volume.empty:
        plt.figure(figsize=(8, 8))
        plt.pie(quarterly_volume.values,
                labels=quarterly_volume.index.strftime('%Y-Q%q'),
                autopct='%1.1f%%',
                startangle=140)
        plt.title(f'{company} Quarterly Volume Distribution')
        plt.tight_layout()
        plt.savefig(volume_pie_chart)
        plt.close()

    # Generate summary
    summary = f"Summary of {company} data from {start_date} to {end_date}:\n"
    summary += f"Total Trading Days: {len(stock_data)}\n"
    summary += f"Highest Closing Price: {stock_data[close_col].max():.2f}\n"
    summary += f"Lowest Closing Price: {stock_data[close_col].min():.2f}\n"
    summary += f"Average Closing Price: {stock_data[close_col].mean():.2f}\n"
    summary += f"Total Volume: {stock_data[volume_col].sum():,.0f}\n\n"

    summary += "Quarterly Volume:\n"
    for date, volume in quarterly_volume.items():
        summary += f"{date.strftime('%Y-Q%q')}: {volume:,.0f}\n"

    # Save summary
    with open(f'{output_dir}/{company}_summary.txt', 'w') as f:
        f.write(summary)

    # Create chart with caption
    fig, ax = plt.subplots(figsize=(10, 6))
    stock_data[close_col].plot(ax=ax, title=f'{company} Stock Price')
    caption = f"Highest: {stock_data[close_col].max():.2f}, Lowest: {stock_data[close_col].min():.2f}, Avg: {stock_data[close_col].mean():.2f}"
    ax.text(0.5, -0.15, caption, ha='center', va='bottom', transform=ax.transAxes)
    plt.savefig(f'{output_dir}/{company}_stock_price_with_caption.png')
    plt.close()


# Process each company
for company in companies:
    generate_charts(company, start_date, end_date)

print("Processing complete. Charts and summaries saved.")