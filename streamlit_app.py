import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Text Formatter & Emojis",
    page_icon="💬"
)

# Function to convert normal text to bold text
def bold_text(text):
    bold_dict = {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
        'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
        'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
        'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
        'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠',
        'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧',
        'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮',
        'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔',
        '7': '𝟕', '8': '𝟖', '9': '𝟗'
    }
    return ''.join(bold_dict.get(c, c) for c in text)

# Function to convert normal text to italic text
def italic_text(text):
    italic_dict = {
        'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍', 'G': '𝘎',
        'H': '𝘏', 'I': '𝘐', 'J': '𝘑', 'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕',
        'O': '𝘖', 'P': '𝘗', 'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛', 'U': '𝘜',
        'V': '𝘝', 'W': '𝘞', 'X': '𝘟', 'Y': '𝘠', 'Z': '𝘡',
        'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨',
        'h': '𝘩', 'i': '𝘪', 'j': '𝘫', 'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯',
        'o': '𝘰', 'p': '𝘱', 'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵', 'u': '𝘶',
        'v': '𝘷', 'w': '𝘸', 'x': '𝘹', 'y': '𝘺', 'z': '𝘻'
    }
    return ''.join(italic_dict.get(c, c) for c in text)

# Emoji selection section
def emoji_selection_section():
    st.markdown("### Select Emojis:")
    emojis = ["😊", "🚀", "💡", "📊", "🔥", "🌍", "🎉", "❤️", "💻", "📈"]
    emoji_columns = st.columns(len(emojis))

    for i, emoji in enumerate(emojis):
        with emoji_columns[i]:
            if st.button(emoji, key=f"emoji_{emoji}"):
                st.session_state.selected_emoji = emoji
                st.success(f"Copied: {emoji}")
    return st.session_state.selected_emoji

# Streamlit app
def main():
    # Initialize session state for selected emoji if not exists
    if 'selected_emoji' not in st.session_state:
        st.session_state.selected_emoji = None

    st.title("Text Formatter & Emojis")
    st.write("Enter your text and choose your transformation style!")

    user_input = st.text_area("Enter your text here", height=200)
    
    # Transformation type selection
    transformation_type = st.radio(
        "Choose the transformation type:",
        ["Bold", "Italic", "Add Emoji"],
        horizontal=True
    )

    # Display emoji section within a border
    st.markdown('<div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px;">', unsafe_allow_html=True)
    selected_emoji = emoji_selection_section()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Transform"):
        if user_input:
            if transformation_type == "Bold":
                transformed_output = bold_text(user_input)
            elif transformation_type == "Italic":
                transformed_output = italic_text(user_input)
            elif transformation_type == "Add Emoji":
                if selected_emoji:
                    transformed_output = f"{user_input} {selected_emoji}"
                else:
                    transformed_output = "Please select an emoji first!"
            else:
                transformed_output = user_input  # Default if no transformation

            # Display transformed text in a highlighted box
            st.markdown("**Transformed Text:**")
            st.code(transformed_output, language="text")

if __name__ == "__main__":
    main()
