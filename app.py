import streamlit as st

# Website name and title
st.set_page_config(page_title="notafaketrip.com")

# Title of the website
st.title("notafaketrip.com")

pdf_path = f"./tripfiles/brochure.pdf"
with open(pdf_path, "rb") as pdf:
    st.download_button("Download Tokyo Trip Brochure", data=pdf.read(), file_name="brochure.pdf")
    
pdf_path = f"./tripfiles/trip_details.pdf"
with open(pdf_path, "rb") as pdf:
    st.download_button("Download Tokyo Trip Details", data=pdf.read(), file_name="trip_details.pdf")
    
st.write("Trip Itenerary Video: https://drive.google.com/file/d/1YFW-nTt7Ys61NVEwUwz2E9s-c7O9sPI9/view?usp=drivesdk")
st.write("Extra video: https://youtu.be/QB7ACr7pUuE?si=G8EdFbi0d6af9_Rx")
