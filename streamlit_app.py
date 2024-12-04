import streamlit as st
from streamlit_js_eval import streamlit_js_eval

def main():
    # App configuration
    st.set_page_config(
        page_title="Ultimate Emoji Clipboard", 
        page_icon="😀", 
        layout="wide"
    )

    # Extensive emoji dictionary with multiple categories
    emoji_categories = {
        "Faces & Emotions": [
            "😀", "😃", "😄", "😁", "😆", "😅", "🤣", "😂", "🙂", "🙃", 
            "😉", "😊", "😇", "🥰", "😍", "🤩", "😘", "😗", "😚", "😙", 
            "😋", "😛", "😜", "🤪", "😝", "🤑", "🤗", "🤭", "🤫", "🤔",
            "🤐", "🤨", "😐", "😑", "😶", "😏", "😒", "🙄", "😬", "😮",
            "😯", "😪", "😫", "🤤", "😴", "😌", "😛", "😜", "🤤", "🥴"
        ],
        "Animals": [
            "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", 
            "🦁", "🐮", "🐷", "🐽", "🐸", "🐒", "🦄", "🐴", "🦓", "🦌",
            "🐑", "🐐", "🐏", "🦙", "🦘", "🦥", "🐓", "🦃", "🦚", "🦜"
        ],
        "Food & Drink": [
            "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", "🍒", 
            "🍑", "🥭", "🍍", "🥥", "🥝", "🍅", "🍆", "🥑", "🥦", "🥬",
            "🥒", "🌽", "🌶️", "🥕", "🥔", "🍞", "🥐", "🥖", "🥨", "🍔"
        ],
        "Travel & Places": [
            "🚗", "🚕", "🚙", "🚌", "🚎", "🏎️", "🚓", "🚑", "🚒", "🚐", 
            "🚚", "🚛", "🚜", "🛴", "🚲", "🛵", "🏍️", "🚨", "🚥", "🚦",
            "✈️", "🛩️", "🚁", "🚀", "🛸", "🚢", "⚓", "🛥️", "🚤", "🛳️"
        ],
        "Objects & Technology": [
            "📱", "💻", "🖥️", "🖨️", "⌨️", "🖱️", "💽", "💾", "💿", "📀", 
            "🎥", "📷", "📸", "📹", "🎬", "📞", "📟", "📠", "📺", "📻",
            "🧭", "⏰", "🌡️", "🧯", "💡", "🔦", "🕯️", "🪑", "🚪", "🔑"
        ],
        "Sports & Activities": [
            "⚽", "🏀", "🏈", "⚾", "🎾", "🏐", "🏉", "🎱", "🥏", "🏓", 
            "🏸", "🏒", "🏑", "🥍", "🏏", "🥅", "⛳", "🏹", "🥊", "🥋",
            "🤿", "🏄", "🏊", "🤽", "🚣", "🏇", "🏂", "🏋️", "🤸", "🤼"
        ]
    }

    # Title and description
    st.title("🌈 Ultimate Emoji Clipboard")
    st.write("Select and copy emojis from various categories!")

    # Sidebar for category selection
    st.sidebar.header("🔍 Emoji Categories")
    selected_category = st.sidebar.radio(
        "Choose an Emoji Category", 
        list(emoji_categories.keys()), 
        index=0
    )

    # Main emoji display area
    st.header(f"📋 {selected_category} Emojis")
    st.write("Click an emoji to copy it to your clipboard!")

    # Create emoji grid for selected category
    emoji_grid = st.columns(10)
    
    # Display emojis in grid
    for i, emoji in enumerate(emoji_categories[selected_category]):
        with emoji_grid[i % 10]:
            if st.button(emoji, key=f"{selected_category}_{i}", use_container_width=True):
                # Copy emoji to clipboard
                streamlit_js_eval(
                    js_expressions=f"navigator.clipboard.writeText('{emoji}')",
                    key=f'copy_{selected_category}_{i}'
                )
                # Success notification
                st.toast(f"Copied {emoji} to clipboard!", icon="📋")

    # Footer with additional information
    st.markdown("---")
    st.info("💡 Tip: Use the sidebar to switch between emoji categories!")

# Run the application
if __name__ == "__main__":
    main()
