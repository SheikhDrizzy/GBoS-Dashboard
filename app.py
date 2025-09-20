# # # import streamlit as st
# # # import pandas as pd
# # # import pyodbc
# # # import plotly.express as px

# # # # # --- SQL Server Connection ---
# # # # def load_data():
# # # #     conn = pyodbc.connect(
# # # #         "Driver={SQL Server};"
# # # #         "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
# # # #         "Database=GBoS_Surveys;"
# # # #         "Trusted_Connection=yes;"
# # # #     )
# # # #     query = "SELECT TOP 100 * FROM HouseholdSurvey;"  # change table name if needed
# # # #     df = pd.read_sql(query, conn)
# # # #     conn.close()
# # # #     return df

# # # # # --- Streamlit App Layout ---
# # # # st.set_page_config(page_title="GBOS Dashboard", layout="wide")
# # # # st.title("📊 GBOS Sales Dashboard")

# # # # df = load_data()

# # # # st.subheader("Raw Data Preview")
# # # # st.dataframe(df)

# # # # # --- Example Chart ---
# # # # if "total_profit" in df.columns and "region" in df.columns:
# # # #     fig = px.bar(df, x="region", y="total_profit", title="Profit by Region")
# # # #     st.plotly_chart(fig, use_container_width=True)
# # # # else:
# # # #     st.warning("Your table must have 'region' and 'total_profit' columns for the chart.")

# # # import pyodbc
# # # import pandas as pd

# # # conn = pyodbc.connect(
# # #     "Driver={SQL Server};"
# # #     "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
# # #     "Database=GBoS_Surveys;"
# # #     "Trusted_Connection=yes;"
# # # )
# # # df = pd.read_sql("SELECT TOP 5 * FROM HouseholdSurvey;", conn)
# # # conn.close()

# # # print(df.columns)



# # import streamlit as st
# # import pandas as pd
# # import pyodbc
# # import plotly.express as px

# # # --- SQL Server Connection ---
# # def load_data():
# #     conn = pyodbc.connect(
# #         "Driver={SQL Server};"
# #         "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
# #         "Database=GBoS_Surveys;"
# #         "Trusted_Connection=yes;"
# #     )
# #     df = pd.read_sql("SELECT TOP 100 * FROM HouseholdSurvey;", conn)
# #     conn.close()
# #     return df

# # # --- Streamlit App Layout ---
# # st.set_page_config(page_title="GBOS Dashboard", layout="wide")
# # st.title("📊 GBOS Survey Dashboard")

# # df = load_data()

# # st.subheader("Raw Data Preview")
# # st.dataframe(df)

# # # --- Auto-detect numeric and categorical columns ---
# # numeric_cols = df.select_dtypes(include='number').columns.tolist()
# # categorical_cols = df.select_dtypes(include='object').columns.tolist()

# # if numeric_cols and categorical_cols:
# #     st.subheader("Automatic Charts by Categorical Column")
# #     cat_col = st.selectbox("Select categorical column", categorical_cols)
    
# #     for num_col in numeric_cols:
# #         st.write(f"### {num_col} by {cat_col}")
# #         fig = px.bar(df, x=cat_col, y=num_col, title=f"{num_col} by {cat_col}")
# #         st.plotly_chart(fig, use_container_width=True)
# # else:
# #     st.warning("Table must have at least one numeric and one categorical column for plotting.")



# import streamlit as st
# import pandas as pd
# import pyodbc
# import plotly.express as px

# # --- SQL Server Connection ---
# def load_data():
#     conn = pyodbc.connect(
#         "Driver={SQL Server};"
#         "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
#         "Database=GBoS_Surveys;"
#         "Trusted_Connection=yes;"
#     )
#     df = pd.read_sql("SELECT TOP 100 * FROM HouseholdSurvey;", conn)
#     conn.close()
#     return df

# # --- Load Data ---
# df = load_data()

# # --- Streamlit Layout ---
# st.set_page_config(page_title="GBOS Survey Dashboard", layout="wide")
# st.title("📊 GBOS Survey Dashboard")

# # --- Show raw data ---
# st.subheader("Raw Data Preview")
# st.dataframe(df)

# # --- Sidebar Controls for Interactivity ---
# st.sidebar.header("Customize Your Dashboard")

# # Categorical column selection
# categorical_col = st.sidebar.selectbox(
#     "Select categorical column", df.select_dtypes(include="object").columns
# )

# # Numeric column selection
# numeric_col = st.sidebar.selectbox(
#     "Select numeric column", df.select_dtypes(include="number").columns
# )

# # Color picker
# chart_color = st.sidebar.color_picker("Pick chart color", "#00f900")

# # Filter by categorical column values
# unique_values = df[categorical_col].unique()
# selected_values = st.sidebar.multiselect(
#     f"Filter {categorical_col}", options=unique_values, default=unique_values
# )
# df_filtered = df[df[categorical_col].isin(selected_values)]

# # --- Charts ---
# st.subheader(f"Bar Chart: {numeric_col} by {categorical_col}")
# fig_bar = px.bar(
#     df_filtered,
#     x=categorical_col,
#     y=numeric_col,
#     color_discrete_sequence=[chart_color],
#     hover_data=df.columns
# )
# st.plotly_chart(fig_bar, use_container_width=True)

# st.subheader(f"Pie Chart: {categorical_col} Distribution")
# fig_pie = px.pie(
#     df_filtered,
#     names=categorical_col,
#     values=numeric_col,
#     title=f"{numeric_col} Distribution by {categorical_col}",
#     color_discrete_sequence=px.colors.sequential.RdBu
# )
# st.plotly_chart(fig_pie, use_container_width=True)
# fig = px.bar(df, x="Region", y="Income", color="Income", color_continuous_scale=px.colors.sequential.Viridis)
# st.plotly_chart(fig)


# st.subheader("➕ Add New Survey Entry")

# # Form to input new survey data
# with st.form("survey_form"):
#     region = st.text_input("Region")
#     household_size = st.number_input("Household Size", min_value=1, step=1)
#     income = st.number_input("Income", min_value=0)
#     education = st.text_input("Education Level")
#     submission_date = st.date_input("Submission Date")
#     marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
    
#     submitted = st.form_submit_button("Add Survey")

#     if submitted:
#         try:
#             # Connect to SQL Server
#             conn = pyodbc.connect(
#                 "Driver={SQL Server};"
#                 "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
#                 "Database=GBoS_Surveys;"
#                 "Trusted_Connection=yes;"
#             )
#             cursor = conn.cursor()
            
#             # Insert new survey
#             cursor.execute("""
#                 INSERT INTO HouseholdSurvey (Region, HouseholdSize, Income, EducationLevel, SubmissionDate, MaritalStatus)
#                 VALUES (?, ?, ?, ?, ?, ?)
#             """, (region, household_size, income, education, submission_date, marital_status))
            
#             conn.commit()
#             conn.close()
            
#             st.success("✅ New survey added successfully!")
            
#             # Refresh data in the dashboard
#             df = load_data()
#             st.dataframe(df)

#         except Exception as e:
#             st.error(f"❌ Error adding survey: {e}")



##ACTUAL CODES 

import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px
from datetime import datetime

# --- SQL Server Connection ---
def load_data():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
        "Database=GBoS_Surveys;"
        "Trusted_Connection=yes;"
    )
    query = "SELECT * FROM HouseholdSurvey;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# --- Streamlit App Layout ---
st.set_page_config(page_title="GBOS Survey Dashboard", layout="wide")
st.title("📊 GBOS Survey Dashboard")

# Load existing data
df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
selected_region = st.sidebar.multiselect("Region", options=df["Region"].unique(), default=df["Region"].unique())
selected_education = st.sidebar.multiselect("Education Level", options=df["EducationLevel"].unique(), default=df["EducationLevel"].unique())
selected_marital = st.sidebar.multiselect("Marital Status", options=df["MaritalStatus"].unique(), default=df["MaritalStatus"].unique())

# Apply filters
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["EducationLevel"].isin(selected_education)) &
    (df["MaritalStatus"].isin(selected_marital))
]

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)


# --- Interactive Charts ---
st.subheader("📈 Charts")

# 1. Categorical distribution
categorical_cols = ["Region", "EducationLevel", "MaritalStatus"]
selected_col = st.selectbox("Select categorical column for distribution chart", categorical_cols)
fig1 = px.histogram(filtered_df, x=selected_col, color=selected_col,
                    title=f"Distribution by {selected_col}", 
                    color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig1, use_container_width=True)

# 2. Numeric summary: Income or HouseholdSize by Region
numeric_col = st.selectbox("Select numeric column for summary chart", ["Income", "HouseholdSize"])
fig2 = px.bar(filtered_df, x="Region", y=numeric_col, color="Region",
              title=f"{numeric_col} by Region", color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig2, use_container_width=True)

# 3. Trend over time
if "SubmissionDate" in filtered_df.columns:
    filtered_df["SubmissionDate"] = pd.to_datetime(filtered_df["SubmissionDate"])
    fig3 = px.line(filtered_df, x="SubmissionDate", y=numeric_col, color="Region",
                   title=f"{numeric_col} Trend Over Time", markers=True,
                   color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig3, use_container_width=True)

# --- Add New Survey Entry ---
st.subheader("➕ Add New Survey Entry")
with st.form("survey_form"):
    region = st.selectbox("Region", ["Kanifing", "Banjul", "Brikama", "Serekunda", "Other"])
    household_size = st.number_input("Household Size", min_value=1, step=1)
    income = st.number_input("Income", min_value=0, step=100)
    education = st.selectbox("Education Level", ["None", "Primary", "Secondary", "Tertiary"])
    submission_date = st.date_input("Submission Date", datetime.today())
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
    
    submitted = st.form_submit_button("Add Survey")
    if submitted:
        try:
            conn = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
                "Database=GBoS_Surveys;"
                "Trusted_Connection=yes;"
            )
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO HouseholdSurvey 
                (Region, HouseholdSize, Income, EducationLevel, SubmissionDate, MaritalStatus)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (region, household_size, income, education, submission_date, marital_status))
            conn.commit()
            conn.close()
            st.success("✅ New survey added successfully!")
            df = load_data()
            filtered_df = df  # Refresh filtered view
        except Exception as e:
            st.error(f"❌ Error adding survey: {e}")


