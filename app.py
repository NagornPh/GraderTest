import streamlit as st
from Pages import home, problems, submissions, about

with st.sidebar:
    page = st.radio("Pages", ["Home", "Problems", "Submissions", "About"], index=0)

if page == "Home":
    home.render_home_page()
elif page == "Problems":
    problems.render_problems_page()
elif page == "Submissions":
    submissions.render_submissions_page()
elif page == "About":
    about.render_about_page()
