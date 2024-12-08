import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="Text Formatter for LinkedIn",
    page_icon="🪶",
    layout="centered"
)

# Utility functions for text transformations
def bold_text(text):
    bold_dict = { ... }  # (Keep the dictionary content unchanged for brevity)
    return ''.join(bold_dict.get(c, c) for c in text)

def italic_text(text):
    italic_dict = { ... }  # (Keep the dictionary content unchanged for brevity)
    return ''.join(italic_dict.get(c, c) for c in text)

def bold_italic_text(text):
    bold_italic_dict = { ... }  # (Keep the dictionary content unchanged for brevity)
    return ''.join(bold_italic_dict.get(c, c) for c in text)

def add_emojis(text, emoji):
    return f"{emoji} {text} {emoji}"

# Streamlit UI
st.title("LinkedIn Text Formatter")
st.subheader("Transform your text to make your LinkedIn posts stand out!")
st.write("Choose a style below, and enhance your LinkedIn posts.")

# User input
user_input = st.text_area("Enter your text here", placeholder="Type something amazing...")

# Transformation type
transformation_type = st.selectbox(
    "Select a transformation type:",
    ["Bold", "Italic", "Bold Italic", "Add Emojis"]
)

# Display emoji options if "Add Emojis" is selected
if transformation_type == "Add Emojis":
    emoji = st.selectbox(
        "Select an emoji:",
        ["😀", "😂", "😎", "🔥", "🚀", "💼", "💯", "⭐", "😇", "🤩"]
    )

# Apply the selected transformation
if st.button("Transform"):
    if not user_input.strip():  # Check if the input is empty or only whitespace
        st.error("Please enter some text to transform!")
    else:
        if transformation_type == "Bold":
            transformed_text = bold_text(user_input)
        elif transformation_type == "Italic":
            transformed_text = italic_text(user_input)
        elif transformation_type == "Bold Italic":
            transformed_text = bold_italic_text(user_input)
        elif transformation_type == "Add Emojis":
            transformed_text = add_emojis(user_input, emoji)
        
        # Display the transformed text
        st.text_area("Transformed Text", transformed_text, height=100)

# Add emoji box at the bottom
st.write("---")
st.subheader("Quick Emoji Selector")
st.write("Add these emojis to your post for extra flair!")

# Display a grid of emojis as clickable buttons
emoji_list = ["😀", "😂", "😎", "🔥", "🚀", "💼", "💯", "⭐", "😇", "🤩"]
selected_emojis = st.multiselect("Select emojis to append to your text:", emoji_list, default=[])

if selected_emojis:
    st.text_area(
        "Your Text with Emojis",
        f"{user_input} {' '.join(selected_emojis)}",
        height=100
    )
