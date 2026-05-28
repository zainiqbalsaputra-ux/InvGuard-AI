import streamlit as st

def run_dashboard():
    st.set_page_config(
        page_title="InvGuard AI",
        layout="wide"
    )

    st.title("🚦 InvGuard AI Dashboard")
    st.write("AI-powered traffic monitoring system")