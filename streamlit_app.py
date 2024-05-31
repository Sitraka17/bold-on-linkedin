import streamlit as st

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

# Streamlit app
st.title("LinkedIn Text Formatter")
st.write("Enter your text below to transform it into bold text for LinkedIn:")

# Text input from user
user_input = st.text_area("Enter your text here")

if user_input:
    bold_output = bold_text(user_input)
    st.write("Transformed Bold Text:")
    st.write(f"**{bold_output}**")

# Donation button on the main page
st.markdown(
    """<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'C0C6YRSIF');kofiwidget2.draw();</script> 
""",
    unsafe_allow_html=True,
)

# Donation button in the sidebar
with st.sidebar:
    st.markdown(
        """
 <a href='https://ko-fi.com/C0C6YRSIF' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi1.png?v=3' 
 border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>     
    """,
        unsafe_allow_html=True,
    )
