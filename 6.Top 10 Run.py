import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("ipl_2023.csv")

# ✅ Step 1: Calculate top 10 run scorers
top_runs = df.groupby("batter")["batsman_run"].sum().sort_values(ascending=False)

# ✅ Step 2: Plot it
top_runs.head(10).plot(kind="bar", color="orange", figsize=(10, 5))
plt.title("🏏 Top 10 Run Scorers - IPL 2023")
plt.xlabel("Batter")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()


