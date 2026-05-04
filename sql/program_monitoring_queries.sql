-- Donor-Funded Program Monitoring, Learning & Evaluation Dashboard
-- SQL Portfolio Queries
-- Author: David Niyigena

-- 1. View all program monitoring records
SELECT *
FROM program_monitoring_data;

-- 2. Calculate achievement rate for each activity
SELECT
    program_name,
    district,
    sector,
    activity,
    indicator,
    reporting_period,
    target,
    actual,
    ROUND((actual * 100.0 / target), 2) AS achievement_rate
FROM program_monitoring_data
ORDER BY achievement_rate DESC;

-- 3. Identify activities below target
SELECT
    program_name,
    district,
    activity,
    indicator,
    reporting_period,
    target,
    actual,
    ROUND((actual * 100.0 / target), 2) AS achievement_rate,
    implementation_status
FROM program_monitoring_data
WHERE actual < target
ORDER BY achievement_rate ASC;

-- 4. Summarize total beneficiaries reached by sector
SELECT
    sector,
    SUM(beneficiaries_reached) AS total_beneficiaries_reached
FROM program_monitoring_data
GROUP BY sector
ORDER BY total_beneficiaries_reached DESC;

-- 5. Summarize performance by donor
SELECT
    donor,
    COUNT(*) AS number_of_records,
    SUM(target) AS total_target,
    SUM(actual) AS total_actual,
    ROUND((SUM(actual) * 100.0 / SUM(target)), 2) AS overall_achievement_rate
FROM program_monitoring_data
GROUP BY donor
ORDER BY overall_achievement_rate DESC;

-- 6. Identify records with data quality issues
SELECT
    program_name,
    district,
    activity,
    indicator,
    reporting_period,
    data_quality_issue,
    implementation_status
FROM program_monitoring_data
WHERE data_quality_issue = 'Yes';

-- 7. Track implementation status counts
SELECT
    implementation_status,
    COUNT(*) AS status_count
FROM program_monitoring_data
GROUP BY implementation_status
ORDER BY status_count DESC;

-- 8. Compare target versus actual by reporting period
SELECT
    reporting_period,
    SUM(target) AS total_target,
    SUM(actual) AS total_actual,
    ROUND((SUM(actual) * 100.0 / SUM(target)), 2) AS achievement_rate
FROM program_monitoring_data
GROUP BY reporting_period
ORDER BY reporting_period;

-- 9. Summarize program performance by region
SELECT
    region,
    COUNT(*) AS number_of_records,
    SUM(target) AS total_target,
    SUM(actual) AS total_actual,
    ROUND((SUM(actual) * 100.0 / SUM(target)), 2) AS achievement_rate
FROM program_monitoring_data
GROUP BY region
ORDER BY achievement_rate DESC;

-- 10. Identify programs that exceeded target
SELECT
    program_name,
    district,
    activity,
    indicator,
    reporting_period,
    target,
    actual,
    ROUND((actual * 100.0 / target), 2) AS achievement_rate
FROM program_monitoring_data
WHERE actual > target
ORDER BY achievement_rate DESC;
