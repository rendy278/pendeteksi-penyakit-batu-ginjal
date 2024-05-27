import streamlit as st 
from web_function import load_data 
from Tabs import home, predict, visualise

Tabs = {
    'Home': home,
    'Prediction': predict,
    'Visualisation': visualise
}

# Sidebar
st.sidebar.title('Navigasi')
# Radio button untuk navigasi halaman
page = st.sidebar.radio('Pages', list(Tabs.keys()))

# Load data
df, x, y = load_data()

# Panggil fungsi app untuk setiap halaman
if page in ['Prediction', 'Visualisation']:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()
