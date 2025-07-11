import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("ipl_2023.csv")

# ✅ Step 1: Filter out only actual wickets (ignore run outs and nulls)
wickets_df = df[(df["kind"].notnull()) & (df["kind"] != "run out")]

# ✅ Step 2: Count wickets per bowler
top_wicket_takers = wickets_df["bowler"].value_counts().head(10)

# ✅ Step 3: Plot
top_wicket_takers.plot(kind="bar", color="green", figsize=(10, 5))
plt.title("🎯 Top 10 Wicket Takers - IPL 2023")
plt.xlabel("Bowler")
plt.ylabel("Wickets")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
