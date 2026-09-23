import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Set up the page title and layout
st.set_page_config(page_title="My Excel Dashboard", layout="wide")
st.title("📊 Dynamic Excel Dashboard")

# 2. Create a file uploader widget
uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])

# 3. Only run the dashboard logic if a file is uploaded
if uploaded_file is not None:
    # Read the Excel sheet into a Pandas DataFrame
    df = pd.read_excel(uploaded_file)

    # Show a preview of the raw data
    st.subheader("Data Preview")
    st.dataframe(df, use_container_width=True)

    st.divider()
    st.subheader("Visualize Your Data")

    # Get all column names from the uploaded sheet
    columns = df.columns.tolist()

    # 4. Create two dropdown menus side-by-side for the user to select chart axes
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Select data for X-axis:", columns)
    with col2:
        y_axis = st.selectbox("Select data for Y-axis:", columns)

    # 5. Generate and display the charts automatically based on selection
    if x_axis and y_axis:
        # Create tabs for different chart types
        tab1, tab2, tab3 = st.tabs(["Bar Chart", "Line Chart", "Scatter Plot"])

        with tab1:
            fig_bar = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
            st.plotly_chart(fig_bar, use_container_width=True)

        with tab2:
            fig_line = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} over {x_axis}")
            st.plotly_chart(fig_line, use_container_width=True)

        with tab3:
            fig_scatter = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
            st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.info("Awaiting file upload. Please upload an Excel sheet to begin.")