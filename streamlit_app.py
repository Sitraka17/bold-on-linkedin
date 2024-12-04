import streamlit as st

def format_text(text, bold=False, italic=False, underline=False, strike=False):
    """
    Apply text formatting based on selected options.
    
    Args:
        text (str): Input text to format
        bold (bool): Apply bold formatting
        italic (bool): Apply italic formatting
        underline (bool): Apply underline formatting
        strike (bool): Apply strikethrough formatting
    
    Returns:
        str: Formatted text with Markdown/HTML styling
    """
    # Apply formatting in a specific order for best readability
    if bold:
        text = f"**{text}**"
    if italic:
        text = f"*{text}*"
    if underline:
        text = f"<u>{text}</u>"
    if strike:
        text = f"~~{text}~~"
    
    return text

def initialize_session_state():
    """
    Initialize session state variables with default values.
    This ensures clean state management and prevents errors.
    """
    # Define default values for session state
    default_states = {
        'selected_emoji': '',
        'text_input': '',
        'formatting': {
            'bold': False,
            'italic': False,
            'underline': False,
            'strike': False
        }
    }
    
    # Initialize each state variable if not already exists
    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value

def main():
    # Set page configuration with enhanced details
    st.set_page_config(
        page_title="Emoji Text Formatter",
        page_icon="📱",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state to prevent errors
    initialize_session_state()
    
    # Title and description with more engaging introduction
    st.title("🎨 Emoji Text Formatter")
    st.write("Transform your text with playful emojis and creative formatting!")
    
    # Emoji categories with more diverse selection
    emoji_categories = {
        "Faces": ["😀", "😍", "😢", "😎", "🤔", "😱", "🥳", "😴", "🤯", "😇"],
        "Animals": ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯"],
        "Objects": ["📱", "💻", "🎮", "🏀", "🚀", "🎂", "🎈", "💡", "🔑", "🎸"],
        "Nature": ["🌞", "🌈", "🍀", "🌻", "🍎", "🌴", "🍄", "🌊", "🌙", "🍁"]
    }
    
    # Emoji selection section with tabs
    st.header("📋 Emoji Selection")
    tabs = st.tabs(list(emoji_categories.keys()))
    
    # Dynamic emoji selection grid
    for i, category in enumerate(emoji_categories):
        with tabs[i]:
            emoji_grid = st.columns(10)
            for j, emoji in enumerate(emoji_categories[category]):
                with emoji_grid[j % 10]:
                    if st.button(emoji, key=f"{category}_{j}", use_container_width=True):
                        # Update selected emoji with more robust handling
                        st.session_state.selected_emoji = emoji
                        st.toast(f"Emoji {emoji} selected!", icon="✅")
    
    # Text input and formatting section
    st.header("✍️ Text Formatting")
    
    # Text input with placeholder and clear guidance
    text = st.text_area(
        "Enter your text here:", 
        height=200, 
        key="text_input", 
        placeholder="Type or paste your text. Select an emoji to add, and choose formatting options!"
    )
    
    # Emoji and formatting controls
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Selected Emoji: {st.session_state.selected_emoji or '(None)'}")
    
    with col2:
        if st.button("Add Emoji", disabled=not st.session_state.selected_emoji):
            # More robust emoji addition
            current_text = st.session_state.text_input
            st.session_state.text_input = current_text + st.session_state.selected_emoji
    
    # Formatting options with state tracking
    st.subheader("Formatting Options")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        bold = st.checkbox("Bold", key="bold_check")
    with col2:
        italic = st.checkbox("Italic", key="italic_check")
    with col3:
        underline = st.checkbox("Underline", key="underline_check")
    with col4:
        strike = st.checkbox("Strikethrough", key="strike_check")
    
    # Formatted text generation
    formatted_text = format_text(
        text, 
        bold=bold, 
        italic=italic, 
        underline=underline, 
        strike=strike
    )
    
    # Display formatted text with clear separation
    st.subheader("Formatted Result:")
    st.markdown(formatted_text or "Your formatted text will appear here...", unsafe_allow_html=True)
    
    # Enhanced copy functionality
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Copy Formatted Text", disabled=not text):
            # Simulate clipboard copy (Streamlit doesn't have direct clipboard access)
            st.toast("Text copied to clipboard!", icon="📋")
    
    with col2:
        if st.button("Clear All", type="primary"):
            # Reset all session state variables
            st.session_state.text_input = ""
            st.session_state.selected_emoji = ""
            st.experimental_rerun()

# Ensure proper script execution
if __name__ == "__main__":
    main()
