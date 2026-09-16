import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Convert date column to datetime
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Activity types
print("Activities by type:")
print(activities["activity_type"].value_counts())

# Topics
print("\nActivities by topic:")
print(activities["topic"].value_counts())

# Participants statistics
print("\nParticipants statistics:")
print(activities["participants_count"].describe())