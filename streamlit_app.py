import streamlit as st
import pyperclip

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

    # Emoji selection section
    st.header("📋 Emoji Selection")
    
    # Create tabs for emoji categories
    tabs = st.tabs(list(emoji_categories.keys()))
    
    # Emoji selection for each category
    selected_emoji = None
    for i, category in enumerate(emoji_categories):
        with tabs[i]:
            emoji_grid = st.columns(10)
            for j, emoji in enumerate(emoji_categories[category]):
                with emoji_grid[j % 10]:
                    if st.button(emoji, key=f"{category}_{j}", use_container_width=True, 
                                 on_click=lambda e=emoji: update_selected_emoji(e)):
                        selected_emoji = emoji

    # Text input and formatting section
    st.header("✍️ Text Formatting")
    
    # Text input
    text = st.text_area("Enter your text here:", height=200)
    
    # Formatting options
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

    # Copy buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Copy Formatted Text"):
            pyperclip.copy(formatted_text)
            st.success("Copied to clipboard!")
    
    with col2:
        if selected_emoji and st.button("Add Selected Emoji"):
            st.session_state.text_input = text + selected_emoji
            st.experimental_rerun()

def update_selected_emoji(emoji):
    st.session_state.selected_emoji = emoji

# Run the app
if __name__ == "__main__":
    main()
