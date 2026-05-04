# Donor-Funded Program Monitoring, Learning & Evaluation Dashboard
# Data Cleaning and Exploratory Data Analysis
# Author: David Niyigena

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/program_monitoring_data.csv")

# Preview data
print("First five rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Create achievement rate
df["achievement_rate"] = (df["actual"] / df["target"]) * 100

# Create performance category
def categorize_performance(rate):
    if rate >= 100:
        return "Exceeded Target"
    elif rate >= 90:
        return "On Track"
    elif rate >= 75:
        return "At Risk"
    else:
        return "Off Track"

df["performance_category"] = df["achievement_rate"].apply(categorize_performance)

# Summary statistics
print("\nSummary statistics:")
print(df[["target", "actual", "beneficiaries_reached", "achievement_rate"]].describe())

# Total beneficiaries by sector
beneficiaries_by_sector = (
    df.groupby("sector")["beneficiaries_reached"]
    .sum()
    .reset_index()
    .sort_values(by="beneficiaries_reached", ascending=False)
)

print("\nTotal beneficiaries reached by sector:")
print(beneficiaries_by_sector)

# Achievement rate by reporting period
achievement_by_period = (
    df.groupby("reporting_period")[["target", "actual"]]
    .sum()
    .reset_index()
)

achievement_by_period["achievement_rate"] = (
    achievement_by_period["actual"] / achievement_by_period["target"]
) * 100

print("\nAchievement rate by reporting period:")
print(achievement_by_period)

# Data quality issues
data_quality_summary = df["data_quality_issue"].value_counts().reset_index()
data_quality_summary.columns = ["data_quality_issue", "count"]

print("\nData quality issue summary:")
print(data_quality_summary)

# Save cleaned dataset
df.to_csv("../data/cleaned_program_monitoring_data.csv", index=False)

print("\nCleaned dataset saved to data/cleaned_program_monitoring_data.csv")

# Visualization: beneficiaries by sector
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
plt.show()

# Visualization: achievement rate by reporting period
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
plt.show()

# Visualization: data quality issues
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
plt.show()
