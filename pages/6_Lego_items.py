import streamlit as st
import pandas as pd
import plotly.express as px

part_num_yearly = pd.read_csv("dataset/num_part106_from14.csv", delimiter=",")
sets_yearly = pd.read_csv("dataset/set_yearly_108.csv", delimiter=",")

st.markdown("# This page is all about lego items")

st.markdown("#### https://factourism.com/facts/lego-combinations/")


st.write(
    "#### Main : Lego own themes, Licensed : Mostly Disney and from it Star Wars"
    "Licensed Game : Minecraft but not only, Licensed : Mostly Disney and within Disney it is mostly Star Wars theme    "
)

# Chart1
# Create a pivot table to prepare data for the stacked bar plot
pivot_table = pd.pivot_table(
    sets_yearly, values="set_num", index="year", columns="cat1", aggfunc="sum"
)

# Reset the index of the pivot table
pivot_table = pivot_table.reset_index()

# Create the stacked bar plot using Plotly Express
stacked_bar_fig = px.bar(
    pivot_table,
    x="year",
    y=pivot_table.columns[1:],
    title="Number of sets by year and colors within bar indicate Categories",
    barmode="stack",
)

# Position the legend on the graph
stacked_bar_fig.update_layout(
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

# Set the x-axis label
stacked_bar_fig.update_xaxes(title="Year")

# Set the y-axis label
stacked_bar_fig.update_yaxes(title="Set Num")

# Set the font size of the title
stacked_bar_fig.update_layout(title_font_size=24)

# Display the stacked bar plot using Streamlit
st.plotly_chart(stacked_bar_fig)

######################

st.title("Lego New Item Numbers / Decade")

decade_grouped = part_num_yearly.groupby("decade")["part_num"].sum()
decade_grouped = decade_grouped.reset_index()

year5grouped = part_num_yearly.groupby("5year")["part_num"].sum()
year5grouped = year5grouped.reset_index()

# PLOT
# Group the data by decade and calculate the sum of the part_num column
decade_grouped = part_num_yearly.groupby("decade")["part_num"].sum()
decade_grouped = decade_grouped.reset_index()

# Create a bar chart using Streamlit
bar_chart_fig = st.bar_chart(decade_grouped.set_index("decade"))

##### chart 3
st.title("Lego New Item Numbers / in every 5 year")

st.bar_chart(year5grouped.set_index("5year"))

################ Chart 4 Treemap
treemap_fig = px.treemap(part_num_yearly, path=["decade", "name"], values="part_num")
treemap_fig.update_layout(title="Number of new parts in every Decade")

# Set the font size of the title
treemap_fig.update_layout(title_font_size=24)

# Display the treemap using Streamlit
st.plotly_chart(treemap_fig)


################ Chart 5 Treemap


part_num_yearly2 = part_num_yearly[
    ~part_num_yearly["name"].str.contains(
        "stickers|minifig|Duplo|Figures|Non", case=False
    )
]

st.markdown("####    Number of new parts in every Decade without stickers and non-lego")
treemap_fig = px.treemap(part_num_yearly2, path=["decade", "name"], values="part_num")
treemap_fig.update_layout(title="Without stickers and non-lego")

# Set the font size of the title
treemap_fig.update_layout(title_font_size=24)

# Display the treemap using Streamlit
st.plotly_chart(treemap_fig)
