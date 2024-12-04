import streamlit as st

# Streamlit page configuration
st.set_page_config(
    page_title="LinkedIn Text Formatter",
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

# Functions for italic and bold italic conversions (unchanged)
# ...

# Function to add emojis and copy result to clipboard
def add_emojis(text, emoji):
    formatted_text = f"{emoji} {text} {emoji}"
    st.code(formatted_text, language="plaintext")
    st.copy_to_clipboard(formatted_text)
    st.success("Copied to clipboard!")

# Streamlit UI setup
st.title("LinkedIn Text Formatter")
st.write("Enter your text below to transform it into bold, italic, or bold italic text for LinkedIn:")

# User input and selections
user_input = st.text_area("Enter your text here")
transformation_type = st.selectbox("Choose the transformation type", ["Bold", "Italic", "Bold Italic", "Add Emoji"])
emoji = st.selectbox("Choose an emoji", ["😀", "😂", "😎", "🥳", "👍", "🔥", "💯", "🚀", "⭐", "💼"])

# Transform and copy button
if st.button("Transform"):
    if user_input:
        if transformation_type == "Bold":
            transformed_output = bold_text(user_input)
        elif transformation_type == "Italic":
            transformed_output = italic_text(user_input)
        elif transformation_type == "Bold Italic":
            transformed_output = bold_italic_text(user_input)
        elif transformation_type == "Add Emoji":
            add_emojis(user_input, emoji)
            transformed_output = None  # No further display needed after copying

        if transformed_output:
            st.write("Transformed Text:")
            st.write(transformed_output)
            st.copy_to_clipboard(transformed_output)
            st.success("Text copied to clipboard!")

# Donation buttons (unchanged)
# ...
