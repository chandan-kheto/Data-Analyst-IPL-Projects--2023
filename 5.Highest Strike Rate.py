import pandas as pd

# Load the CSV
df = pd.read_csv("ipl_2023.csv")
# Group by batter
batter_stats = df.groupby("batter").agg({
    "batsman_run": "sum",
    "ballnumber": "count"
})

# Rename columns
batter_stats.columns = ["total_runs", "balls_faced"]

# Calculate strike rate
batter_stats["strike_rate"] = (batter_stats["total_runs"] / batter_stats["balls_faced"]) * 100

# Filter: min 100 balls faced
filtered = batter_stats[batter_stats["balls_faced"] >= 100]

# Sort by strike rate
top_strikers = filtered.sort_values(by="strike_rate", ascending=False).head(10)

print("\n⚡ Top 10 Strike Rates (min 100 balls):")
print(top_strikers)
