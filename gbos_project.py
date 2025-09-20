# import pandas as pd
# import pyodbc
# import os

# # -----------------------------
# # Configuration
# # -----------------------------
# excel_file = "C:/Users/HP/PythonClass/GBoS_Household_Survey_50.xlsx"
# sql_server = "YOUR_SERVER_NAME"   # <-- Replace with your server name
# database = "GBoS_Surveys"         # <-- Replace with your database name
# table = "HouseholdSurvey"

# # -----------------------------
# # Step 1: Generate Sample Dataset
# # -----------------------------
# data = {
#     "SurveyID": list(range(1, 51)),
#     "Region": ["Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse",
#                "Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse",
#                "Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse",
#                "Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse",
#                "Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse",
#                "Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse",
#                "Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Basse"],
#     "HouseholdSize": [4,6,5,3,7,4,5,2,8,3,6,4,5,3,7,4,5,2,6,3,5,4,7,3,5,4,6,3,5,4,6,3,5,4,7,4,5,2,6,3,5,4,6,3,5,4,7,4,5,3],
#     "Income": [25000,35000,28000,22000,40000,27000,30000,18000,45000,20000,
#                35000,26000,32000,21000,40000,27000,30000,19000,36000,22000,
#                31000,25000,42000,20000,30000,27000,38000,21000,31000,26000,
#                34000,21000,32000,27000,41000,28000,30000,18000,36000,22000,
#                33000,27000,38000,21000,31000,26000,42000,27000,30000,20000],
#     "EducationLevel": ["Secondary","Tertiary","Primary","Secondary","None","Secondary","Primary",
#                        "Tertiary","Secondary","Primary","Tertiary","Secondary","Primary","Tertiary",
#                        "Secondary","Primary","Tertiary","Secondary","Primary","Tertiary",
#                        "Secondary","Primary","Tertiary","Secondary","Primary","Tertiary","Secondary",
#                        "Primary","Tertiary","Secondary","Primary","Tertiary","Secondary","Primary",
#                        "Tertiary","Secondary","Primary","Tertiary","Secondary","Primary","Tertiary",
#                        "Secondary","Primary","Tertiary","Secondary","Primary","Tertiary","Secondary",
#                        "Primary","Tertiary","Secondary"],
#     "SubmissionDate": pd.date_range(start="2025-09-01", periods=50, freq='D'),
#     "MaritalStatus": ["Married","Married","Single","Married","Married","Single","Married",
#                       "Single","Married","Single","Married","Single","Married","Single",
#                       "Married","Single","Married","Single","Married","Single","Married","Single",
#                       "Married","Single","Married","Single","Married","Single","Married","Single",
#                       "Married","Single","Married","Single","Married","Single","Married","Single",
#                       "Married","Single","Married","Single","Married","Single","Married","Single",
#                       "Married","Single"]
# }

# df = pd.DataFrame(data)

# # Save Excel
# df.to_excel(excel_file, index=False)
# print(f"✅ Excel file created at {excel_file}")

# # -----------------------------
# # Step 2: Validate Data
# # -----------------------------
# df = df.dropna()
# df = df[(df['HouseholdSize'] > 0) & (df['Income'] > 0)]
# valid_regions = ['Banjul', 'Kanifing', 'Brikama', 'Kerewan', 'Mansakonko', 'Janjanbureh', 'Basse']
# df = df[df['Region'].isin(valid_regions)]
# df['SubmissionDate'] = pd.to_datetime(df['SubmissionDate'], errors='coerce')
# df = df.dropna(subset=['SubmissionDate'])

# # -----------------------------
# # Step 3: Connect to SQL Server
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
#     print(f"❌ Error connecting to SQL Server: {e}")
#     exit()

# # -----------------------------
# # Step 4: Insert Data (avoid duplicates)
# # -----------------------------
# for index, row in df.iterrows():
#     try:
#         # Optional: Check if SurveyID already exists to avoid duplicates
#         cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE SurveyID = ?", row['SurveyID'])
#         if cursor.fetchone()[0] == 0:
#             cursor.execute(f"""
#                 INSERT INTO {table} (SurveyID, Region, HouseholdSize, Income, EducationLevel, SubmissionDate, MaritalStatus)
#                 VALUES (?, ?, ?, ?, ?, ?, ?)
#             """, row['SurveyID'], row['Region'], row['HouseholdSize'], row['Income'],
#                  row['EducationLevel'], row['SubmissionDate'], row['MaritalStatus'])
#     except Exception as e:
#         print(f"❌ Error inserting row {index}: {e}")

# conn.commit()
# cursor.close()
# conn.close()
# print("✅ Data inserted into SQL Server successfully!")



import pandas as pd

# Path to your Excel file
excel_file = "C:/Users/HP/PythonClass/GBoS_Household_Survey_50.xlsx"
clean_file = "C:/Users/HP/PythonClass/GBoS_Household_Survey_50_Cleaned.xlsx"

# Read Excel
df = pd.read_excel(excel_file)

# Data Cleaning
df = df.dropna()  # Remove empty rows
df = df[df['HouseholdSize'] > 0]
df = df[df['Income'] > 0]

# Validate Regions
valid_regions = ['Banjul', 'Kanifing', 'Brikama', 'Kerewan', 'Mansakonko', 'Janjanbureh', 'Basse']
df = df[df['Region'].isin(valid_regions)]

# Validate Dates
df['SubmissionDate'] = pd.to_datetime(df['SubmissionDate'], errors='coerce')
df = df.dropna(subset=['SubmissionDate'])

# Save cleaned data
df.to_excel(clean_file, index=False)
print(f"✅ Cleaned Excel file saved at {clean_file}")
