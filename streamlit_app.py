import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

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

    # Emoji selection section
    st.header("📋 Emoji Selection")

    # Create tabs for emoji categories
    tabs = st.tabs(list(emoji_categories.keys()))
    for i, (category, emojis) in enumerate(emoji_categories.items()):
        with tabs[i]:
            cols = st.columns(5)
            for j, emoji in enumerate(emojis):
                if cols[j % 5].button(emoji, key=f"{category}_{j}"):
                    st.session_state.selected_emoji = emoji
                    st.toast(f"Emoji {emoji} selected!")

    # Text input and formatting section
    st.header("✍️ Text Formatting")
    text = st.text_area("Enter your text here:", height=200, key="text_input")

    # Add selected emoji button
    if st.button("Add Selected Emoji"):
        if st.session_state.selected_emoji:
            st.session_state.text_input += st.session_state.selected_emoji
            st.experimental_rerun()
        else:
            st.warning("Please select an emoji first!")

    # Formatting options
    st.subheader("Formatting Options")
    bold, italic, underline, strike = st.columns(4)

    bold = bold.checkbox("Bold")
    italic = italic.checkbox("Italic")
    underline = underline.checkbox("Underline")
    strike = strike.checkbox("Strikethrough")

    # Format text based on options
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

    # Display formatted text
    st.subheader("Formatted Result:")
    st.markdown(formatted_text, unsafe_allow_html=True)

    # Clipboard functionality with st-copy-to-clipboard
    st_copy_to_clipboard(formatted_text)

if __name__ == "__main__":
    main()
