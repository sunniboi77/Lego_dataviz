import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

import matplotlib


creator = pd.read_csv("dataset/creator_104.csv", delimiter=",")
creatorpivot = pd.read_csv("dataset/creatorpivot_105.csv", delimiter=",")


st.write("CREATOR")

# st.write(creator.head(3))

st.write(
    "Creator sets are 20 years old, I have clusterized the sets, but it would have been be able to do it with pd.cut as well"
)
st.write("the sets are clustered based on the number of items they contain")
st.write("After 2005 Lego changed its strategy")

# Display a boxplot for clusters using Plotly
fig = px.box(creator, x="Cluster", y="num_parts")
st.plotly_chart(fig)


import seaborn as sns
import matplotlib.pyplot as plt

# Create a separate plot for each cluster
clusters = creator["Cluster"].unique()
num_clusters = len(clusters)

plt.figure(figsize=(15, 5 * num_clusters))  # Adjust the figure size as needed

for i, cluster in enumerate(clusters):
    cluster_data = creatorpivot[creatorpivot["Cluster"] == cluster]

    ax = plt.subplot(num_clusters, 1, i + 1)
    sns.lineplot(data=cluster_data, x="year", y="mean_num_parts")

    plt.xlabel("Year")
    plt.ylabel("mean_num_parts")
    plt.title(f"Cluster {cluster}")
    plt.tight_layout()

plt.show()


# # Create a separate plot for each cluster
# clusters = creator["Cluster"].unique()
# num_clusters = len(clusters)

# fig, axs = plt.subplots(
#     num_clusters, 1, figsize=(15, 5 * num_clusters)
# )  # Adjust the figure size as needed

# for i, cluster in enumerate(clusters):
#     cluster_data = creatorpivot[creatorpivot["Cluster"] == cluster]

#     ax = axs[i]
#     sns.lineplot(data=cluster_data, x="year", y="mean_num_parts", ax=ax)

#     ax.set_xlabel("Year", fontsize=14)
#     ax.set_ylabel("mean_num_parts", fontsize=14)
#     ax.set_title(f"Cluster {cluster}", fontsize=16)
#     ax.tick_params(labelsize=12)

# fig.suptitle("Average Part Number in Creator Clusters", fontsize=45)
# plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the top parameter as needed
# st.pyplot(fig)


##### bar and line plot
# Create a separate plot for each cluster
clusters = creator["Cluster"].unique()
num_clusters = len(clusters)

fig, axs = plt.subplots(
    num_clusters * 2, 1, figsize=(15, 5 * num_clusters * 2)
)  # Adjust the figure size as needed

for i, cluster in enumerate(clusters):
    cluster_data = creatorpivot[creatorpivot["Cluster"] == cluster]

    # Create the line plot
    ax1 = axs[i * 2]
    sns.lineplot(data=cluster_data, x="year", y="mean_num_parts", ax=ax1)
    ax1.set_xlabel("Year", fontsize=14)
    ax1.set_ylabel("mean_num_parts", fontsize=20)
    ax1.set_title(f"Cluster {cluster}", fontsize=20)
    ax1.tick_params(labelsize=14)

    # Create the bar plot
    ax2 = axs[i * 2 + 1]
    sns.barplot(data=cluster_data, x="year", y="count_sets", ax=ax2)
    ax2.set_xlabel("Year", fontsize=20)
    ax2.set_ylabel("count_sets", fontsize=20)
    ax2.tick_params(labelsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the top parameter as needed
st.pyplot(fig)
