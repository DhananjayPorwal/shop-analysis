# @Email:  dporwal985@gmail.com
# @Project:  Shop Analysis w/ Streamlit

# Libraries
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly
import streamlit as st  # pip install streamlit

# Page Title
st.set_page_config(page_title="Shop Analysis", page_icon="📊", layout="wide")


@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="DatabaseSample.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        usecols="B:R",
    )
    return df


df = get_data_from_excel()

# ---- Sidebar ----

st.sidebar.header("Please Filter Here:")
month = st.sidebar.multiselect(
    "Select the Month:",
    options=df["Month"].unique(),
    default=df["Month"].unique()
)

# payment,season,
payment_type = st.sidebar.multiselect(
    "Select the Payment Type:",
    options=df["Payment_Mode"].unique(),
    default=df["Payment_Mode"].unique()
)

season = st.sidebar.multiselect(
    "Select the Seasoned Sales:",
    options=df["Season"].unique(),
    default=df["Season"].unique(),
)

df_selection = df.query(
    "Month == @month & Payment_Mode == @payment_type & Season == @season"
)


# ---- Main Page ----

st.title("📊 Sales Dashboard")
st.markdown("##")

# Top KPI's
total_sales = int(df_selection["Total_Amount"].sum())
average_sale_by_transaction = round(
    df_selection["Total_Selling_Price"].mean(), 1)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Sales:")
    st.subheader("₹ " + str(total_sales))

with right_column:
    st.subheader("Average Sale by Transaction:")
    st.subheader("₹ " + str(average_sale_by_transaction))

st.markdown("---")

# *****Sales by Month [Bar Chart]*****

sales_by_month = (
    df_selection.groupby(by=["Month"]).sum()[
        ["Total_Selling_Price"]].sort_values(by="Total_Selling_Price")
)
fig_month_sales = px.bar(
    sales_by_month,
    x="Total_Selling_Price",
    y=sales_by_month.index,
    orientation="h",
    title="<b>Sales by Month</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_month),
    template="plotly_white"
)

# Make chart transparent
fig_month_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# *****Sales by Month [Line Chart]*****
fig_month_sales_line = px.line(
    sales_by_month,
    x="Total_Selling_Price",
    y=sales_by_month.index,
    orientation="h",
    title="<b>Sales by Month</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_month),
    template="plotly_white"
)

# Make chart transparent
fig_month_sales_line.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# Plot chart
left_column, right_column = st.columns(2)

left_column.plotly_chart(fig_month_sales, use_container_width=True)
right_column.plotly_chart(fig_month_sales_line, use_container_width=True)

# *****Payment Gateway [Pie Chart]*****
# payment_gateway = (

# *****Data Entry*****
st.subheader("Data Entry By Filter:")
st.dataframe(df_selection)

# ---- Hide Streamlit Style ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
