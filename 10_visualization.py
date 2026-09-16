import pandas as pd
import matplotlib.pyplot as plt

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Convert date column to datetime
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Count activities by type
activity_counts = activities["activity_type"].value_counts()

# Create bar chart
activity_counts.plot(kind="bar")

plt.title("Activities by Type")
plt.xlabel("Activity Type")
plt.ylabel("Number of Activities")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()