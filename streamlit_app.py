import streamlit as st

def main():
    st.set_page_config(page_title="Emoji Picker", page_icon="😀")

    st.title("📋 Emoji Picker & Text Formatter")

    # Emoji categories with more options
    emoji_categories = {
        "Faces": ["😀", "😍", "😢", "😎", "🤔", "😱", "🥳", "😴", "🤯", "😇"],
        "Animals": ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯"],
        "Objects": ["📱", "💻", "🎮", "🏀", "🚀", "🎂", "🎈", "💡", "🔑", "🎸"],
        "Nature": ["🌞", "🌈", "🍀", "🌻", "🍎", "🌴", "🍄", "🌊", "🌙", "🍁"]
    }

    # Emoji selection
    st.header("Select Emojis")
    selected_tab = st.radio("Choose Emoji Category", list(emoji_categories.keys()), horizontal=True)
    
    # Display emojis in grid
    emoji_grid = st.columns(10)
    for i, emoji in enumerate(emoji_categories[selected_tab]):
        with emoji_grid[i % 10]:
            if st.button(emoji, key=emoji):
                st.toast(f"Copied {emoji}")
                st.code(emoji)

    # Text formatting section
    st.header("Text Formatter")
    text = st.text_area("Enter your text", height=200)

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

    # Show formatted text
    formatted_text = format_text(text)
    st.subheader("Formatted Result:")
    st.markdown(formatted_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
