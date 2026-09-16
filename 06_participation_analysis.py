import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Convert date column to datetime
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Participation statistics by activity type
print("Participation by activity type:")
print(
    activities.groupby("activity_type")["participants_count"]
    .agg(["count", "sum", "mean", "median"])
    .sort_values("sum", ascending=False)
)

# Participation statistics by topic
print("\nParticipation by topic:")
print(
    activities.groupby("topic")["participants_count"]
    .agg(["count", "sum", "mean", "median"])
    .sort_values("sum", ascending=False)
)