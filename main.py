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
    if st.button("Proceed"):
        st.switch_page("Pages/app.py")  # Navigates to app.py without opening a new tab

elif search_by in dataset_2_columns:
    if st.button("Proceed"):
        st.switch_page("Pages/app2.py")  # Navigates to app2.py without opening a new tab
