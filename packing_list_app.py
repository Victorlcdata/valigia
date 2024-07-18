import streamlit as st
import pandas as pd

# Load data
database_df = pd.read_csv('database.csv')

# Title
st.title('Activity Packing List')

# Sidebar for activity selection
activities = database_df['category'].unique()
selected_activities = st.sidebar.multiselect('Select Activities', activities)

# Filter items based on selected activities
filtered_df = database_df[database_df['category'].isin(selected_activities)]

# Extract unique items
unique_items = filtered_df['item'].drop_duplicates().sort_values()

# Display checklist with options to mark items as taken or not taken
if len(unique_items) > 0:
    st.write('## Packing List')
    for item in unique_items:
        cols = st.columns([3, 1])
        cols[0].write(item)
        cols[1].radio("", ['Not taken', 'Taken'], key=item)
else:
    st.write('Select activities to see the packing list.')
