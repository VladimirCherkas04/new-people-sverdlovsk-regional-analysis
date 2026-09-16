# Political Activity & Participation Analysis

## Sverdlovsk Regional Branch of the New People political party

This project demonstrates an end-to-end data analytics workflow for analyzing political activity, participation patterns, and organizational characteristics.

The project uses a synthetic dataset designed for portfolio and methodological demonstration purposes.

## Project objectives

The analysis explores:

- activity dynamics over time;
- activity types and topics;
- geographic distribution of activities;
- participation patterns;
- gender and age structure of participation records;
- participation by organizational role;
- public vs non-public activities;
- engagement by activity type and topic;
- relationships between activity types and topics.

## Data

The dataset contains four related tables:

- `activities` — information about activities and events;
- `locations` — municipalities and locations;
- `participants` — participation records;
- `roles` — organizational roles.

### Important data note

The dataset is **synthetic**.

It does not contain real internal data, personal data, or confidential information from the New People political party or its Sverdlovsk Regional Branch.

The dataset was created to demonstrate data analysis methods and technical skills.

## Project structure

```text
new-people-sverdlovsk-regional-analysis/
│
├── README.md
├── data/
│   ├── raw/
│   │   ├── activities.csv
│   │   ├── participants.csv
│   │   ├── locations.csv
│   │   ├── roles.csv
│   │   └── DATA_NOTE.txt
│   │
│   └── processed/
│       ├── activities_processed.csv
│       └── participants_processed.csv
│
├── sql/
│   ├── 01_data_quality.sql
│   ├── 02_activity_over_time.sql
│   ├── 03_activity_by_type.sql
│   ├── 04_activity_by_topic.sql
│   ├── 05_activity_by_location.sql
│   ├── 06_participation_by_gender.sql
│   ├── 07_gender_by_role.sql
│   ├── 08_participation_by_age.sql
│   ├── 09_gender_by_age.sql
│   ├── 10_role_by_age.sql
│   ├── 11_public_vs_nonpublic.sql
│   ├── 12_activity_type_engagement.sql
│   ├── 13_topic_engagement.sql
│   ├── 14_yearly_activity_summary.sql
│   ├── 15_activity_participation_profile.sql
│   ├── 16_top_activities_by_type.sql
│   ├── 17_activity_type_by_year.sql
│   └── 18_activity_type_topic_matrix.sql
│
├── python/
│   ├── 01_data_loading.py
│   ├── 02_data_quality.py
│   ├── 03_data_cleaning.py
│   ├── 04_activity_eda.py
│   ├── 05_activity_over_time.py
│   ├── 06_participation_analysis.py
│   ├── 07_public_activity.py
│   ├── 08_location_analysis.py
│   ├── 09_participant_analysis.py
│   ├── 10_visualization.py
│   ├── 11_time_visualization.py
│   ├── 12_participant_visualization.py
│   ├── 13_prepare_activity_data.py
│   └── 14_prepare_participant_data.py
│
├── tableau/
│   └── political_activity_analysis.twb
│
└── visualizations/