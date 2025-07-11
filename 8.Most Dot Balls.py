
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("ipl_2023.csv")

# A dot ball = batsman_run == 0
dot_balls = df[df["batsman_run"] == 0]

# Count dot balls by bowler
dot_ball_counts = dot_balls["bowler"].value_counts().head(10)

print("\n💤 Top 10 Dot Ball Bowlers:")
print(dot_ball_counts)
