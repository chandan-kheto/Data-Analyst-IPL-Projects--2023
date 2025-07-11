import pandas as pd

# Load the CSV
df = pd.read_csv("ipl_2023.csv")

# Filter only 6s
sixes_df = df[df["batsman_run"] == 6]

# Count sixes per batter
top_six_hitters = sixes_df["batter"].value_counts().head(10)

print("\n💣 Top 10 Six Hitters:")
print(top_six_hitters)
