import streamlit as st

# Title
st.title("Text Copy Example")

# Text area for user input
text_to_copy = st.text_area('Type in the text area and click Copy')

# JavaScript to copy text to clipboard
copy_button = f"""
    <script>
        function copyText() {{
            const text = {repr(text_to_copy)};  // Safely escape user input
            navigator.clipboard.writeText(text).then(() => {{
                alert("Text copied to clipboard!");
            }}).catch(err => {{
                console.error('Could not copy text:', err);
            }});
        }}
    </script>
    <button onclick="copyText()">Copy</button>
"""

# Display the button with the JavaScript code
st.markdown(copy_button, unsafe_allow_html=True)
