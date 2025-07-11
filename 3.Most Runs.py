import pandas as pd

# Load the CSV
df = pd.read_csv("ipl_2023.csv")

# Group by batter and sum total runs
top_runs = df.groupby("batter")["batsman_run"].sum().sort_values(ascending=False)

# Show top 10 run-scorers
print("🏆 Top 10 Run Scorers:")
print(top_runs.head(10))
