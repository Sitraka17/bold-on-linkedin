import streamlit as st
import pyperclip

# Title
st.title("Text Copy Example")

# Text area for user input
text_to_copy = st.text_area('Type in the text area and click Copy')

# Button to copy text
if st.button('Copy'):
    if text_to_copy:  # Ensure there's something to copy
        pyperclip.copy(text_to_copy)
        st.success('Text copied successfully!')
    else:
        st.warning("Please enter some text to copy.")
