import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Convert date column to datetime
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Check data types
print(activities.dtypes)

# Check date range
print("\nDate range:")
print(activities["activity_date"].min())
print(activities["activity_date"].max())