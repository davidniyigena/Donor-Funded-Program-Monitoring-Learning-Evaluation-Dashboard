# Donor-Funded Program Monitoring, Learning & Evaluation Dashboard
# Visualization Script
# Author: David Niyigena

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/program_monitoring_data.csv")

# Create achievement rate
df["achievement_rate"] = (df["actual"] / df["target"]) * 100

# Create output folder note:
# The charts will be saved in the visuals folder when this script is run locally.

# 1. Beneficiaries reached by sector
beneficiaries_by_sector = (
    df.groupby("sector")["beneficiaries_reached"]
    .sum()
    .reset_index()
    .sort_values(by="beneficiaries_reached", ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=beneficiaries_by_sector,
    x="sector",
    y="beneficiaries_reached"
)
plt.title("Total Beneficiaries Reached by Sector")
plt.xlabel("Sector")
plt.ylabel("Beneficiaries Reached")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/beneficiaries_by_sector.png")
plt.close()

# 2. Achievement rate by donor
achievement_by_donor = (
    df.groupby("donor")[["target", "actual"]]
    .sum()
    .reset_index()
)

achievement_by_donor["achievement_rate"] = (
    achievement_by_donor["actual"] / achievement_by_donor["target"]
) * 100

achievement_by_donor = achievement_by_donor.sort_values(
    by="achievement_rate",
    ascending=False
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=achievement_by_donor,
    x="donor",
    y="achievement_rate"
)
plt.title("Achievement Rate by Donor")
plt.xlabel("Donor")
plt.ylabel("Achievement Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/achievement_rate_by_donor.png")
plt.close()

# 3. Implementation status summary
status_summary = (
    df["implementation_status"]
    .value_counts()
    .reset_index()
)

status_summary.columns = ["implementation_status", "count"]

plt.figure(figsize=(8, 5))
sns.barplot(
    data=status_summary,
    x="implementation_status",
    y="count"
)
plt.title("Implementation Status Summary")
plt.xlabel("Implementation Status")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/implementation_status_summary.png")
plt.close()

# 4. Data quality issues
data_quality_summary = (
    df["data_quality_issue"]
    .value_counts()
    .reset_index()
)

data_quality_summary.columns = ["data_quality_issue", "count"]

plt.figure(figsize=(6, 4))
sns.barplot(
    data=data_quality_summary,
    x="data_quality_issue",
    y="count"
)
plt.title("Data Quality Issue Summary")
plt.xlabel("Data Quality Issue")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("../visuals/data_quality_issues.png")
plt.close()

# 5. Achievement rate by reporting period
achievement_by_period = (
    df.groupby("reporting_period")[["target", "actual"]]
    .sum()
    .reset_index()
)

achievement_by_period["achievement_rate"] = (
    achievement_by_period["actual"] / achievement_by_period["target"]
) * 100

plt.figure(figsize=(8, 5))
sns.lineplot(
    data=achievement_by_period,
    x="reporting_period",
    y="achievement_rate",
    marker="o"
)
plt.title("Achievement Rate by Reporting Period")
plt.xlabel("Reporting Period")
plt.ylabel("Achievement Rate (%)")
plt.tight_layout()
plt.savefig("../visuals/achievement_rate_by_period.png")
plt.close()

print("Visualization files created successfully in the visuals folder.")
