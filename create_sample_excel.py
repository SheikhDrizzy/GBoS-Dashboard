# import pandas as pd

# # -----------------------------
# # Correct 50-row dataset
# # -----------------------------
# regions = ["Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse"]
# regions = (regions * 8)[:50]  # repeat to make exactly 50 values

# household_size = [4,6,5,3,7,4,5,2,8,3,6,4,5,3,7,4,5,2,6,3,5,4,7,3,5,4,6,3,5,4,6,3,5,4,7,4,5,2,6,3,5,4,6,3,5,4,7,4,5,3]
# income = [25000,35000,28000,22000,40000,27000,30000,18000,45000,20000,
#           35000,26000,32000,21000,40000,27000,30000,19000,36000,22000,
#           31000,25000,42000,20000,30000,27000,38000,21000,31000,26000,
#           34000,21000,32000,27000,41000,28000,30000,18000,36000,22000,
#           33000,27000,38000,21000,31000,26000,42000,27000,30000,20000]
# education_level = ["Secondary","Tertiary","Primary","Secondary","None","Secondary","Primary",
#                    "Tertiary","Secondary","Primary","Tertiary","Secondary","Primary","Tertiary",
#                    "Secondary","Primary","Tertiary","Secondary","Primary","Tertiary",
#                    "Secondary","Primary","Tertiary","Secondary","Primary","Tertiary","Secondary",
#                    "Primary","Tertiary","Secondary","Primary","Tertiary","Secondary","Primary",
#                    "Tertiary","Secondary","Primary","Tertiary","Secondary","Primary","Tertiary",
#                    "Secondary","Primary","Tertiary","Secondary","Primary","Tertiary","Secondary",
#                    "Primary","Tertiary","Secondary"]
# submission_date = pd.date_range(start="2025-09-01", periods=50, freq='D')
# marital_status = ["Married","Married","Single","Married","Married","Single","Married",
#                   "Single","Married","Single","Married","Single","Married","Single",
#                   "Married","Single","Married","Single","Married","Single","Married","Single",
#                   "Married","Single","Married","Single","Married","Single","Married","Single",
#                   "Married","Single","Married","Single","Married","Single","Married","Single",
#                   "Married","Single","Married","Single","Married","Single","Married","Single",
#                   "Married","Single"]
# status = ["Pending"]*50

# # Create DataFrame
# df = pd.DataFrame({
#     "SurveyID": list(range(1, 51)),
#     "Region": regions,
#     "HouseholdSize": household_size,
#     "Income": income,
#     "EducationLevel": education_level,
#     "SubmissionDate": submission_date,
#     "MaritalStatus": marital_status,
#     "Status": status
# })

# # Save Excel file
# file_path = "C:/Users/HP/PythonClass/GBoS_Household_Survey_50.xlsx"
# df.to_excel(file_path, index=False)

# print(f"✅ Excel file created at {file_path}")


import pandas as pd
import numpy as np

# -----------------------------
# Number of rows
# -----------------------------
n_rows = 50

# -----------------------------
# Generate columns dynamically
# -----------------------------
survey_ids = list(range(1, n_rows + 1))

regions = ["Banjul","Kanifing","Brikama","Kerewan","Mansakonko","Janjanbureh","Basse"]
regions = [regions[i % len(regions)] for i in range(n_rows)]  # repeats to fill 50

household_size = np.random.randint(1, 9, size=n_rows)  # 1 to 8 members
income = np.random.randint(15000, 50001, size=n_rows)   # 15k to 50k
education_levels = ["None","Primary","Secondary","Tertiary"]
education_level = [education_levels[i % len(education_levels)] for i in range(n_rows)]
submission_date = pd.date_range(start="2025-09-01", periods=n_rows, freq='D')
marital_status_options = ["Single","Married"]
marital_status = [marital_status_options[i % len(marital_status_options)] for i in range(n_rows)]
status = ["Pending"] * n_rows

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame({
    "SurveyID": survey_ids,
    "Region": regions,
    "HouseholdSize": household_size,
    "Income": income,
    "EducationLevel": education_level,
    "SubmissionDate": submission_date,
    "MaritalStatus": marital_status,
    "Status": status
})

# -----------------------------
# Save to Excel
# -----------------------------
file_path = "C:/Users/HP/PythonClass/GBoS_Household_Survey_50.xlsx"
df.to_excel(file_path, index=False)

print(f"✅ Excel file created at {file_path} with {len(df)} rows")
