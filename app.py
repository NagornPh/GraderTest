import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages to navigate
with st.sidebar:
    page = option_menu(
        "Pages",
        ["Home", "Problems", "Submissions", "About"],
        icons=["house", "clipboard", "file-earmark-text", "info-circle"],
        default_index=0
    )

if page == "Home":
    import Pages.home
elif page == "Problems":
    import Pages.problems
elif page == "Submissions":
    import Pages.submissions
elif page == "About":
    import Pages.about

#bruh1a
