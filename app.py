import streamlit as st

# Website name and title
st.set_page_config(page_title="notafaketrip.com")

# Title of the website
st.title("notafaketrip.com")

pdf_path = f"./tripfiles/brochure.pdf"
with open(pdf_path, "rb") as pdf:
    st.download_button("Download Brochure", data=pdf.read(), file_name="brochure.pdf")
st.write("Trip Itenerary Video: ")
st.write("Extra video: https://youtu.be/QB7ACr7pUuE?si=G8EdFbi0d6af9_Rx")
