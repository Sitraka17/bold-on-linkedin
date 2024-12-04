import streamlit as st
from streamlit_js_eval import streamlit_js_eval

def format_text(text, formatting_options):
    """
    Apply multiple text formatting styles based on user selections.
    
    Args:
        text (str): The input text to format
        formatting_options (dict): Dictionary of formatting options
    
    Returns:
        str: Formatted text with applied styles
    """
    # Apply formatting in a specific order
    if formatting_options['bold']:
        text = f"**{text}**"
    if formatting_options['italic']:
        text = f"*{text}*"
    if formatting_options['underline']:
        text = f"<u>{text}</u>"
    if formatting_options['strike']:
        text = f"~~{text}~~"
    
    return text

def main():
    # Set page configuration with enhanced styling
    st.set_page_config(
        page_title="Emoji Text Formatter",
        page_icon="✨",
        layout="wide"
    )

    

    # Title and description
    st.title("🎨 Emoji Text Formatter")
    st.write("Select emojis, format your text, and copy with ease!")

    # Expanded emoji categories
    emoji_categories = {
        "Faces": ["😀", "😍", "😢", "😎", "🤔", "😱", "🥳", "😴", "🤯", "😇"],
        "Animals": ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯"],
        "Objects": ["📱", "💻", "🎮", "🏀", "🚀", "🎂", "🎈", "💡", "🔑", "🎸"],
        "Nature": ["🌞", "🌈", "🍀", "🌻", "🍎", "🌴", "🍄", "🌊", "🌙", "🍁"],
        "Symbols": ["❤️", "🔥", "✨", "👍", "💯", "🌟", "🚀", "🎉", "💕", "🤯"]
    }

    # Initialize session state
    if 'selected_emoji' not in st.session_state:
        st.session_state.selected_emoji = ""
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""

    # Create layout with sidebar for categories
    st.sidebar.header("🔍 Emoji Categories")
    selected_category = st.sidebar.radio(
        "Choose Emoji Category", 
        list(emoji_categories.keys()), 
        index=0
    )

    # Emoji selection section
    st.header("📋 Emoji Selection")
    
    # Display emojis for selected category
    emoji_grid = st.columns(10)
    for j, emoji in enumerate(emoji_categories[selected_category]):
        with emoji_grid[j % 10]:
            if st.button(emoji, key=f"{selected_category}_{j}", use_container_width=True):
                st.session_state.selected_emoji = emoji
                st.toast(f"Emoji {emoji} selected!")

    # Text input and formatting section
    st.header("✍️ Text Formatting")
    
    # Text input with larger height
    text = st.text_area("Enter your text here:", height=250, key="text_input")
    
    # Emoji and text manipulation controls
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.write(f"Selected Emoji: {st.session_state.selected_emoji or 'None'}")
    
    with col2:
        # Add Emoji button
        if st.button("Add Emoji", disabled=not st.session_state.selected_emoji):
            current_text = st.session_state.text_input
            st.session_state.text_input = current_text + st.session_state.selected_emoji
    
    with col3:
        # Clear Text button
        if st.button("Clear Text"):
            st.session_state.text_input = ""
            st.session_state.selected_emoji = ""

    # Formatting options
    st.subheader("Formatting Options")
    col1, col2, col3, col4 = st.columns(4)
    
    # Formatting checkboxes with unique keys
    with col1:
        bold = st.checkbox("Bold", key="bold_format")
    with col2:
        italic = st.checkbox("Italic", key="italic_format")
    with col3:
        underline = st.checkbox("Underline", key="underline_format")
    with col4:
        strike = st.checkbox("Strikethrough", key="strike_format")

    # Prepare formatting options
    formatting_options = {
        'bold': bold,
        'italic': italic,
        'underline': underline,
        'strike': strike
    }

    # Format text
    formatted_text = format_text(text, formatting_options)
    
    # Display formatted text
    st.subheader("Formatted Result:")
    st.markdown(formatted_text or "Your formatted text will appear here...", unsafe_allow_html=True)

    # Copy buttons with JavaScript clipboard integration
    col1, col2 = st.columns(2)
    
    with col1:
        # Copy Formatted Text button
        if st.button("Copy Formatted Text", disabled=not text):
            streamlit_js_eval(
                js_expressions=f"navigator.clipboard.writeText(`{formatted_text}`)",
                key='copy_formatted'
            )
            st.toast("Formatted text copied to clipboard!", icon="📋")
    
    with col2:
        # Copy Plain Text button
        if st.button("Copy Plain Text", disabled=not text):
            streamlit_js_eval(
                js_expressions=f"navigator.clipboard.writeText(`{text}`)",
                key='copy_plain'
            )
            st.toast("Plain text copied to clipboard!", icon="📝")

# Run the application
if __name__ == "__main__":
    main()
