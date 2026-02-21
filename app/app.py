import streamlit as st
import pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="AgriLogistics Premium | Yield AI", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")
st.markdown("<style>body { font-family: 'Outfit', sans-serif; background-color: #0f172a; }</style>", unsafe_allow_html=True)
st.title("Intelligent Crop Yield Prediction System 🌾")
st.sidebar.title("AgriAI")
nav = st.sidebar.radio("Navigation", ["🏠 Overview", "🎯 Make a Prediction", "📈 Model Evaluation", "📖 Architecture & Explanation"])

if nav == "🎯 Make a Prediction":
    st.header("🎯 Prediction Engine")
    uploaded = st.file_uploader("Drop your CSV data here", type=["csv"])
    if uploaded:
        st.success("Data uploaded successfully!")
