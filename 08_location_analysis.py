import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")
locations = pd.read_csv("data/raw/locations.csv")

# Join activities with locations
activity_locations = activities.merge(
    locations,
    on="location_id",
    how="left"
)

# Check the result
print("Joined dataset:")
print(activity_locations.head())

# Activity count by municipality
print("\nActivities by municipality:")
print(
    activity_locations["municipality"]
    .value_counts()
)

# Participation by municipality
print("\nParticipation by municipality:")
print(
    activity_locations.groupby("municipality")["participants_count"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)