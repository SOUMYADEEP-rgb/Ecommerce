import pandas as pd
import mysql.connector

# === DB CONNECTION ===
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root123",
    database="ecommerce"
)

# === DEFINE QUERIES ===
queries = {
    "Basic_Count": "SELECT COUNT(*) AS total_rows FROM survey_clean;",
    
    "Sample_Data": "SELECT * FROM survey_clean LIMIT 5;",
    
    "Platform_Users": """
        SELECT primary_platform, COUNT(*) AS users
        FROM survey_clean
        GROUP BY primary_platform
        ORDER BY users DESC;
    """,

    "Platform_Satisfaction": """
        SELECT primary_platform, 
               AVG(satisfaction) AS avg_satisfaction,
               AVG(monthly_spending) AS avg_spend
        FROM survey_clean
        GROUP BY primary_platform
        ORDER BY avg_spend DESC;
    """,

    "Gender_Spend": """
        SELECT gender, AVG(monthly_spending) AS avg_spend
        FROM survey_clean
        GROUP BY gender;
    """,

    "Occupation_Spend": """
        SELECT occupation, AVG(monthly_spending) AS avg_spend
        FROM survey_clean
        GROUP BY occupation
        ORDER BY avg_spend DESC;
    """,

    "Age_Frequency": """
        SELECT age, AVG(shopping_frequency) AS avg_frequency
        FROM survey_clean
        GROUP BY age;
    """,

    "Purchase_Factor": """
        SELECT purchase_factor, COUNT(*) AS count
        FROM survey_clean
        GROUP BY purchase_factor
        ORDER BY count DESC;
    """,

    "Category_Purchases": """
        SELECT primary_category, COUNT(*) AS purchases
        FROM survey_clean
        GROUP BY primary_category
        ORDER BY purchases DESC;
    """,

    "Payment_Method": """
        SELECT payment_method, COUNT(*) AS users
        FROM survey_clean
        GROUP BY payment_method
        ORDER BY users DESC;
    """,

    "Delivery_Impact": """
        SELECT delivery_issue, AVG(satisfaction) AS avg_satisfaction
        FROM survey_clean
        GROUP BY delivery_issue;
    """,

    "Price_Sensitivity": """
        SELECT price_compare, AVG(monthly_spending) AS avg_spend
        FROM survey_clean
        GROUP BY price_compare
        ORDER BY price_compare DESC;
    """,

    "High_Value_Customers": """
        SELECT *
        FROM survey_clean
        WHERE monthly_spending > 5000
        ORDER BY monthly_spending DESC;
    """,

    "Business_Insight": """
        SELECT 
            primary_platform,
            COUNT(*) AS users,
            AVG(monthly_spending) AS avg_spend,
            AVG(satisfaction) AS avg_satisfaction
        FROM survey_clean
        GROUP BY primary_platform
        ORDER BY avg_spend DESC;
    """,

    "Clustering_Data": """
        SELECT 
            age,
            income,
            monthly_spending,
            shopping_frequency,
            satisfaction
        FROM survey_clean;
    """
}

# === CREATE EXCEL FILE ===
output_file = "analysis_output_final.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for sheet_name, query in queries.items():
        df = pd.read_sql(query, conn)
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("✅ Excel file created: analysis_output_final.xlsx")
# Python code is used with sql to automate the execution of sql queries to be stored in excel sheets for permanent use

# === CLOSE CONNECTION ===
conn.close()