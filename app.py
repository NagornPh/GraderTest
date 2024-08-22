import streamlit as st

# Website name and title
st.set_page_config(page_title="notafaketrip.com")

# Title of the website
st.title("notafaketrip.com")

# Menu - Sidebar
menu = ["Home", "Trips"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Trips":
    st.subheader("Available Trips")
    if st.button("Tokyo Deluxe Plan"):
        # Buttons for Brochure, Trip Details, and Book
        brochure = st.button("Brochure")
        details = st.button("Trip Details")
        book = st.button("Book")
        
        # Handle Brochure download
        if brochure:
            with open("tripfiles/brochure.pdf", "rb") as file:
                st.download_button(label="Download Brochure", data=pdf.read(), file_name="brochure.pdf")

        # Handle Trip Details download
        if details:
            with open("tripfiles/trip_details.pdf", "rb") as file:
                st.download_button(label="Download Trip Details", data=pdf.read(), file_name="trip_details.pdf")
        
        # Handle Book action
        if book:
            st.subheader("To be continued...")

