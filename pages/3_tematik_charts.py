import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

import matplotlib

cat1byyear = pd.read_csv(
    "dataset/100_cat1_numparts_sum_mean_year.csv", delimiter=",", index_col="index"
)

setthemesets_year = pd.read_csv("dataset/101_setthemesets_year.csv", delimiter=",")
stacked_data102 = pd.read_csv("dataset/stacked_data102.csv", delimiter=",")
tema_103 = pd.read_csv("dataset/tema_103.csv", delimiter=",")
# Load the image URL


st.write(setthemesets_year.head(3))

st.write("hello")


# Set the figure size and create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate the cumulative sum of 'set_num' for each 'year' and 'cat1'
stacked_data = (
    setthemesets_year.groupby(["year", "cat1"])["set_num"].sum().unstack().cumsum()
)

# Plot the stacked area chart
stacked_data.plot.area(ax=ax, stacked=True)

# Set the plot title and labels
ax.set_title("Lego sets year by year")
ax.set_xlabel("Year")
ax.set_ylabel("Sum of set_num")

# Add a legend
ax.legend(title="cat1")

# Display the plot
st.pyplot(fig)


def drawfunct(sumormean):
    fig = px.line(
        data_frame=cat1byyear,
        x="year",
        y=sumormean,
        color="cat1",
        title=f"Line Plot of {sumormean.capitalize()} Part Size of sets by Year",
    )

    # Add a hover interaction that changes the thickness of a line when you hover over its corresponding legend entry
    for trace in fig.data:
        trace.hovertemplate = f"<b>{trace.name}</b><br>{sumormean.capitalize()}: %{{y}}"
        trace.on_hover(lambda trace, points, state: trace.update(line={"width": 5}))
        trace.on_unhover(lambda trace, points, state: trace.update(line={"width": 1}))

    # Update the position of the legend
    fig.update_layout(
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="left", x=0)
    )
    st.plotly_chart(fig)


# Example usage
drawfunct("mean")

#### tema103

# Define the bins for colorization
bins = [0, 10, 50, 100, 500, 1000, 1900]
bin_labels = ["<10", "20-50", "50-100", "100-500", "500-1000", "1000+"]

# Example usage
drawfunct("sum")

# Load the image URL
image_url = "dataset/img.png"

# Display the image
st.image(image_url)
