import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- SETTINGS ---
st.set_page_config(page_title="Inflation Dashboard", layout="wide")

# --- LOAD DATA ---
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()  # Clean column names

# --- TITLE ---
st.title("Inflation & Price Trend Dashboard")
st.markdown("Visualizing Dollar Rate, Petrol Price, Grocery Prices & Inflation over the years.")

# --- STYLE ---
st.markdown("---")

# --- PLOTTING FUNCTION ---
def make_chart(column, color, ylabel):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Year"], df[column], marker='o', color=color)
    ax.set_title(f"{column} Over Time", fontsize=14)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    return fig

# --- CHARTS ---
col1, col2 = st.columns(2)
with col1:
    st.pyplot(make_chart("Dollar Rate", "#1f77b4", "PKR"))
with col2:
    st.pyplot(make_chart("Petrol Price", "#2ca02c", "PKR"))

col3, col4 = st.columns(2)
with col3:
    st.pyplot(make_chart("Grocery Prices", "#d62728", "PKR"))
with col4:
    st.pyplot(make_chart("Inflation", "#ff7f0e", "Percent"))

# --- FOOTER ---
st.markdown("---")
st.caption("Data Source: Simulated Data for Educational and Dashboard Demonstration")
st.markdown("Created by Abdul Moiz - [GitHub](https://github.com/AMK-DSAI25)")
# --- END OF DASHBOARD ---