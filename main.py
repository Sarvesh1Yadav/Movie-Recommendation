import streamlit as st
import subprocess

# Define the search options for each dataset
dataset_1_columns = ["Type", "Genre", "Premiere", "Watch Time"]
dataset_2_columns = ["Country", "Genre", "Type", "IMDb Rating", "Release Month"]

st.title("Movie Search App")

# Inform users about the datasets
st.write("### Dataset Information:")
st.write("- **Dataset 1** contains: Type, Genre, Premiere, Watch Time")
st.write("- **Dataset 2** contains: Country, Genre, Type, IMDb Rating, Release Month")

st.write("### How would you like to search for the movie?")
search_type = st.radio("Select search basis from:", ("Dataset 1 (Type, Genre, Premiere, Watch Time)", 
                                                      "Dataset 2 (Country, Genre, Type, IMDb Rating, Release Month)"))

if "Dataset 1" in search_type:
    # search_by = st.selectbox("Search by:", dataset_1_columns)
    if st.button("Proceed"):
        st.write(f"Launching app for your recommendation...")
        subprocess.run(["streamlit", "run", "app.py"])

elif "Dataset 2" in search_type:
    # search_by = st.selectbox("Search by:", dataset_2_columns)
    if st.button("Proceed"):
        st.write(f"Launching app for your recommendation...")
        subprocess.run(["streamlit", "run", "app2.py"])
