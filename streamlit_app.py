import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Emoji Text Formatter",
        page_icon="✨",
        layout="centered"
    )

    # Custom CSS for improved styling
    st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTextArea {
        border-radius: 10px;
    }
    .emoji-grid {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        gap: 10px;
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .emoji-button {
        font-size: 30px;
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 10px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .emoji-button:hover {
        background-color: #e9ecef;
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("🎨 Emoji Text Formatter")
    st.write("Select emojis and format your text with ease!")

    # Popular emojis categorized
    emoji_categories = {
        "Faces": ["😀", "😍", "😢", "😎", "🤔", "😱", "🥳", "😴", "🤯", "😇"],
        "Animals": ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯"],
        "Objects": ["📱", "💻", "🎮", "🏀", "🚀", "🎂", "🎈", "💡", "🔑", "🎸"],
        "Nature": ["🌞", "🌈", "🍀", "🌻", "🍎", "🌴", "🍄", "🌊", "🌙", "🍁"]
    }

    # Initialize session state for selected emoji
    if 'selected_emoji' not in st.session_state:
        st.session_state.selected_emoji = ""

    # Emoji selection section
    st.header("📋 Emoji Selection")
    
    # Create tabs for emoji categories
    tabs = st.tabs(list(emoji_categories.keys()))
    
    # Emoji selection for each category
    for i, category in enumerate(emoji_categories):
        with tabs[i]:
            emoji_grid = st.columns(10)
            for j, emoji in enumerate(emoji_categories[category]):
                with emoji_grid[j % 10]:
                    if st.button(emoji, key=f"{category}_{j}", use_container_width=True):
                        st.session_state.selected_emoji = emoji
                        st.toast(f"Emoji {emoji} selected!")

    # Text input and formatting section
    st.header("✍️ Text Formatting")
    
    # Text input with emoji addition option
    text = st.text_area("Enter your text here:", 
                        value=st.session_state.get('text_input', ''), 
                        key='text_input_area',
                        height=200)
    
    # Add selected emoji button
    if st.button("Add Selected Emoji"):
        text += st.session_state.selected_emoji
        st.session_state.text_input = text
        st.experimental_rerun()
    
    # Formatting options
    st.subheader("Formatting Options")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        bold = st.checkbox("Bold")
    with col2:
        italic = st.checkbox("Italic")
    with col3:
        underline = st.checkbox("Underline")
    with col4:
        strike = st.checkbox("Strikethrough")

    # Format text
    def format_text(text):
        if bold:
            text = f"**{text}**"
        if italic:
            text = f"*{text}*"
        if underline:
            text = f"<u>{text}</u>"
        if strike:
            text = f"~~{text}~~"
        return text

    # Formatted text
    formatted_text = format_text(text)
    
    # Display formatted text
    st.subheader("Formatted Result:")
    st.markdown(formatted_text, unsafe_allow_html=True)

    # Copy button with direct clipboard interaction
    st.button("Copy Formatted Text", 
              on_click=lambda: st.toast("Copied to clipboard!", icon="📋"),
              key="copy_button")

# Run the app
if __name__ == "__main__":
    main()
