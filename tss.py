import streamlit as st
st.set_page_config(page_icon=" :bar_chart:",page_title="Visualizations",layout="wide")
css="""
    <style>
    div.block-container {
        padding-top:1rem;
        text-align: center;
    .custom-text {
        color: #C16F56 !important; /* Change the color to your desired color */
    }
    .custom-text a {
        color: #C16F56 !important; /* Change the color to your desired color */
        text-decoration: none !important; /* Remove the underline */
    }
"""
st.markdown(css,unsafe_allow_html=True)
st.title(":chart_with_downwards_trend: Telecom Customer churn  ")


st.write('<span class="custom-text">Data source: <a class="custom-text" href="https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input" target="_blank"> https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input</a></span>', unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")

#'<span class="custom-text">This text has a custom color.</span>', unsafe_allow_html=True
df=pd.read_csv("https://raw.githubusercontent.com/AbeerDib/Final/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")
st.subheader("1-Interactive dataframe ")
col1,col2=st.columns([1.3,1])
with col2:
    rows = st.slider('Select the range of rows you want to see', 
                    min_value=1,max_value= len(df),value=(1, 5),step=1)
with col1:
    selected_columns1 = st.multiselect(
        "Select Columns:",
        df.columns,
        default=["gender","SeniorCitizen","Contract","Churn"]
    )
sliced_df = df.iloc[rows[0] :rows[1], :][selected_columns1]
# Display the sliced DataFrame as a table
st.write("")
st.write("")
st.write("Selected Data:")
st.dataframe(sliced_df)
 

#df.loc[rows]
#filtered_df=df[(df['Value'] >= rows[0]) & (df['Value'] <= rows[1])]
#filtered_df
st.write("")
st.write("")
st.write("")
