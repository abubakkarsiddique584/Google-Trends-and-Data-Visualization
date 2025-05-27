# Create a Python script that contains all the data analysis and visualization code

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load Tesla data
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
print("TESLA Dataset")
print(df_tesla.shape)
print(df_tesla.columns)
print(f"Missing values for Tesla?: {df_tesla['TSLA_WEB_SEARCH'].isnull().sum()}")
df_tesla.dropna(inplace=True)

# Convert MONTH to datetime
df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])
print(f"Largest value in Tesla search data: {df_tesla['TSLA_WEB_SEARCH'].max()}")
print(f"Smallest value in Tesla search data: {df_tesla['TSLA_WEB_SEARCH'].min()}")
print(df_tesla.head())
print("\\nTesla Web Search Statistics:")
print(df_tesla['TSLA_WEB_SEARCH'].describe())
print("Tesla date range:")
print(df_tesla['MONTH'].min(), "to", df_tesla['MONTH'].max())
print("Number of entries:", len(df_tesla))


# Load BTC Search data
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
print("\\nBTC Search Dataset")
print(df_btc_search.shape)
print(df_btc_search.columns)
print(f"Missing values for BTC Search?: {df_btc_search['BTC_NEWS_SEARCH'].isnull().sum()}")
df_btc_search.dropna(inplace=True)

# Convert MONTH to datetime
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])
print(f"Largest value in BTC search data: {df_btc_search['BTC_NEWS_SEARCH'].max()}")
print(f"Smallest value in BTC search data: {df_btc_search['BTC_NEWS_SEARCH'].min()}")
print("\\nBTC Search Statistics:")
print(df_btc_search['BTC_NEWS_SEARCH'].describe())
print("BTC date range:")
print(df_btc_search['MONTH'].min(), "to", df_btc_search['MONTH'].max())
print("Number of entries:", len(df_btc_search))


# Load Bitcoin price data
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
print("\\nBTC Price Dataset")
print(df_btc_price.shape)
print(df_btc_price.columns)
print(f"Missing values for BTC Price?: {df_btc_price.isnull().sum().sum()}")
df_btc_price.dropna(inplace=True)

# Convert DATE to datetime
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
print("\\nBTC Price Statistics:")
print(df_btc_price['CLOSE'].describe())
print("BTC Price date range:")
print(df_btc_price['DATE'].min(), "to", df_btc_price['DATE'].max())
print("Number of entries:", len(df_btc_price))


# Load Unemployment data
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
print("\\nUnemployment Dataset")
print(df_unemployment.shape)
print(df_unemployment.columns)
print(f"Missing values for U/E?: {df_unemployment.isnull().sum().sum()}")
df_unemployment.dropna(inplace=True)

# Convert MONTH to datetime
df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])
print("\\nU/E Statistics:")
print(df_unemployment['UE_BENEFITS_WEB_SEARCH'].describe())
print("U/E date range:")
print(df_unemployment['MONTH'].min(), "to", df_unemployment['MONTH'].max())
print("Number of entries:", len(df_unemployment))

# =================================================================
# TESLA VISUALIZATION 1
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt

# Load Tesla data
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])  # Convert to datetime
df_tesla.dropna(inplace=True)

# --- Plot Tesla stock price vs search volume ---
plt.figure(figsize=(14, 6))

# Create twin axes
ax1 = plt.gca()
ax2 = ax1.twinx()

# Plot stock price on primary y-axis
ax1.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color='red', label='TSLA Stock Price')
ax1.set_ylabel('TSLA Stock Price', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Plot search trend on secondary y-axis
ax2.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], color='blue', label='Search Trend')
ax2.set_ylabel('Search Trend', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Set x-axis label and title
plt.title('Tesla Web Search vs. Stock Price Over Time')
ax1.set_xlabel('Date')
plt.grid(True)

plt.tight_layout()
plt.show()

# =================================================================
# TESLA VISUALIZATION 2 (Enhanced)
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt

# Load Tesla data
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])
df_tesla.dropna(inplace=True)

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8), dpi=120)

# Secondary axis
ax2 = ax1.twinx()

# Line plots with increased thickness
ax1.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color='red', linewidth=3, label='TSLA Stock Price')
ax2.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], color='blue', linewidth=3, label='Search Trend')

# Labels and formatting
ax1.set_ylabel('TSLA Stock Price', color='red', fontsize=14)
ax2.set_ylabel('Search Trend', color='blue', fontsize=14)
ax1.set_xlabel('Date', fontsize=14)

# x-axis ticks rotation and size
ax1.tick_params(axis='x', labelsize=14, rotation=45)
ax1.tick_params(axis='y', labelsize=14, colors='red')
ax2.tick_params(axis='y', labelsize=14, colors='blue')

# Title
plt.title('Tesla Web Search vs Price', fontsize=16)

# Set axis limits (adjust as needed)
ax1.set_ylim([df_tesla['TSLA_USD_CLOSE'].min() * 0.95, df_tesla['TSLA_USD_CLOSE'].max() * 1.05])
ax2.set_ylim([df_tesla['TSLA_WEB_SEARCH'].min() * 0.95, df_tesla['TSLA_WEB_SEARCH'].max() * 1.05])
ax1.set_xlim([df_tesla['MONTH'].min(), df_tesla['MONTH'].max()])

# Grid
ax1.grid(True)

# Show plot
plt.tight_layout()
plt.show()

# =================================================================
# TESLA VISUALIZATION 3 (With Date Formatting)
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load Tesla data
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])
df_tesla.dropna(inplace=True)

# Plotting Tesla Search vs Price
plt.figure(figsize=(14, 8), dpi=120)

ax1 = plt.gca()  # Get current axis
ax2 = ax1.twinx()  # Create secondary axis for stock price

# Plot search trend
ax1.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], color='red', label='Search Trend', linewidth=3)
ax1.set_ylabel('Search Trend', color='red', fontsize=14)
ax1.tick_params(axis='y', labelcolor='red', labelsize=12)

# Plot stock price
ax2.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color='blue', label='TSLA Stock Price', linewidth=3)
ax2.set_ylabel('TSLA Stock Price', color='blue', fontsize=14)
ax2.tick_params(axis='y', labelcolor='blue', labelsize=12)

# Title and layout
plt.title('Tesla Web Search vs Price', fontsize=16)

# Format x-axis with readable dates
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Tick every 3 months
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Format: Jan 2020
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=14)

# Set x and y limits (optional)
ax1.set_ylim([0, df_tesla['TSLA_WEB_SEARCH'].max() + 10])
ax2.set_ylim([0, df_tesla['TSLA_USD_CLOSE'].max() + 100])
ax1.set_xlim([df_tesla['MONTH'].min(), df_tesla['MONTH'].max()])

# Layout to avoid label cutoff
plt.tight_layout()

# Show plot
plt.show()

# =================================================================
# BITCOIN VISUALIZATION
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load search data
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])
df_btc_search.dropna(inplace=True)

# Load daily BTC price data
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
df_btc_price.dropna(inplace=True)

# Convert daily BTC price data to monthly average (Month Start to match search trend)
df_btc_price.set_index('DATE', inplace=True)
df_btc_price_monthly = df_btc_price.resample('MS').mean().reset_index()

# Merge BTC search with monthly price
df_merged = pd.merge(df_btc_search, df_btc_price_monthly,
                     left_on='MONTH', right_on='DATE')

# Drop NaNs just in case
df_merged = df_merged.dropna()

# Plotting
plt.figure(figsize=(14, 8), dpi=120)

# Primary y-axis: Search trend
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(df_merged['MONTH'], df_merged['BTC_NEWS_SEARCH'],
         color='red', marker='o', linewidth=2.5, label='Search Trend')
ax1.set_ylabel('Search Trend', color='red', fontsize=14)
ax1.tick_params(axis='y', labelcolor='red', labelsize=12)

# Secondary y-axis: BTC price
ax2.plot(df_merged['MONTH'], df_merged['CLOSE'],
         color='blue', linestyle='--', linewidth=3, label='BTC Price')
ax2.set_ylabel('BTC Price', color='blue', fontsize=14)
ax2.tick_params(axis='y', labelcolor='blue', labelsize=12)

# Title and axis formatting
plt.title('Bitcoin News Search vs Resampled Price', fontsize=16)
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=14)

# Set axis limits for better appearance
ax1.set_ylim([0, df_merged['BTC_NEWS_SEARCH'].max() + 10])
ax2.set_ylim([0, df_merged['CLOSE'].max() + 500])
ax1.set_xlim([df_merged['MONTH'].min(), df_merged['MONTH'].max()])

# Show plot
plt.tight_layout()
plt.show()

# =================================================================
# UNEMPLOYMENT VISUALIZATION 1
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the data
un_benefits_df = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
un_benefits_df['MONTH'] = pd.to_datetime(un_benefits_df['MONTH'])
un_benefits_df.dropna(inplace=True)

# Set up the figure and axes
plt.figure(figsize=(14, 8), dpi=120)
ax1 = plt.gca()
ax2 = ax1.twinx()

# Plot search interest
ax1.plot(un_benefits_df['MONTH'], un_benefits_df['UE_BENEFITS_WEB_SEARCH'],
         color='purple', linewidth=3, label='Search Trend')
ax1.set_ylabel('Search Interest', color='purple', fontsize=14)
ax1.tick_params(axis='y', labelcolor='purple', labelsize=12)

# Plot unemployment rate
ax2.plot(un_benefits_df['MONTH'], un_benefits_df['UNRATE'],
         color='black', linewidth=3, linestyle='--', label='U/E Rate')
ax2.set_ylabel('FRED U/E Rate', color='black', fontsize=14)
ax2.tick_params(axis='y', labelcolor='black', labelsize=12)

# Add title
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=16)

# Format x-axis with dates
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=14)

# Add grid to help with readability
ax1.grid(color='gray', linestyle='--', linewidth=0.5)

# Set axis limits
ax1.set_ylim([0, un_benefits_df['UE_BENEFITS_WEB_SEARCH'].max() + 10])
ax2.set_ylim([0, un_benefits_df['UNRATE'].max() + 2])
ax1.set_xlim([un_benefits_df['MONTH'].min(), un_benefits_df['MONTH'].max()])

# Show the plot
plt.tight_layout()
plt.show()

# =================================================================
# UNEMPLOYMENT VISUALIZATION 2 (With Rolling Average)
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load and clean the data
un_benefits_df = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
un_benefits_df['MONTH'] = pd.to_datetime(un_benefits_df['MONTH'])
un_benefits_df.dropna(inplace=True)

# Calculate 6-month rolling average
un_benefits_df['6MA_SEARCH'] = un_benefits_df['UE_BENEFITS_WEB_SEARCH'].rolling(window=6).mean()

# Plotting
plt.figure(figsize=(14, 8), dpi=120)
ax1 = plt.gca()
ax2 = ax1.twinx()

# Plot 6-month rolling average of search interest
ax1.plot(un_benefits_df['MONTH'], un_benefits_df['6MA_SEARCH'],
         color='blue', linewidth=3, label='6-Month Avg Search')

# Plot actual unemployment rate
ax2.plot(un_benefits_df['MONTH'], un_benefits_df['UNRATE'],
         color='black', linewidth=3, linestyle='--', label='U/E Rate')

# Labels and title
ax1.set_ylabel('6-Month Avg Search', color='blue', fontsize=14)
ax2.set_ylabel('FRED U/E Rate', color='black', fontsize=14)
plt.title('6-Month Rolling Avg of "Unemployment Benefits" Search vs U/E Rate', fontsize=16)

# Formatting the x-axis
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=12)

# Grid and limits
ax1.grid(color='gray', linestyle='--', linewidth=0.5)
ax1.set_ylim([0, un_benefits_df['6MA_SEARCH'].max() + 5])
ax2.set_ylim([0, un_benefits_df['UNRATE'].max() + 2])
ax1.set_xlim([un_benefits_df['MONTH'].min(), un_benefits_df['MONTH'].max()])

plt.tight_layout()
plt.show()

# =================================================================
# UNEMPLOYMENT VISUALIZATION 3 (Extended Dataset)
# =================================================================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load and clean the data
un_benefits_df = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
un_benefits_df['MONTH'] = pd.to_datetime(un_benefits_df['MONTH'])
un_benefits_df.dropna(inplace=True)

plt.figure(figsize=(14, 8), dpi=120)
ax1 = plt.gca()
ax2 = ax1.twinx()


# Plot search interest
ax1.plot(un_benefits_df['MONTH'], un_benefits_df['UE_BENEFITS_WEB_SEARCH'],
         color='purple', linewidth=3, label='Search Trend')
ax1.set_ylabel('Search Interest', color='purple', fontsize=14)
ax1.tick_params(axis='y', labelcolor='purple', labelsize=12)

# Plot unemployment rate
ax2.plot(un_benefits_df['MONTH'], un_benefits_df['UNRATE'],
         color='black', linewidth=3, linestyle='--', label='U/E Rate')
ax2.set_ylabel('FRED U/E Rate', color='black', fontsize=14)
ax2.tick_params(axis='y', labelcolor='black', labelsize=12)

# Add title
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=16)

# Format x-axis with dates
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=14)

# Add grid to help with readability
ax1.grid(color='gray', linestyle='--', linewidth=0.5)

# Set axis limits
ax1.set_ylim([0, un_benefits_df['UE_BENEFITS_WEB_SEARCH'].max() + 10])
ax2.set_ylim([0, un_benefits_df['UNRATE'].max() + 2])
ax1.set_xlim([un_benefits_df['MONTH'].min(), un_benefits_df['MONTH'].max()])

# Show the plot
plt.tight_layout()
plt.show()


