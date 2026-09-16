import pandas as pd

# Load data
participants = pd.read_csv("data/raw/participants.csv")

# Load roles
roles = pd.read_csv("data/raw/roles.csv")

# Join participants with roles
participant_roles = participants.merge(
    roles,
    on="role_id",
    how="left"
)

# Gender distribution
print("Participants by gender:")
print(
    participant_roles["gender"]
    .value_counts()
)

# Age distribution
print("\nParticipants by age group:")
print(
    participant_roles["age_group"]
    .value_counts()
)

# Role distribution
print("\nParticipants by role:")
print(
    participant_roles["role"]
    .value_counts()
)