import streamlit as st
#letzzzz go
# What could be added ? 
# A web app to have all the tools to help people to create content ? (dammmm BRO the idea is so common lol ) 
st.set_page_config(
        page_title="Emoji Text Formatter",
        page_icon="✨",
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
        '!': '❗', '?': '❓', '.': '⨀', ',': '⧫', '-': '⫷', '+': '⧿', '(': '⦅', ')': '⦆',
        '[': '⦃', ']': '⦄', '{': '⦅', '}': '⦆', '/': '⧄', '\\': '⧅', ':': '⧼', ';': '⧽',
        '&': '⦘', '*': '⦙', '@': '⦧', '#': '⦦', '$': '⦚', '%': '⦜', '^': '⦣', '_': '⦪',
        '=': '⦭', '~': '⧃', '<': '⫲', '>': '⫳', '|': '⦒', ' ': ' '
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
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9',
        '!': '!', '?': '?', '.': '.', ',': ',', '-': '-', '+': '+', '(': '(', ')': ')',
        '[': '[', ']': ']', '{': '{', '}': '}', '/': '/', '\\': '\\', ':': ':', ';': ';',
        '&': '&', '*': '*', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '_': '_',
        '=': '=', '~': '~', '<': '<', '>': '>', '|': '|', ' ': ' '
    }
    return ''.join(italic_dict.get(c, c) for c in text)

# Function to convert normal text to bold italic text
def bold_italic_text(text):
    bold_italic_dict = {
        'A': '𝑨', 'B': '𝑩', 'C': '𝑪', 'D': '𝑫', 'E': '𝑬', 'F': '𝑭', 'G': '𝑮',
        'H': '𝑯', 'I': '𝑰', 'J': '𝑱', 'K': '𝑲', 'L': '𝑳', 'M': '𝑴', 'N': '𝑵',
        'O': '𝑶', 'P': '𝑷', 'Q': '𝑸', 'R': '𝑹', 'S': '𝑺', 'T': '𝑻', 'U': '𝑼',
        'V': '𝑽', 'W': '𝑾', 'X': '𝑿', 'Y': '𝒀', 'Z': '𝒁',
        'a': '𝒂', 'b': '𝒃', 'c': '𝒄', 'd': '𝒅', 'e': '𝒆', 'f': '𝒇', 'g': '𝒈',
        'h': '𝒉', 'i': '𝒊', 'j': '𝒋', 'k': '𝒌', 'l': '𝒍', 'm': '𝒎', 'n': '𝒏',
        'o': '𝒐', 'p': '𝒑', 'q': '𝒒', 'r': '𝒓', 's': '𝒔', 't': '𝒕', 'u': '𝒖',
        'v': '𝒗', 'w': '𝒘', 'x': '𝒙', 'y': '𝒚', 'z': '𝒛',
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9',
        '!': '!', '?': '?', '.': '.', ',': ',', '-': '-', '+': '+', '(': '(', ')': ')',
        '[': '[', ']': ']', '{': '{', '}': '}', '/': '/', '\\': '\\', ':': ':', ';': ';',
        '&': '&', '*': '*', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '_': '_',
        '=': '=', '~': '~', '<': '<', '>': '>', '|': '|', ' ': ' '
    }
    return ''.join(bold_italic_dict.get(c, c) for c in text)

# Function to add emojis
def add_emojis(text, emoji):
    return f"{emoji} {text} {emoji}"

# Streamlit app
st.title("LinkedIn Text Formatter")
st.write("Enter your text below to transform it into bold, italic, or bold italic text for LinkedIn:")

# Text input from user
user_input = st.text_area("Enter your text here")

# Transformation type selection
transformation_type = st.selectbox("Choose the transformation type", ["Bold", "Italic", "Bold Italic", "Add Emoji"])

# Emoji selection
#emoji = st.selectbox("Choose an emoji", ["😀", "😂", "😎", "🥳", "👍", "🔥", "💯", "🚀", "⭐", "💼"])

import streamlit as st

# List of 50 emojis
emoji_options = [
    "😀", "😂", "😎", "🥳", "👍", "🔥", "💯", "🚀", "⭐", "💼", 
    "😇", "🤩", "😜", "🤔", "😋", "😆", "🙃", "😎", "😬", "😭", 
    "😱", "🥺", "😅", "🥴", "🤪", "😤", "😳", "😈", "👻", "💀", 
    "👽", "🤖", "🦄", "🐶", "🐱", "🐭", "🐹", "🦊", "🐻", "🐼", 
    "🐯", "🦁", "🐮", "🐷", "🐸", "🦋", "🌸", "🌼", "🌺", "🌈"
]

# Segregating categories
categories = {
    "Smileys": emoji_options[:10],
    "Animals": emoji_options[10:30],
    "Nature": emoji_options[30:]
}

# Create a sidebar for category selection
category = st.sidebar.selectbox("Choose a category", list(categories.keys()))

# Display emojis for the selected category
st.title(f"Emojis from the {category} category")
selected_emoji = st.selectbox("Pick an emoji", categories[category])


# Transform button
if st.button("Transform"):
    if user_input:
        if transformation_type == "Bold":
            transformed_output = bold_text(user_input)
        elif transformation_type == "Italic":
            transformed_output = italic_text(user_input)
        elif transformation_type == "Bold Italic":
            transformed_output = bold_italic_text(user_input)
        elif transformation_type == "Add Emoji":
            transformed_output = add_emojis(user_input, emoji)

        st.write("Transformed Text:")
        st.write(f"{transformed_output}")

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
