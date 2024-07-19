import streamlit as st
import pandas as pd

# Load data
database_df = pd.read_csv('database.csv')

# Title
st.title('Nella mia valigia 🧳')

# Sidebar for activity selection
activities = database_df['category'].unique()
selected_activities = st.sidebar.multiselect('Seleziona le attività', activities)

# Filter items based on selected activities
filtered_df = database_df[database_df['category'].isin(selected_activities)]

# Extract unique items
unique_items = filtered_df['item'].drop_duplicates().sort_values()

# Display checklist with options to mark items as taken or not taken
if len(unique_items) > 0:
    st.write('## Packing List')
    for item in unique_items:
        cols = st.columns([3, 1])
        item_html = f"<span style='font-size:20px; font-weight:bold;'>{item}</span>"
        cols[0].markdown(item_html, unsafe_allow_html=True)
        cols[1].radio("", ['Non ancora', 'Preso','Non lo voglio'], key=item)
else:
    st.write('Selezionare le attività per vedere l\'elenco dei bagagli e andare all\'avventura 🤠')
