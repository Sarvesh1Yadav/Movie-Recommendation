import streamlit as st

# Define search criteria mapped to datasets
dataset_1_columns = ["Type", "Genre", "Premiere", "Watch Time"]
dataset_2_columns = ["Country", "Genre", "Type", "IMDb Rating", "Release Month"]

st.title("Movie Recommendation App")

# Inform users about the datasets
st.write("### Dataset Information:")
st.write("- **Dataset 1** contains: Type, Genre, Premiere, Watch Time")
st.write("- **Dataset 2** contains: Country, Genre, Type, IMDb Rating, Release Month")

st.write("### How would you like to get movie recommendations?")
search_by = st.selectbox("Select recommendation basis:", dataset_1_columns + dataset_2_columns)

if search_by in dataset_1_columns:
    st.page_link("Pages/app.py", label="Go to Dataset 1 App 📽️")

elif search_by in dataset_2_columns:
    st.page_link("Pages/app2.py", label="Go to Dataset 2 App 🎬")
