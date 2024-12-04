import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Text Formatter & Emojis without ads",
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
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟖',
        '7': '𝟗', '8': '𝟖', '9': '𝟕',
    }
    return ''.join(bold_dict.get(c, c) for c in text)

# Function to add emojis
def add_emojis(text, emoji):
    return f"{emoji} {text} {emoji}"

# Expanded emoji dictionary with more categories
EMOJI_CATEGORIES = {
    "Smileys": ["😀", "😂", "🤣", "😊", "🙃", "😉", "🥹", "😍"],
    "Professional": ["💼", "🚀", "📊", "💡", "🏆", "⭐", "💯", "🤝"],
    "Celebrations": ["🎉", "🎊", "🥳", "🎂", "🍾", "🎈", "👏", "🎓"],
    "Nature": ["🌟", "🌈", "🍀", "🌻", "🌍", "🍃", "🔆", "🌞"],
    "Hand Gestures": ["👍", "👏", "✌️", "🤘", "👊", "🙌", "✨", "🤲"]
}

# Streamlit app
st.title("Text Formatter & Emojis")
st.write("Enter your text and choose your transformation style!")

# Create columns for input and options
col1, col2 = st.columns([2, 1])

with col1:
    # Text input from user
    user_input = st.text_area("Enter your text here", height=200)

with col2:
    # Transformation type selection with visual radio buttons
    st.markdown("**Select Transformation:**")
    transformation_type = st.radio(
        "Choose the transformation type",
        ["Bold", "Italic", "Bold Italic", "Add Emoji"],
        help="Select how you want to style your text for LinkedIn"
    )

    # Emoji selection with category tabs
    st.markdown("**Select Emoji Category:**")
    emoji_tab = st.selectbox(
        "Choose Emoji Category", 
        list(EMOJI_CATEGORIES.keys()),
        help="Select a category of emojis"
    )
    
    st.markdown("**Select Emoji:**")
    emoji = st.selectbox(
        "Choose an emoji", 
        EMOJI_CATEGORIES[emoji_tab],
        help="Select an emoji to add to your text"
    )

# Process the user input based on selected transformation type
if transformation_type == "Bold":
    transformed_text = bold_text(user_input)
elif transformation_type == "Italic":
    transformed_text = italic_text(user_input)
elif transformation_type == "Bold Italic":
    transformed_text = bold_italic_text(user_input)
elif transformation_type == "Add Emoji":
    transformed_text = add_emojis(user_input, emoji)

# Display the transformed text
st.markdown(f"### Transformed Text: {transformed_text}")

# Donation button on the main page
st.markdown(
    """
    <a href='https://ko-fi.com/sitrakaforler' target='_blank'><img height='36' style='border:0px;height:36px;' 
    src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>        
    """,
    unsafe_allow_html=True,
)

# Donation button in the sidebar
with st.sidebar:
    st.image("SitrakasLogo.png")
    st.markdown(
        """
   <a href='https://ko-fi.com/C0C6YRSIF' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi1.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
   """,
        unsafe_allow_html=True,
    )
