import streamlit as st

# Title
st.title("Text Copy Example")

# Text area for user input
text_to_copy = st.text_area('Type in the text area and click Copy')

# JavaScript for browser clipboard
copy_js = f"""
<script>
function copyText() {{
    const text = {text_to_copy.__repr__()};  // Capture Streamlit text
    navigator.clipboard.writeText(text).then(() => {{
        alert("Text copied to clipboard!");
    }});
}}
</script>
<button onclick="copyText()">Copy</button>
"""

# Display button with JavaScript
st.markdown(copy_js, unsafe_allow_html=True)
