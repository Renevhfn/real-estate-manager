HEAD
import streamlit as st
from setup_database import create_database

st.title('🏡 Real Estate Manager')

# Button to create the database
if st.button("Setup Database"):
    create_database()
    st.success("Database created successfully!")


# real-estate-manager
d8d21a1 (Add database setup)
