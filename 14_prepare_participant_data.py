import pandas as pd

# Load data
participants = pd.read_csv("data/raw/participants.csv")
roles = pd.read_csv("data/raw/roles.csv")

# Join participants with roles
participant_data = participants.merge(
    roles[["role_id", "role"]],
    on="role_id",
    how="left"
)

# Save processed dataset
participant_data.to_csv(
    "data/processed/participants_processed.csv",
    index=False
)

# Check result
print("Processed participant dataset shape:")
print(participant_data.shape)

print("\nColumns:")
print(participant_data.columns.tolist())

print("\nFirst 5 rows:")
print(participant_data.head())

print("\nSaved to:")
print("data/processed/participants_processed.csv")