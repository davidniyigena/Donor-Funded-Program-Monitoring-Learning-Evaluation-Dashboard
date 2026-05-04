# Project Summary: Donor-Funded Program Monitoring, Learning & Evaluation Dashboard

## 1. Project Purpose

This project demonstrates how data science and analytics can support monitoring, learning, and evaluation for donor-funded programs. The goal is to show how program data can be cleaned, analyzed, summarized, and transformed into insights that help nonprofit organizations, donors, and program teams make better decisions.

The project focuses on tracking program indicators, comparing targets against actual results, identifying data quality issues, and summarizing program performance across sectors, districts, regions, and reporting periods.

---

## 2. Background

Donor-funded programs often collect data from multiple locations and implementation teams. This data may include program activities, targets, actual achievements, beneficiaries reached, reporting periods, and data quality issues.

When this information is not organized properly, it becomes difficult to answer important questions such as:

- Are program activities meeting their targets?
- Which districts or regions are performing well?
- Which activities are at risk?
- Are there data quality issues that need attention?
- How many beneficiaries have been reached?
- What results should be reported to donors?

This project creates a structured example of how those questions can be answered using Python, SQL, and dashboard-style analysis.

---

## 3. Dataset Description

The dataset used in this project is a sample program monitoring dataset. It includes information about donor-funded activities across education, health, workforce development, and economic development programs.

Key fields include:

- Program ID
- Program name
- Country
- Region
- District
- Sector
- Activity
- Indicator
- Reporting period
- Target
- Actual result
- Beneficiaries reached
- Data quality issue
- Implementation status
- Donor

The dataset is stored in:

```text
data/program_monitoring_data.csv
