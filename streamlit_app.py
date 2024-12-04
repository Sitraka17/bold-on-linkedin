import streamlit as st
import pyperclip

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Emoji Text Formatter",
        page_icon="✨",
        layout="centered"
    )

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

    # Initialize session state
    if 'selected_emoji' not in st.session_state:
        st.session_state.selected_emoji = ""
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""

    # Emoji selection section
    st.header("📋 Emoji Selection")
    # Create tabs for emoji categories
    tabs = st.tabs(list(emoji_categories.keys()))
    
    for i, category in enumerate(emoji_categories):
        with tabs[i]:
            for emoji in emoji_categories[category]:
                if st.button(emoji, key=f"{category}_{emoji}"):
                    st.session_state.selected_emoji = emoji
                    st.toast(f"Emoji {emoji} selected!")

    # Text input and formatting section
    st.header("✍️ Text Formatting")
    text = st.text_area("Enter your text here:", height=200, key="text_input")
    
    if st.session_state.selected_emoji:
        if st.button("Add Emoji"):
            st.session_state.text_input += st.session_state.selected_emoji
            st.experimental_rerun()

    # Formatting options
    st.subheader("Formatting Options")
    bold = st.checkbox("Bold")
    italic = st.checkbox("Italic")
    underline = st.checkbox("Underline")
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

    formatted_text = format_text(text)
    st.subheader("Formatted Result:")
    st.markdown(formatted_text, unsafe_allow_html=True)

    # Copy functionality using pyperclip
    if st.button("Copy Formatted Text"):
        pyperclip.copy(formatted_text)
        st.toast("Copied to clipboard!", icon="📋")

# Run the app
if __name__ == "__main__":
    main()
