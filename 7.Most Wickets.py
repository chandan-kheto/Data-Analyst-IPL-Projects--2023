import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("ipl_2023.csv")
# Filter rows where wicket was taken (not null 'kind' and not 'run out')
wickets_df = df[(df["kind"].notnull()) & (df["kind"] != "run out")]

# Count wickets by bowler
top_wicket_takers = wickets_df["bowler"].value_counts().head(10)

print("🎯 Top 10 Wicket Takers:")
print(top_wicket_takers)