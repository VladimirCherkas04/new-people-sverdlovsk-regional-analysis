import pandas as pd
import matplotlib.pyplot as plt

# Load data
participants = pd.read_csv("data/raw/participants.csv")

# Gender distribution
gender_counts = participants["gender"].value_counts()

gender_counts.plot(kind="bar")

plt.title("Participants by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Participation Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Age distribution
age_order = ["18-24", "25-34", "35-44", "45-54", "55+"]

age_counts = (
    participants["age_group"]
    .value_counts()
    .reindex(age_order)
)

age_counts.plot(kind="bar")

plt.title("Participants by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Participation Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()