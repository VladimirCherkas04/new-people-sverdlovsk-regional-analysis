import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Number of activities by public status
print("Activities by public status:")
print(
    activities["public_event"]
    .value_counts()
)

# Participation by public status
print("\nParticipation by public status:")
print(
    activities.groupby("public_event")["participants_count"]
    .agg(["count", "sum", "mean", "median"])
    .sort_values("sum", ascending=False)
)