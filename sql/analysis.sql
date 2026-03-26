USE ecommerce;

-- ==============================
-- BASIC CHECK
-- ==============================
SELECT COUNT(*) AS total_rows FROM survey_clean;

SELECT * FROM survey_clean LIMIT 5;

-- ==============================
-- PLATFORM ANALYSIS
-- ==============================
SELECT primary_platform, COUNT(*) AS users
FROM survey_clean
GROUP BY primary_platform
ORDER BY users DESC;

SELECT primary_platform, 
       AVG(satisfaction) AS avg_satisfaction,
       AVG(monthly_spending) AS avg_spend
FROM survey_clean
GROUP BY primary_platform
ORDER BY avg_spend DESC;

-- ==============================
-- DEMOGRAPHIC ANALYSIS
-- ==============================
SELECT gender, AVG(monthly_spending) AS avg_spend
FROM survey_clean
GROUP BY gender;

SELECT occupation, AVG(monthly_spending) AS avg_spend
FROM survey_clean
GROUP BY occupation
ORDER BY avg_spend DESC;

SELECT age, AVG(shopping_frequency) AS avg_frequency
FROM survey_clean
GROUP BY age;

-- ==============================
-- CUSTOMER BEHAVIOR
-- ==============================
SELECT purchase_factor, COUNT(*) AS count
FROM survey_clean
GROUP BY purchase_factor
ORDER BY count DESC;

SELECT primary_category, COUNT(*) AS purchases
FROM survey_clean
GROUP BY primary_category
ORDER BY purchases DESC;

-- ==============================
-- PAYMENT & EXPERIENCE
-- ==============================
SELECT payment_method, COUNT(*) AS users
FROM survey_clean
GROUP BY payment_method
ORDER BY users DESC;

SELECT delivery_issue, AVG(satisfaction) AS avg_satisfaction
FROM survey_clean
GROUP BY delivery_issue;

-- ==============================
-- PRICE SENSITIVITY
-- ==============================
SELECT price_compare, AVG(monthly_spending) AS avg_spend
FROM survey_clean
GROUP BY price_compare
ORDER BY price_compare DESC;

-- ==============================
-- HIGH VALUE CUSTOMERS
-- ==============================
SELECT *
FROM survey_clean
WHERE monthly_spending > 5000
ORDER BY monthly_spending DESC;

-- ==============================
-- COMBINED BUSINESS INSIGHT ⭐
-- ==============================
SELECT 
    primary_platform,
    COUNT(*) AS users,
    AVG(monthly_spending) AS avg_spend,
    AVG(satisfaction) AS avg_satisfaction
FROM survey_clean
GROUP BY primary_platform
ORDER BY avg_spend DESC;

-- ==============================
-- CLUSTERING DATA (FOR PYTHON)
-- ==============================
SELECT 
    age,
    income,
    monthly_spending,
    shopping_frequency,
    satisfaction
FROM survey_clean;