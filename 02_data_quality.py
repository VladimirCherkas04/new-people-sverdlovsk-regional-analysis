import pandas as pd

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Basic information
print("Dataset shape:")
print(activities.shape)

print("\nColumn names:")
print(activities.columns.tolist())

print("\nData types:")
print(activities.dtypes)

print("\nMissing values:")
print(activities.isnull().sum())

print("\nDuplicate rows:")
print(activities.duplicated().sum())