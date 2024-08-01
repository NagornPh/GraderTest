import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

# Initialize cookies manager
cookies = EncryptedCookieManager(
    prefix="my_app_",
    secret_key="my_secret_key",
    cookie_expiration_days=30
)
cookies.load()

# Function to handle login
def login():
    st.session_state["logged_in"] = True
    cookies["logged_in"] = "true"

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    cookies.pop("logged_in", None)

# Authentication page
def authentication_page():
    st.title("Sign Up / Log In")

    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        st.write("You are already logged in.")
        if st.button("Log Out"):
            logout()
            st.experimental_rerun()
    else:
        mode = st.radio("Select an option", ["Log In", "Sign Up"])

        user_id = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if mode == "Sign Up":
            if st.button("Sign Up"):
                if user_id and password:
                    create_user(user_id, password)
                    st.success("User created successfully! Please log in.")
                else:
                    st.warning("Please enter both username and password.")
        elif mode == "Log In":
            if st.button("Log In"):
                if authenticate_user(user_id, password):
                    login()
                    st.success("Logged in successfully!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password.")

# Define the Home page
def home_page():
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        authentication_page()
    else:
        st.title("Home Page")
        st.write("Welcome to the Home Page!")
        st.write("You are logged in.")
        # Add other content for the Home page here

# Call the function to display the Home page
home_page()
