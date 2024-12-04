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
    
    # Selected emoji placeholder
    selected_emoji = st.empty()
    
    # Emoji selection for each category
    chosen_emoji = None
    for i, category in enumerate(emoji_categories):
        with tabs[i]:
            emoji_grid = st.columns(10)
            for j, emoji in enumerate(emoji_categories[category]):
                with emoji_grid[j % 10]:
                    if st.button(emoji, key=f"{category}_{j}", use_container_width=True):
                        chosen_emoji = emoji
                        selected_emoji.text(f"Selected Emoji: {chosen_emoji}")

    # Text input section
    st.header("✍️ Text Formatting")
    
    # Text input with emoji addition
    text = st.text_area("Enter your text here:", height=200)
    
    # Add emoji button
    if chosen_emoji and st.button("Add Selected Emoji"):
        text += chosen_emoji
    
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

    # Format text function
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

    # Copy button simulation
    if st.button("Copy Formatted Text"):
        st.toast("Copied to clipboard!", icon="📋")

# Run the app
if __name__ == "__main__":
    main()
