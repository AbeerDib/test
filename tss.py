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
