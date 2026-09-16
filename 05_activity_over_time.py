import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Convert date column to datetime
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Extract year and month
activities["year"] = activities["activity_date"].dt.year
activities["month"] = activities["activity_date"].dt.month

# Activity count by year
print("Activities by year:")
print(activities["year"].value_counts().sort_index())

# Activity count by year and month
print("\nActivities by year and month:")
print(
    activities.groupby(["year", "month"])
    .size()
    .reset_index(name="activity_count")
)