import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages to navigate
with st.sidebar:
    "Pages"
    page = option_menu(
        ["Home", "Problems", "Submissions", "About"],
        icons=["house", "clipboard", "file-earmark-text", "info-circle"],
        default_index=0
    )

# Page routinga
if page == "Home":
    import Pages.home
elif page == "Problems":
    import Pages.problems
elif page == "Submissions":
    import Pages.submissions
elif page == "About":
    import Pages.about
