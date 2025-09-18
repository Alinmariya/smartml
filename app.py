import streamlit as st
import pandas as pd
from ml_utils import data_processing, eda, feature_engineering, model_builder, model_evaluation

st.title("SmartML Pro 🚀")
st.write("Upload a dataset and build ML models instantly!")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview Data")
    st.dataframe(df.head())
else:
    st.info("Upload a dataset to begin.")
