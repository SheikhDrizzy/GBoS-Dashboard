import logging
from datetime import datetime

# Setup logging
log_file = "etl_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Job started...")



import pandas as pd
import pyodbc

# -----------------------------
# Config - Update your SQL Server info
# -----------------------------
excel_file = "C:/Users/HP/PythonClass/GBoS_Household_Survey_50.xlsx"
sql_server = "SHEIKH-OUSMAN-H\\SQLEXPRESS"   # e.g., localhost\SQLEXPRESS
database = "GBoS_Surveys"
table = "HouseholdSurvey"

# -----------------------------
# Step 1: Read Excel and get only Pending rows
# -----------------------------
df = pd.read_excel(excel_file)
df_pending = df[df['Status'] == 'Pending']

if df_pending.empty:
    print("✅ No new rows to process.")
    exit()

# -----------------------------
# Step 2: Clean Data
# -----------------------------
df_pending = df_pending.dropna()
df_pending = df_pending[(df_pending['HouseholdSize'] > 0) & (df_pending['Income'] > 0)]
valid_regions = ['Banjul', 'Kanifing', 'Brikama', 'Kerewan', 'Mansakonko', 'Janjanbureh', 'Basse']
df_pending = df_pending[df_pending['Region'].isin(valid_regions)]
df_pending['SubmissionDate'] = pd.to_datetime(df_pending['SubmissionDate'], errors='coerce')
df_pending = df_pending.dropna(subset=['SubmissionDate'])

print(f"✅ {len(df_pending)} new rows cleaned and ready to insert.")
logging.info("✅ 37 new rows cleaned and ready to insert.")
# # -----------------------------
# # Step 3: Push to SQL Server
# # -----------------------------
# try:
#     conn = pyodbc.connect(
#         f"Driver={{SQL Server}};"
#         f"Server={sql_server};"
#         f"Database={database};"
#         "Trusted_Connection=yes;"
#     )
#     cursor = conn.cursor()
#     print("✅ Connected to SQL Server")
# except Exception as e:
#     print(f"❌ SQL Server connection error: {e}")
#     exit()


# -----------------------------
# Step 3: Push to SQL Server
# -----------------------------
try:
    conn = pyodbc.connect(
        f"Driver={{SQL Server}};"
        f"Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"  # note the double backslash
        f"Database={database};"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    logging.info("✅ Connected to SQL Server")
except Exception as e:
    print(f"❌ SQL Server connection error: {e}")
    exit()


for index, row in df_pending.iterrows():
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE SurveyID = ?", row['SurveyID'])
        if cursor.fetchone()[0] == 0:
            cursor.execute(f"""
                INSERT INTO {table} 
                (SurveyID, Region, HouseholdSize, Income, EducationLevel, SubmissionDate, MaritalStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, row['SurveyID'], row['Region'], row['HouseholdSize'], row['Income'],
                 row['EducationLevel'], row['SubmissionDate'], row['MaritalStatus'])
        # Mark the row as processed in Excel
        df.loc[df['SurveyID'] == row['SurveyID'], 'Status'] = 'Processed'
    except Exception as e:
        logging.error(f"❌ Error: {e}")
conn.commit()
cursor.close()
conn.close()
logging.info("✅ Data pushed to SQL Server successfully!")

# -----------------------------
# Step 4: Update Excel file
# -----------------------------
df.to_excel(excel_file, index=False)
print(f"✅ Excel updated, new rows marked as Processed.")
