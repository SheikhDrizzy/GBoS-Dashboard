# # import streamlit as st
# # import pandas as pd
# # import pyodbc
# # import plotly.express as px

# # # # --- SQL Server Connection ---
# # # def load_data():
# # #     conn = pyodbc.connect(
# # #         "Driver={SQL Server};"
# # #         "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
# # #         "Database=GBoS_Surveys;"
# # #         "Trusted_Connection=yes;"
# # #     )
# # #     query = "SELECT TOP 100 * FROM HouseholdSurvey;"  # change table name if needed
# # #     df = pd.read_sql(query, conn)
# # #     conn.close()
# # #     return df

# # # # --- Streamlit App Layout ---
# # # st.set_page_config(page_title="GBOS Dashboard", layout="wide")
# # # st.title("📊 GBOS Sales Dashboard")

# # # df = load_data()

# # # st.subheader("Raw Data Preview")
# # # st.dataframe(df)

# # # # --- Example Chart ---
# # # if "total_profit" in df.columns and "region" in df.columns:
# # #     fig = px.bar(df, x="region", y="total_profit", title="Profit by Region")
# # #     st.plotly_chart(fig, use_container_width=True)
# # # else:
# # #     st.warning("Your table must have 'region' and 'total_profit' columns for the chart.")

# # import pyodbc
# # import pandas as pd

# # conn = pyodbc.connect(
# #     "Driver={SQL Server};"
# #     "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
# #     "Database=GBoS_Surveys;"
# #     "Trusted_Connection=yes;"
# # )
# # df = pd.read_sql("SELECT TOP 5 * FROM HouseholdSurvey;", conn)
# # conn.close()

# # print(df.columns)



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

# # --- Streamlit App Layout ---
# st.set_page_config(page_title="GBOS Dashboard", layout="wide")
# st.title("📊 GBOS Survey Dashboard")

# df = load_data()

# st.subheader("Raw Data Preview")
# st.dataframe(df)

# # --- Auto-detect numeric and categorical columns ---
# numeric_cols = df.select_dtypes(include='number').columns.tolist()
# categorical_cols = df.select_dtypes(include='object').columns.tolist()

# if numeric_cols and categorical_cols:
#     st.subheader("Automatic Charts by Categorical Column")
#     cat_col = st.selectbox("Select categorical column", categorical_cols)
    
#     for num_col in numeric_cols:
#         st.write(f"### {num_col} by {cat_col}")
#         fig = px.bar(df, x=cat_col, y=num_col, title=f"{num_col} by {cat_col}")
#         st.plotly_chart(fig, use_container_width=True)
# else:
#     st.warning("Table must have at least one numeric and one categorical column for plotting.")



import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

# --- SQL Server Connection ---
def load_data():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=SHEIKH-OUSMAN-H\\SQLEXPRESS;"
        "Database=GBoS_Surveys;"
        "Trusted_Connection=yes;"
    )
    df = pd.read_sql("SELECT TOP 100 * FROM HouseholdSurvey;", conn)
    conn.close()
    return df

# --- Load Data ---
df = load_data()

# --- Streamlit Layout ---
st.set_page_config(page_title="GBOS Survey Dashboard", layout="wide")
st.title("📊 GBOS Survey Dashboard")

# --- Show raw data ---
st.subheader("Raw Data Preview")
st.dataframe(df)

# --- Sidebar Controls for Interactivity ---
st.sidebar.header("Customize Your Dashboard")

# Categorical column selection
categorical_col = st.sidebar.selectbox(
    "Select categorical column", df.select_dtypes(include="object").columns
)

# Numeric column selection
numeric_col = st.sidebar.selectbox(
    "Select numeric column", df.select_dtypes(include="number").columns
)

# Color picker
chart_color = st.sidebar.color_picker("Pick chart color", "#00f900")

# Filter by categorical column values
unique_values = df[categorical_col].unique()
selected_values = st.sidebar.multiselect(
    f"Filter {categorical_col}", options=unique_values, default=unique_values
)
df_filtered = df[df[categorical_col].isin(selected_values)]

# --- Charts ---
st.subheader(f"Bar Chart: {numeric_col} by {categorical_col}")
fig_bar = px.bar(
    df_filtered,
    x=categorical_col,
    y=numeric_col,
    color_discrete_sequence=[chart_color],
    hover_data=df.columns
)
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader(f"Pie Chart: {categorical_col} Distribution")
fig_pie = px.pie(
    df_filtered,
    names=categorical_col,
    values=numeric_col,
    title=f"{numeric_col} Distribution by {categorical_col}",
    color_discrete_sequence=px.colors.sequential.RdBu
)
st.plotly_chart(fig_pie, use_container_width=True)


