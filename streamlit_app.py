import streamlit as st

# Set page configuration with title and icon
st.set_page_config(
    page_title="Text Formatter & Emojis",
    page_icon="💬"
)

# Text transformation functions
def bold_text(text):
    # Your existing bold dictionary
    bold_dict = {
        'A': '𝐀', 'B': '𝐁', # Full dictionary as in your code
        ' ': ' '
    }
    return ''.join(bold_dict.get(c, c) for c in text)

def italic_text(text):
    # Italic dictionary similar to your existing code
    italic_dict = {
        'A': '𝘈', 'B': '𝘉', # Full dictionary as in your code
        ' ': ' '
    }
    return ''.join(italic_dict.get(c, c) for c in text)

# Emoji selection function with clickable rectangle layout
def emoji_selection_section():
    st.markdown("### Select Emojis:")
    emojis = ["😊", "🚀", "💡", "📊", "🔥", "🌍", "🎉", "❤️", "💻", "📈"]

    # Display emojis as buttons within a grid
    col1, col2, col3 = st.columns(3)
    emoji_selected = None  # Variable to store the clicked emoji

    for index, emoji in enumerate(emojis):
        with [col1, col2, col3][index % 3]:  # Rotate through columns
            if st.button(emoji, key=f"emoji_{emoji}"):
                st.session_state.selected_emoji = emoji
                st.success(f"Selected: {emoji}")  # Provide feedback
                st.write("Copy with Ctrl+C or ⌘+C after selecting")

# Main Streamlit app function
def main():
    st.title("Text Formatter & Emojis")
    st.write("Enter your text, choose the style, and select emojis!")

    # Text input area
    user_input = st.text_area("Enter your text here", height=200)

    # Sidebar or column for style selection
    col1, col2 = st.columns([2, 1])
    with col2:
        transformation_type = st.radio("Select Transformation:", ["Bold", "Italic", "Add Emoji"])
        emoji_selection_section()  # Call emoji selector inside column

    # Button to apply transformation
    if st.button("Transform"):
        if user_input:
            if transformation_type == "Bold":
                transformed_text = bold_text(user_input)
            elif transformation_type == "Italic":
                transformed_text = italic_text(user_input)
            else:  # Add emoji at the end
                emoji = st.session_state.get("selected_emoji", "")
                transformed_text = f"{user_input} {emoji}"
            
            st.success("Transformed Text:")
            st.code(transformed_text)  # Display transformed result

# Run the app
if __name__ == "__main__":
    main()

