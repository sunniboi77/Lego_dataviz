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


# st.write(allset.head(3))
# st.write(settheme.head(3))


st.title("The LEGO Story in Data")
# st.subheader("A story by sunniboii")
st.write(
    ("My intention is to show the lego story and analyze similarities between sets")
)

st.title("Sales by year")
# Convert expenses column to absolute values
sales["expenses"] = sales["expenses"].abs()

# Sort by Year column
# sales = sales.sort_values(by='year')
sales = sales.sort_index()

# Create the plot
fig3, ax3 = plt.subplots()
sales[["revenue", "expenses", "netprofit"]].plot(
    kind="bar", stacked=True, figsize=(10, 6), ax=ax3
)
# Display the plot in Streamlit
st.pyplot(fig3)

# Create the first plot for sales data before 2004
fig1, ax1 = plt.subplots()
# pdb.set_trace()
sales_before_2004 = sales[sales.index < 2005]
# st.write(sales_before_2004)

sales_before_2004[["revenue", "expenses", "netprofit"]].plot(
    kind="bar", stacked=True, figsize=(10, 6), ax=ax1
)

# Display the first plot in Streamlit
st.pyplot(fig1)

# Create the second plot for sales data after 2004
fig2, ax2 = plt.subplots()
sales_after_2004 = sales[sales.index >= 2006]
sales_after_2004[["revenue", "expenses", "netprofit"]].plot(
    kind="bar", stacked=True, figsize=(10, 6), ax=ax2
)

# Display the second plot in Streamlit
st.pyplot(fig2)

# employee / year v1
colors = ["#4ea080", "#5eb698", "#6fccb1", "#80e2ca", "#92f9e4", "#ffffe0"]
ax4 = sales[["employees"]].plot(
    kind="bar",
    stacked=False,
    figsize=(10, 6),
    color=colors,
    title="Number of Employees and Net Profit by Year",
    rot=45,
)
fig4, ax4 = plt.subplots()

ax5 = ax4.twinx()
ax5.set_ylim(sales["revenue"].min(), sales["revenue"].max() * 1.1)
sales[["revenue"]].plot(ax=ax5, kind="line", color="red")

ax4.set_ylabel("Revenue")
st.pyplot(fig4)


# employee / year v2
fig4, ax4 = plt.subplots()
colors = ["#4ea080", "#5eb698", "#6fccb1", "#80e2ca", "#92f9e4", "#ffffe0"]
sales[["employees"]].plot(
    kind="bar",
    stacked=False,
    figsize=(10, 6),
    color=colors,
    title="Number of Employees and Net Profit by Year",
    rot=45,
    ax=ax4,
)
ax4.set_ylabel("Employees")


ax5 = ax4.twinx()
ax5.set_ylim(sales["revenue"].min(), sales["revenue"].max() * 1.1)
sales[["revenue"]].plot(ax=ax5, kind="line", color="red")

ax5.set_ylabel("Revenue")
st.pyplot(fig4)

# EMPREV EMPROF
# Get the revenue and employees
emprev = sales["emprev"]
emprof = sales["emprof"]


# Create a figure and an axes object
fig5, ax5 = plt.subplots()

# Plot the revenue
emprof.plot(ax=ax5, kind="line", label="Profit / Employee")

# Generate horizontal lines on ax5 dynamically based on the data
y_values = [
    0,
    round(sales["emprev"].max() / 2, -3),
    round(sales["emprev"].max() * 0.75, -3),
]  # Rounded y-values for horizontal lines
for y_value in y_values:
    ax5.axhline(y=y_value, color="gray", linestyle="--")


emprev.plot(ax=ax5, kind="line", label="Revenue / Employee", color="orange")

# Add a title and labels to the axes
ax5.set_title("Revenue and Profit / Employee")
ax5.set_xlabel("Year")
ax5.set_ylabel("Employee Number")

# Add a legend
ax5.legend()
# Show the plot
st.pyplot(fig5)
