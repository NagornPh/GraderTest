import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages to navigate
with st.sidebar:
    page = option_menu(
        "Navigation",
        ["Home", "Problems", "Submissions", "About"],
        icons=["house", "clipboard", "file-earmark-text", "info-circle"],
        default_index=0
    )

if page == "Home":
    import pages.home
elif page == "Problems":
    import pages.problems
elif page == "Submissions":
    import pages.submissions
elif page == "About":
    import pages.about
