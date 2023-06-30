# Load the image URL

import streamlit as st


st.markdown("# On this page you can see an image of every major lego theme")

st.markdown(
    "#### The color of the bar indicates the number of sets within the given theme"
)


image_url = "dataset/img.png"

# Display the image
st.image(image_url)
