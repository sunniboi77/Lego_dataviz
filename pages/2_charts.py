from numpy import negative
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pdb
import plotly.express as px

sales = pd.read_csv("dataset/sales.csv", delimiter=";", index_col="year")
settheme = pd.read_csv("dataset/dfsettheme4.csv", delimiter=",")
allset = pd.read_csv("dataset/90allset.csv", delimiter=",")
import streamlit as st

if "show_fig6" not in st.session_state:
    st.session_state.show_fig6 = False

if "show_fig7" not in st.session_state:
    st.session_state.show_fig7 = False

st.session_state.show_fig6 = st.checkbox(
    "Show Treemap All", value=st.session_state.show_fig6
)

st.session_state.show_fig7 = st.checkbox(
    "Show Treemap by Year", value=st.session_state.show_fig7
)


@st.cache_data
def get_treemap_data1():
    """Generates data for treemap visualization (fig6)."""
    treemap_data1 = px.treemap(allset, path=["cat1", "cat2", "cat3"], values="set_num")
    treemap_data1.update_traces(
        hovertemplate="Sets: %{value}<br> %{label}<br><extra></extra>"
    )
    return treemap_data1


@st.cache_data
def get_treemap_data2():
    # code to generate data for treemap goes here
    treemap_data2 = px.treemap(
        allset, path=["year", "cat1", "cat2", "cat3"], values="set_num"
    )
    # treemap_data2.update_traces(marker=dict(line=dict(width=2, color="black")))
    treemap_data2.update_traces(
        hovertemplate="Sets: %{value}<br> %{label}<br><extra></extra>"
    )
    return treemap_data2


if st.session_state.show_fig6:
    fig6 = get_treemap_data1()
    st.write("fig6 goes here")
    st.plotly_chart(fig6)

if st.session_state.show_fig7:
    st.write("Treemap by year")
    try:
        fig7 = get_treemap_data2()
        st.plotly_chart(fig7)
    except Exception as e:
        st.write(f"An error occurred: {e}")
