# Project Summary: Donor-Funded Program Monitoring, Learning & Evaluation Dashboard

## 1. Project Purpose

This project demonstrates how data science and analytics can support monitoring, learning, and evaluation for donor-funded programs. The goal is to show how program data can be cleaned, analyzed, summarized, visualized, and transformed into insights that help nonprofit organizations, donors, and program teams make better decisions.

The project focuses on tracking program indicators, comparing targets against actual results, identifying data quality issues, and summarizing program performance across sectors, districts, regions, donors, and reporting periods.

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

Dataset file: `data/program_monitoring_data.csv`

---

## 4. Methods

This project uses a basic data analytics workflow.

### Data Cleaning

The Python script checks the data structure, reviews missing values, standardizes column names, creates calculated fields, and prepares the dataset for analysis.

Script file: `scripts/01_data_cleaning_and_eda.py`

### SQL Analysis

SQL queries are used to organize and summarize the monitoring data. The SQL file includes queries for achievement rates, below-target activities, beneficiary totals, donor performance, data quality issues, and regional performance.

SQL file: `sql/program_monitoring_queries.sql`

### Visualization

The visualization script creates chart outputs for program performance, donor achievement rates, implementation status, data quality issues, beneficiary reach, and reporting-period trends.

Visualization script: `scripts/02_visualizations.py`

### Dashboard Planning

The dashboard plan outlines proposed dashboard sections, KPI cards, filters, visualizations, and a future Google Looker Studio dashboard structure.

Dashboard plan file: `visuals/dashboard_plan.md`

---

## 5. Key Performance Questions

This project is designed to answer the following monitoring and evaluation questions:

1. Which activities are meeting or exceeding their targets?
2. Which activities are below target and may need follow-up?
3. How many beneficiaries were reached by sector?
4. Which donors have the highest overall achievement rate?
5. Which records have data quality issues?
6. How does program performance change across reporting periods?
7. Which regions or districts need additional implementation support?

---

## 6. Expected Insights

This project is expected to produce insights such as:

- Education and health programs may reach large numbers of beneficiaries.
- Some activities may be at risk during early reporting periods but improve over time.
- Data quality issues may affect performance interpretation.
- Achievement rates can help program teams identify which activities need additional support.
- Donor reporting can be strengthened through structured data summaries.

---

## 7. Visualization Outputs and Key Findings

This project includes generated visualization images that summarize major monitoring and evaluation insights from the dataset.

### Visualization Files

The following chart images are stored in the `visuals/` folder:

- `visuals/achievement_rate_by_period.png`
- `visuals/beneficiaries_by_sector.png`
- `visuals/data_quality_issues.png`
- `visuals/implementation_status_summary.png`
- `visuals/achievement_rate_by_donor.png`

### Key Findings from the Visualizations

1. **Achievement rate improved across reporting periods.**  
   The achievement rate increased from Q1-2025 to Q3-2025, suggesting improved program performance over time.

2. **Health and education reached the largest number of beneficiaries.**  
   The beneficiary reach chart shows that health and education activities reached more participants compared with other sectors.

3. **Most records did not show data quality issues.**  
   The data quality issue summary shows that most reporting records were clean, while a smaller number required follow-up.

4. **Most activities were on track.**  
   The implementation status summary shows that many activities were classified as on track, with fewer activities marked as at risk.

5. **Donor achievement rates were relatively strong.**  
   The donor achievement chart shows high achievement rates across donors, indicating generally strong implementation performance.

### Why These Visualizations Matter

These visualizations help program managers, monitoring and evaluation teams, and donors quickly understand where the program is performing well and where follow-up may be needed. They also make the project more useful for dashboard development and donor reporting.

---

## 8. Tools Used

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

## 9. Skills Demonstrated

This project demonstrates the following skills:

- Data cleaning
- Data transformation
- Exploratory data analysis
- Descriptive analytics
- SQL querying
- Data visualization
- Monitoring and evaluation analytics
- Donor reporting
- Program performance tracking
- Data quality assessment
- Dashboard planning
- Predictive analytics preparation

---

## 10. Portfolio Relevance

This project connects data science with monitoring, evaluation, accountability, and learning. It reflects how data analytics can support nonprofit organizations, donor-funded programs, education systems, health programs, and social impact initiatives.

It also demonstrates practical skills in Python, SQL, data cleaning, reporting, visualization, and dashboard development.

---

## 11. Next Steps

Future improvements to this project may include:

- Adding a cleaned dataset output
- Creating a full Jupyter Notebook version of the analysis
- Expanding the dataset with more reporting periods
- Adding more advanced visualizations
- Building an interactive dashboard in Google Looker Studio
- Adding predictive modeling to classify activities as on-track or off-track
- Updating the README with dashboard screenshots or dashboard links
