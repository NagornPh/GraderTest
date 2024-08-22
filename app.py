import streamlit as st
from io import BytesIO

# Set the title of the website
st.set_page_config(page_title="notafaketrip.com")

# Define the menu tabs
menu_tabs = ["Home", "Trips"]
selected_tab = st.sidebar.radio("Menu", menu_tabs)

if selected_tab == "Home":
    st.title("Welcome to notafaketrip.com!")
    st.write("Explore amazing travel packages and plan your next adventure.")

elif selected_tab == "Trips":
    trip_tabs = st.tabs(["Tokyo Deluxe Plan"])

    with trip_tabs[0]:
        st.header("Tokyo Deluxe Plan")
        st.write("Enjoy a luxurious trip to Tokyo with the finest experiences for the cheap price of 1.3M thb.")

        # Define buttons
        brochure = st.button("Brochure")
        trip_details = st.button("Trip Details")
        book = st.button("Book")

        # Brochure button functionality
        if brochure:
            brochure_content = BytesIO(b"Tokyo Deluxe Plan Brochure")
            st.download_button(label="Download Brochure", data=brochure_content, file_name="Tokyo_Deluxe_Brochure.pdf")

        # Trip Details button functionality
        if trip_details:
            trip_details_content = BytesIO(b"Tokyo Deluxe Plan Detailed Information")
            st.download_button(label="Download Trip Details", data=trip_details_content, file_name="Tokyo_Deluxe_Details.pdf")

        # Book button functionality
        if book:
            st.write("To be continued...")

