import streamlit as st
import pyperclip

# Set page configuration
st.set_page_config(
    page_title="Text Formatter & Emojis without ads",
    page_icon="💬"
)

# All previous functions remain the same (bold_text, italic_text, bold_italic_text, add_emojis)
# [Copying all the original functions from the previous implementation]

# Expanded emoji dictionary with more categories
EMOJI_CATEGORIES = {
    "Smileys": ["😀", "😂", "🤣", "😊", "🙃", "😉", "🥹", "😍"],
    "Professional": ["💼", "🚀", "📊", "💡", "🏆", "⭐", "💯", "🤝"],
    "Celebrations": ["🎉", "🎊", "🥳", "🎂", "🍾", "🎈", "👏", "🎓"],
    "Nature": ["🌟", "🌈", "🍀", "🌻", "🌍", "🍃", "🔆", "🌞"],
    "Hand Gestures": ["👍", "👏", "✌️", "🤘", "👊", "🙌", "✨", "🤲"]
}

# Improved emoji selection function
def emoji_selection_section():
    # Emoji category selection
    selected_category = st.selectbox(
        "Choose Emoji Category", 
        list(EMOJI_CATEGORIES.keys()),
        help="Select a category of emojis"
    )
    
    # Display emojis in a grid
    st.write("### Click on an emoji to copy it:")
    emojis = EMOJI_CATEGORIES[selected_category]
    
    # Create columns for emoji display
    cols = st.columns(min(8, len(emojis)))
    
    # Store the selected emoji
    selected_emoji = None
    
    # Display emojis
    for i, emoji in enumerate(emojis):
        with cols[i % len(cols)]:
            if st.button(emoji, key=f"emoji_{emoji}"):
                # Copy emoji to clipboard
                pyperclip.copy(emoji)
                st.success(f"Copied: {emoji}")
                selected_emoji = emoji
    
    return selected_emoji

# Streamlit app
def main():
    st.title("Text Formatter & Emojis")
    st.write("Enter your text and choose your transformation style!")

    # Create columns for input and options
    col1, col2 = st.columns([2, 1])

    with col1:
        # Text input from user
        user_input = st.text_area("Enter your text here", height=200)

    with col2:
        # Transformation type selection with visual radio buttons
        st.markdown("**Select Transformation:**")
        transformation_type = st.radio(
            "Choose the transformation type",
            ["Bold", "Italic", "Bold Italic", "Add Emoji"],
            help="Select how you want to style your text for LinkedIn"
        )

        # Improved emoji selection
        selected_emoji = emoji_selection_section()

    # Transform button with improved styling
    transform_col1, transform_col2 = st.columns([1, 3])

    with transform_col1:
        if st.button("Transform", type="primary"):
            if user_input:
                if transformation_type == "Bold":
                    transformed_output = bold_text(user_input)
                elif transformation_type == "Italic":
                    transformed_output = italic_text(user_input)
                elif transformation_type == "Bold Italic":
                    transformed_output = bold_italic_text(user_input)
                elif transformation_type == "Add Emoji":
                    if selected_emoji:
                        transformed_output = add_emojis(user_input, selected_emoji)
                    else:
                        transformed_output = "Please select an emoji first!"
                
                # Display transformed text in a highlighted box
                st.markdown("**Transformed Text:**")
                st.code(transformed_output, language="text")
                
                # Copy to clipboard button
                if st.button("Copy Transformed Text"):
                    pyperclip.copy(transformed_output)
                    st.success("Copied to clipboard!")

    # Donation button on the main page
    st.markdown(
        """
        <a href='https://ko-fi.com/sitrakaforler' target='_blank'><img height='36' style='border:0px;height:36px;' 
        src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>        
        """,
        unsafe_allow_html=True,
    )

    # Donation button in the sidebar
    with st.sidebar:
        st.image("SitrakasLogo.png")
        st.markdown(
            """
       <a href='https://ko-fi.com/C0C6YRSIF' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi1.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
       """,
            unsafe_allow_html=True,
        )

# Run the main function
if __name__ == "__main__":
    main()
