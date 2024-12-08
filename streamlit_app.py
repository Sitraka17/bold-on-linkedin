# A not so bad version
import streamlit as st

# Configure Streamlit app
st.set_page_config(
    page_title="Emoji Text Formatter",
    page_icon="🪶",
    layout="centered"
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
        '7': '𝟕', '8': '𝟖', '9': '𝟗',
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
        'v': '𝘷', 'w': '𝘸', 'x': '𝘹', 'y': '𝘺', 'z': '𝘻',
    }
    return ''.join(italic_dict.get(c, c) for c in text)

# Function to add emojis
def add_emojis(text, emoji):
    return f"{emoji} {text} {emoji}"

# Streamlit app
st.title("LinkedIn Text Formatter")
st.write("Enter your text below to transform it into bold, italic, or bold italic text for LinkedIn:")

# Text input from user
user_input = st.text_area("Enter your text here")

# Transformation type selection
transformation_type = st.selectbox("Choose the transformation type", ["Bold", "Italic", "Add Emoji"])

# Emoji selection (only if "Add Emoji" is selected)
emoji = None
if transformation_type == "Add Emoji":
    emoji = st.selectbox("Choose an emoji", ["😀", "😂", "🔥", "👍", "🚀", "⭐", "💯", "🥳", "😇", "🤩"])

# Perform the transformation
if st.button("Transform"):
    if transformation_type == "Bold":
        transformed_text = bold_text(user_input)
    elif transformation_type == "Italic":
        transformed_text = italic_text(user_input)
    elif transformation_type == "Add Emoji" and emoji:
        transformed_text = add_emojis(user_input, emoji)
    else:
        transformed_text = user_input  # No transformation

    st.subheader("Transformed Text")
    st.text(transformed_text)

# Add emoji box at the bottom
st.write("---")
st.subheader("Quick Emoji Selector")
st.write("Add these emojis to your post for extra flair!")

import streamlit as st

# Categories of emojis
emojis = {
    "Smileys": ["😀", "😂", "😎", "😇", "🤩", "😅", "😍", "😏", "😋", "🤔"],
    "Actions": ["👍", "👎", "💪", "🙏", "👏", "🤷‍♂️", "🤷‍♀️", "🙄", "🎉", "😱"],
    "Symbols": ["💼", "💯", "⭐", "🔥", "🚀", "⚡", "💔", "💖", "🌟", "🌈"],
    "Objects": ["🍕", "🍔", "🎁", "🏆", "📚", "✈️", "🖥️"],
}

# Tabs for categories
tab1, tab2, tab3, tab4 = st.tabs(emojis.keys())

selected_emojis = []

with tab1:
    selected_emojis += st.multiselect("Select Smileys:", emojis["Smileys"], default=[])
with tab2:
    selected_emojis += st.multiselect("Select Actions:", emojis["Actions"], default=[])
with tab3:
    selected_emojis += st.multiselect("Select Symbols:", emojis["Symbols"], default=[])
with tab4:
    selected_emojis += st.multiselect("Select Objects:", emojis["Objects"], default=[])

# Display selected emojis in a text area
if selected_emojis:
    user_input = st.text_input("Enter your text here:")
    st.text_area(
        "Your Text with Emojis",
        f"{user_input} {' '.join(selected_emojis)}",
        height=100
    )

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

