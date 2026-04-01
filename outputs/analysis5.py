import pandas as pd
import mysql.connector

# === DATABASE CONNECTION ===
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root123",
    database="ecommerce"
)

cursor = conn.cursor()

# === QUERIES ===
queries = {

    # ✅ BASIC CHECK
    "Basic_Count": "SELECT COUNT(*) AS total_rows FROM survey_clean;",


    # ⭐ WINDOW FUNCTION (RANK)
    "Platform_Ranking": """
        SELECT 
            primary_platform,
            AVG(monthly_spending) AS avg_spend,
            RANK() OVER (ORDER BY AVG(monthly_spending) DESC) AS spend_rank
        FROM survey_clean
        GROUP BY primary_platform;
    """,


    # ⭐ CASE STATEMENT (Customer Segmentation)
    "Customer_Segments": """
        SELECT 
            primary_platform,
            monthly_spending,
            CASE 
                WHEN monthly_spending > 5000 THEN 'High'
                WHEN monthly_spending BETWEEN 2000 AND 5000 THEN 'Medium'
                ELSE 'Low'
            END AS customer_segment
        FROM survey_clean;
    """,


    # ⭐ SUBQUERY (Above Average Customers)
    "Above_Average_Customers": """
        SELECT *
        FROM survey_clean
        WHERE monthly_spending > (
            SELECT AVG(monthly_spending) FROM survey_clean
        );
    """,


    # ✅ BUSINESS INSIGHT
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


    # ✅ CLUSTERING DATA (for ML/Python)
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
output_file = "analysis_output5_final.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for sheet_name, query in queries.items():
        try:
            cursor.execute(query)

            if cursor.with_rows:
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                df = pd.DataFrame(rows, columns=columns)
                df.to_excel(writer, sheet_name=sheet_name, index=False)

                print(f"✅ {sheet_name} done")

        except Exception as e:
            print(f"❌ Error in {sheet_name}: {e}")

# === CLOSE CONNECTION ===
cursor.close()
conn.close()

print("🎉 Excel file created: analysis_output5.xlsx")