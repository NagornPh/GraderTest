import streamlit as st

# In-memory user store
user_db = {
    "admin": "password123"  # Example user; replace with your own logic
}

# Function to handle login
def login():
    st.session_state["logged_in"] = True

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False

# Function to check if user is logged in
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

# Authentication page
def authentication_page():
    st.title("Sign Up / Log In")

    if st.session_state["logged_in"]:
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
                    # Add user to in-memory DB
                    user_db[user_id] = password
                    st.success("User created successfully! Please log in.")
                else:
                    st.warning("Please enter both username and password.")
        elif mode == "Log In":
            if st.button("Log In"):
                if user_id in user_db and user_db[user_id] == password:
                    login()
                    st.success("Logged in successfully!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password.")

# Define the Home page
def home_page():
    check_login()

    if not st.session_state["logged_in"]:
        authentication_page()
    else:
        st.title("Home Page")
        st.write("Welcome to the Home Page!")
        st.write("You are logged in.")
        # Add other content for the Home page here

# Call the function to display the Home page
home_page()
