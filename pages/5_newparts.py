import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import matplotlib
import plotly.express as px

part_num_yearly = pd.read_csv("dataset/num_part106_from14.csv", delimiter=",")
sets_yearly = pd.read_csv("dataset/set_yearly_108.csv", delimiter=",")


st.write("This page is all about lego items")


# Create a pivot table to prepare data for the stacked bar plot
pivot_table = pd.pivot_table(
    sets_yearly, values="set_num", index="year", columns="cat1", aggfunc="sum"
)

# Reset the index of the pivot table
pivot_table = pivot_table.reset_index()

# Create the stacked bar plot using Plotly Express
fig = px.bar(
    pivot_table,
    x="year",
    y=pivot_table.columns[1:],
    title="Stacked Bar Plot - Set Num by Year and Cat1",
    barmode="stack",
)

# Position the legend on the graph
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))


# Display the available options for legend position
print(fig.layout.legend)

# Set the x-axis label
fig.update_xaxes(title="Year")

# Set the y-axis label
fig.update_yaxes(title="Set Num")

# Display the stacked bar plot using Streamlit
st.plotly_chart(fig)


######################

st.write(sets_yearly.head(3))
st.title("Lego New Item Numbers / Decade")

decade_grouped = part_num_yearly.groupby("decade")["part_num"].sum()
decade_grouped = decade_grouped.reset_index()
# st.write(decade_grouped)

year5grouped = part_num_yearly.groupby("5year")["part_num"].sum()
year5grouped = year5grouped.reset_index()

# PLOT
# Group the data by decade and calculate the sum of the part_num column
decade_grouped = part_num_yearly.groupby("decade")["part_num"].sum()
decade_grouped = decade_grouped.reset_index()

# # Display the grouped data
# st.write(decade_grouped)

# Create a bar chart using the grouped data
st.bar_chart(decade_grouped.set_index("decade"))

st.title("Lego New Item Numbers / in every 5 year")


st.bar_chart(year5grouped.set_index("5year"))


################

fig = px.treemap(part_num_yearly, path=["decade", "name"], values="part_num")

# Display the treemap using Streamlit
st.plotly_chart(fig)

#########################
