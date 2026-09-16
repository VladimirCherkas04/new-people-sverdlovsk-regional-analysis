import pandas as pd
import matplotlib.pyplot as plt

# Load data
activities = pd.read_csv("data/raw/activities.csv")

# Convert date column to datetime
activities["activity_date"] = pd.to_datetime(activities["activity_date"])

# Count activities by month
monthly_activity = (
    activities
    .set_index("activity_date")
    .resample("ME")
    .size()
)

# Create line chart
monthly_activity.plot(kind="line", marker="o")

plt.title("Monthly Activity")
plt.xlabel("Month")
plt.ylabel("Number of Activities")
plt.grid(True)
plt.tight_layout()
plt.show()