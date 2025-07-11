import pandas as pd

# Load the CSV
df = pd.read_csv("ipl_2023.csv")

# Show top 5 rows
print("📊 First few rows:")
print(df.head())

# Basic info
print("\n📄 Columns in dataset:")
print(df.columns)

# Data summary
print("\n🔍 Info:")
print(df.info())
