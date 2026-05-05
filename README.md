# Donor-Funded Program Monitoring, Learning & Evaluation Dashboard

## Project Overview

This project is a data science portfolio project focused on monitoring, learning, and evaluation for donor-funded programs. It demonstrates how data can be used to track program indicators, monitor implementation progress, identify data quality issues, and support evidence-based decision-making.

The project is designed around a nonprofit and development-program context, where donors, program managers, monitoring and evaluation teams, and stakeholders need reliable dashboards and reports to understand program performance.

---

## Problem Statement

Donor-funded programs often collect large amounts of data across activities, beneficiaries, locations, indicators, and reporting periods. However, this data can become difficult to manage when it is stored in different formats or reported inconsistently.

This project addresses the need for a structured analytics workflow that can:

- Organize program monitoring data
- Clean and validate indicator data
- Track progress against targets
- Identify missing or inconsistent records
- Summarize results for donor reporting
- Support learning and program improvement

---

## Objectives

The main objectives of this project are to:

- Build a clean and organized monitoring and evaluation dataset
- Use SQL to query program indicators, activities, and reporting data
- Use Python for data cleaning, analysis, and visualization
- Create dashboard-style visuals for program performance tracking
- Demonstrate descriptive analytics and early predictive analytics concepts
- Present findings in a clear format for nonprofit and donor-funded program stakeholders

---

## Repository Structure

- `data/program_monitoring_data.csv`
- `sql/program_monitoring_queries.sql`
- `scripts/01_data_cleaning_and_eda.py`
- `reports/project_summary.md`
- `visuals/dashboard_plan.md`
- `README.md`
- `requirements.txt`

---

## Dataset

The dataset is a sample donor-funded program monitoring dataset. It includes information on program activities, sectors, districts, reporting periods, targets, actual results, beneficiaries reached, data quality issues, implementation status, and donors.

**Dataset file:** `data/program_monitoring_data.csv`

### Key Fields

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

---

## Tools and Technologies

- Python
- SQL
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Google Looker Studio
- Jupyter Notebook
- CSV data files

---

## Analysis Workflow

### 1. Data Cleaning and Transformation

The Python script loads the dataset, checks missing values, standardizes column names, creates an achievement rate field, categorizes performance, and prepares the dataset for analysis.

**Script file:** `scripts/01_data_cleaning_and_eda.py`

### 2. SQL Analysis

The SQL file contains queries to summarize and analyze program monitoring data.

**SQL file:** `sql/program_monitoring_queries.sql`

The SQL queries answer questions such as:

- Which activities are below target?
- Which activities exceeded their targets?
- What is the total number of beneficiaries reached by sector?
- What is the overall achievement rate by donor?
- Which records have data quality issues?
- How does performance change by reporting period?
- Which regions show stronger program performance?

### 3. Reporting

The project summary explains the purpose, background, dataset, methods, key performance questions, expected insights, and next steps.

**Report file:** `reports/project_summary.md`

### 4. Dashboard Planning

The dashboard plan outlines the proposed dashboard sections, KPI cards, filters, visualizations, and Google Looker Studio dashboard structure.

**Dashboard plan file:** `visuals/dashboard_plan.md`

---

## Key Performance Questions

This project is designed to answer the following monitoring and evaluation questions:

1. Are program activities meeting their targets?
2. Which activities are below target and may need follow-up?
3. Which programs or sectors are reaching the most beneficiaries?
4. Which donors have the highest overall achievement rates?
5. Which records have data quality issues?
6. How does performance change across reporting periods?
7. Which regions or districts need additional implementation support?

---

## Key Skills Demonstrated

- Data cleaning
- Data transformation
- Descriptive analytics
- Predictive analytics planning
- SQL querying
- Dashboard planning
- Data visualization
- Monitoring and evaluation analytics
- Donor reporting
- Program performance tracking
- Data quality assessment
- Regression and classification modeling concepts
- Machine learning model training, testing, and evaluation preparation

---

## Planned Visualizations

The project is designed to support dashboard visuals such as:

- KPI cards
- Target vs. actual charts
- Beneficiaries reached by sector
- Achievement rate by reporting period
- Data quality issue summary
- Implementation status summary
- Donor performance summary
- Regional performance charts

---

## How to Use This Project

### 1. Clone the repository

`git clone https://github.com/davidniyigena/Donor-Funded-Program-Monitoring-Learning-Evaluation-Dashboard.git`

### 2. Install required packages

`pip install -r requirements.txt`

### 3. Run the Python analysis script

`python scripts/01_data_cleaning_and_eda.py`

### 4. Review the SQL queries

Open: `sql/program_monitoring_queries.sql`

### 5. Review the report and dashboard plan

Open:

- `reports/project_summary.md`
- `visuals/dashboard_plan.md`

---

## Portfolio Relevance

This project connects my background in monitoring, evaluation, accountability, and learning with data science and analytics. It demonstrates how Python, SQL, dashboards, and machine learning concepts can support donor-funded programs, nonprofit decision-making, education systems, health programs, and social impact measurement.

---

## Future Improvements

Future improvements may include:

- Adding a cleaned dataset output
- Creating a Jupyter Notebook version of the analysis
- Adding generated visualization images
- Building an interactive Google Looker Studio dashboard
- Publishing dashboard screenshots
- Expanding the dataset with more reporting periods
- Adding predictive modeling to classify activities as on-track or off-track

---

## Author

**David Niyigena**  
Data Scientist | Data Analytics | Monitoring & Evaluation Specialist  
GitHub: [github.com/davidniyigena](https://github.com/davidniyigena)
