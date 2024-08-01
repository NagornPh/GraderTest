import streamlit as st
from streamlit_option_menu import option_menu

st.title("Test Navigation")

with st.sidebar:
    page = option_menu(
        "Test",
        ["Page 1", "Page 2"],
        icons=["house", "clipboard"],
        default_index=0
    )

if page == "Page 1":
    st.write("You are on Page 1")
elif page == "Page 2":
    st.write("You are on Page 2")
