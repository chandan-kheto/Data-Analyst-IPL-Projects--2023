import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("ipl_2023.csv")

# Filter only sixes
sixes_df = df[df["batsman_run"] == 6]

# Count sixes per batter
top_six_hitters = sixes_df["batter"].value_counts().head(10)

# Print
print("💣 Top 10 Six Hitters:")
print(top_six_hitters)

# Plot
top_six_hitters.plot(kind="bar", color="purple", figsize=(10, 5))
plt.title("💥 Top 10 Six Hitters - IPL 2023")
plt.xlabel("Batter")
plt.ylabel("Total Sixes")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
