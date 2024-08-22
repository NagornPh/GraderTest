import streamlit as st

# Set website title
st.set_page_config(page_title="notafaketrip.com")

# Main title of the website
st.title("Welcome to notafaketrip.com")

# Create menu for Trips
menu = ["Home", "Trips"]
choice = st.sidebar.selectbox("Menu", menu)

# Show Trips page if selected
if choice == "Trips":
    st.subheader("Trips")
    
    # Display one trip: Tokyo Deluxe Plan
    trip_name = "Tokyo Deluxe Plan"
    st.write(trip_name)
    
    # Buttons for trip options
    brochure_button = st.button("Brochure")
    trip_details_button = st.button("Trip Details")
    book_button = st.button("Book")
    
    # If Brochure button is clicked, download brochure file
    if brochure_button:
        with open("brochure.pdf", "rb") as file:
            st.download_button(label="Download Brochure", data=file, file_name="brochure.pdf")
    
    # If Trip Details button is clicked, download trip details file
    if trip_details_button:
        with open("trip_details.pdf", "rb") as file:
            st.download_button(label="Download Trip Details", data=file, file_name="trip_details.pdf")
    
    # If Book button is clicked, show "To be continued..." screen
    if book_button:
        st.write("To be continued...")

