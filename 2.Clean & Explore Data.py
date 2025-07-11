
import pandas as pd

# Load the CSV
df = pd.read_csv("ipl_2023.csv")
# Check for missing values
print("\n🔍 Missing values:")
print(df.isnull().sum())

print('----------------------')

# Check for duplicate rows
print("\n📑 Duplicates:")
print(df.duplicated().sum())

print('----------------------')

# Describe numeric columns (runs, balls, etc.)
print("\n📈 Numeric summary:")
print(df.describe())
print('----------------------')

# List of unique teams
print("\n🏏 Unique Batting Teams:")
print(df['BattingTeam'].unique())

print('----------------------')

# List of players
print("\n👤 Sample Batters:")
print(df['batter'].unique()[:10])

print('----------------------')

# List of types of dismissals
print("\n🚫 Wicket Types:")
print(df['kind'].unique())

