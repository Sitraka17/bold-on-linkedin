import streamlit as st
from streamlit_js_eval import streamlit_js_eval

def main():
    # Set up the app configuration
    st.set_page_config(
        page_title="Emoji Clipboard Copier", 
        page_icon="📋", 
        layout="centered"
    )

    # Title and description
    st.title("📋 Emoji Clipboard Copier")
    st.write("Select and instantly copy emojis to your clipboard!")

    # Comprehensive emoji categories
    emoji_categories = {
        "Faces": ["😀", "😂", "😊", "😍", "😎", "🤓", "🥳", "😇", "🤩", "😜"],
        "Emotions": ["🥺", "😡", "😭", "😱", "🤯", "😳", "😴", "🤔", "😉", "😢"],
        "Characters": ["🤖", "👻", "👽", "🤠", "💩", "🤡", "👾", "🧠", "🤤", "👀"],
        "Symbols": ["❤️", "🔥", "✨", "👍", "👏", "🎉", "🌈", "🌟", "💯", "🚀"]
    }

    # Emoji selection with tabs
    st.header("Select an Emoji to Copy")
    
    # Create tabs for emoji categories
    tabs = st.tabs(list(emoji_categories.keys()))
    
    # Emoji selection for each category
    for i, (category, emojis) in enumerate(emoji_categories.items()):
        with tabs[i]:
            # Create a grid of emojis
            emoji_grid = st.columns(5)
            
            for j, emoji in enumerate(emojis):
                with emoji_grid[j % 5]:
                    # Button to copy emoji
                    if st.button(emoji, key=f"{category}_{j}", use_container_width=True):
                        # Use streamlit_js_eval to copy to clipboard
                        streamlit_js_eval(
                            js_expressions=f"navigator.clipboard.writeText('{emoji}')",
                            key=f'copy_{category}_{j}'
                        )
                        # Show success toast
                        st.toast(f"Copied {emoji} to clipboard!", icon="📋")

    # Informative footer
    st.markdown("---")
    st.info("💡 Pro Tip: Click on any emoji to instantly copy it to your clipboard!")

# Run the app
if __name__ == "__main__":
    main()
