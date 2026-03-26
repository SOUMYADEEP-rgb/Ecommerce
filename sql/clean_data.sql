USE ecommerce;

DROP TABLE IF EXISTS survey_clean;

CREATE TABLE survey_clean AS
SELECT

col1 AS timestamp,

CASE
    WHEN col2 = '<18' THEN 15
    WHEN REPLACE(col2,'–','-') = '18-30' THEN 24
    WHEN REPLACE(col2,'–','-') = '30-50' THEN 40
    ELSE 60
END AS age,

CASE
    WHEN col3 = 'Male' THEN 1
    WHEN col3 = 'Female' THEN 2
    ELSE 0
END AS gender,

CASE
    WHEN col4 = 'Student' THEN 1
    WHEN col4 = 'Working Professional' THEN 2
    WHEN col4 = 'Business' THEN 3
    ELSE 4
END AS occupation,

CASE
    WHEN col5 LIKE '<%' THEN 5000
    WHEN col5 LIKE '10%' THEN 20000
    WHEN col5 LIKE '30%' THEN 45000
    WHEN col5 LIKE '60%' THEN 80000
    ELSE 120000
END AS income,

col6 AS platforms_used,
col7 AS primary_platform,

CASE
    WHEN col8 = 'Daily' THEN 30
    WHEN col8 = 'Weekly' THEN 12
    WHEN col8 = 'Monthly' THEN 4
    ELSE 1
END AS shopping_frequency,

CASE
    WHEN col9 LIKE '<%' THEN 500
    WHEN col9 LIKE '1000%' THEN 2000
    WHEN col9 LIKE '3000%' THEN 5000
    ELSE 8000
END AS monthly_spending,

col10 AS primary_category,
col11 AS secondary_category,
col12 AS purchase_factor,

-- ✅ price_compare (col13)
CASE
    WHEN col13 = 'Always' THEN 4
    WHEN col13 = 'Sometimes' THEN 3
    WHEN col13 = 'Rarely' THEN 2
    WHEN col13 = 'Never' THEN 1
    ELSE 0
END AS price_compare,

-- shifted
CAST(col14 AS UNSIGNED) AS satisfaction,
CAST(col15 AS UNSIGNED) AS price_importance,
CAST(col16 AS UNSIGNED) AS delivery_importance,
CAST(col17 AS UNSIGNED) AS variety_importance,

-- ✅ FIXED
CAST(col18 AS UNSIGNED) AS return_importance,

CASE 
    WHEN col19 = 'Yes' THEN 1 
    ELSE 0 
END AS delivery_issue,

CASE
    WHEN REPLACE(col20,'–','-') = '1-3 days' THEN 2
    WHEN REPLACE(col20,'–','-') = '3-7 days' THEN 5
    WHEN col20 = 'Same day' THEN 1
    ELSE 9
END AS delivery_days,

col21 AS payment_method

FROM survey_raw;