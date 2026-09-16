import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")
locations = pd.read_csv("data/raw/locations.csv")

# Convert date column
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Add year and month
activities["year"] = activities["activity_date"].dt.year
activities["month"] = activities["activity_date"].dt.month
activities["month_name"] = activities["activity_date"].dt.strftime("%B")

# Join with locations
activity_data = activities.merge(
    locations[
        ["location_id", "municipality", "city", "district", "location_type"]
    ],
    on="location_id",
    how="left"
)

# Save processed dataset
activity_data.to_csv(
    "data/processed/activities_processed.csv",
    index=False
)

# Check result
print("Processed dataset shape:")
print(activity_data.shape)

print("\nColumns:")
print(activity_data.columns.tolist())

print("\nFirst 5 rows:")
print(activity_data.head())

print("\nSaved to:")
print("data/processed/activities_processed.csv")