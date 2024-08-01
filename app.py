import streamlit as st

# Define the pages to navigate
page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Problems", "Submissions", "About"]
)

if page == "Home":
    import Pages.home
elif page == "Problems":
    import Pages.problems
elif page == "Submissions":
    import Pages.submissions
elif page == "About":
    import Pages.about
