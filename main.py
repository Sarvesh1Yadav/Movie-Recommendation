import streamlit as st

# Define the search options for each dataset
dataset_1_columns = ["Type", "Genre", "Premiere", "Watch Time"]
dataset_2_columns = ["Country", "Genre", "Type", "IMDb Rating", "Release Month"]

st.set_page_config(page_title="Movie Search App")

st.title("🎬 Movie Search App")

# Inform users about the datasets
st.write("### Dataset Information:")
st.write("- **Dataset 1** contains: Type, Genre, Premiere, Watch Time")
st.write("- **Dataset 2** contains: Country, Genre, Type, IMDb Rating, Release Month")

st.write("### How would you like to search for the movie?")
search_type = st.radio(
    "Select search basis from:",
    ("Dataset 1 (Type, Genre, Premiere, Watch Time)", "Dataset 2 (Country, Genre, Type, IMDb Rating, Release Month)")
)

if "Dataset 1" in search_type:
    
    
    st.page_link("pages/app.py", label="🔍 Go to Dataset 1 Search")

elif "Dataset 2" in search_type:
    
    st.page_link("pages/app2.py", label="🔍 Go to Dataset 2 Search")
