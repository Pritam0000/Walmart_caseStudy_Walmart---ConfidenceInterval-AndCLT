import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data
from data_processor import process_data
from visualizations import create_visualizations
from confidence_intervals import calculate_confidence_intervals

def main():
    st.title("Walmart Black Friday Sales Analysis")

    # Load and process data
    df = load_data()
    processed_df = process_data(df)

    # Display basic statistics
    st.header("Basic Statistics")
    st.write(processed_df.describe())

    # Display visualizations
    st.header("Visualizations")
    figs = create_visualizations(processed_df)
    for fig in figs:
        st.pyplot(fig)

    # Display confidence intervals
    st.header("Confidence Intervals")
    ci_results = calculate_confidence_intervals(processed_df)
    st.write(ci_results)

if __name__ == "__main__":
    main()