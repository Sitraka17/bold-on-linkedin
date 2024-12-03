import streamlit as st
import warnings

def create_transformation_dict(transformation_type):
    """
    Create a transformation dictionary based on the type of text styling.
    
    Args:
        transformation_type (str): Type of text transformation ('bold', 'italic', 'bold_italic')
    
    Returns:
        dict: A dictionary mapping characters to their styled versions
    """
    # Base character sets
    base_chars = {
        'uppercase': {
            'bold': '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙',
            'italic': '𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡',
            'bold_italic': '𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁'
        },
        'lowercase': {
            'bold': '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳',
            'italic': '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻',
            'bold_italic': '𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛'
        }
    }
    
    # Numbers and symbols remain mostly the same across styles
    numbers = '0123456789'
    punctuation = '!?,-+()[]{}/:;&*@#$%^_=~<>|'
    
    # Create the transformation dictionary
    transformation_dict = {}
    
    # Add characters based on the transformation type
    for case, chars in base_chars.items():
        for i, char in enumerate(case):
            transformation_dict[char] = chars[transformation_type][i]
    
    # Add numbers and punctuation
    for char in numbers + punctuation + ' ':
        transformation_dict[char] = char
    
    # Important: Explicitly exclude period from transformation
    transformation_dict['.'] = '.'
    
    return transformation_dict

def transform_text(text, transformation_type=None, emoji=None):
    """
    Transform text based on the specified transformation type.
    
    Args:
        text (str): Input text to transform
        transformation_type (str, optional): Type of transformation
        emoji (str, optional): Emoji to add
    
    Returns:
        str: Transformed text
    """
    if not text:
        return ''
    
    if transformation_type == 'Bold':
        transformation_dict = create_transformation_dict('bold')
        transformed_text = ''.join(transformation_dict.get(c, c) for c in text)
    elif transformation_type == 'Italic':
        transformation_dict = create_transformation_dict('italic')
        transformed_text = ''.join(transformation_dict.get(c, c) for c in text)
    elif transformation_type == 'Bold Italic':
        transformation_dict = create_transformation_dict('bold_italic')
        transformed_text = ''.join(transformation_dict.get(c, c) for c in text)
    elif transformation_type == 'Add Emoji':
        transformed_text = f"{emoji} {text} {emoji}"
    else:
        transformed_text = text
    
    return transformed_text

# Streamlit app configuration
st.set_page_config(
    page_title="LinkedIn Text Formatter", 
    page_icon="✍️",
    layout="centered"
)

# Main app
def main():
    st.title("📝 LinkedIn Text Formatter")
    st.markdown("Transform your text for LinkedIn with cool styles!")

    # Sidebar for additional information
    with st.sidebar:
        st.image("SitrakasLogo.png", use_column_width=True)
        st.markdown("## About")
        st.info("Easily format your LinkedIn posts with special text styles!")
        
        # Donation buttons
        st.markdown("### Support the Project")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <a href='https://ko-fi.com/sitrakaforler' target='_blank'>
                <img height='36' style='border:0px;height:36px;' 
                src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' 
                border='0' alt='Buy Me a Coffee at ko-fi.com' />
                </a>
                """, 
                unsafe_allow_html=True
            )

    # User input section
    user_input = st.text_area("Enter your text here 👇", height=200)

    # Transformation options
    col1, col2 = st.columns(2)
    
    with col1:
        transformation_type = st.selectbox(
            "Choose the transformation type", 
            ["Bold", "Italic", "Bold Italic", "Add Emoji"]
        )
    
    with col2:
        emoji = st.selectbox(
            "Choose an emoji", 
            ["😀", "😂", "😎", "🥳", "👍", "🔥", "💯", "🚀", "⭐", "💼"]
        ) if transformation_type == "Add Emoji" else None

    # Transform button
    if st.button("Transform", type="primary"):
        if user_input:
            transformed_output = transform_text(
                user_input, 
                transformation_type, 
                emoji
            )
            
            st.subheader("Transformed Text:")
            st.code(transformed_output, language=None)
            
            # Copy to clipboard button
            st.button("📋 Copy to Clipboard", 
                      on_click=lambda: st.write(f"Copied: {transformed_output}"))

    # Footer
    st.markdown("---")
    st.markdown("*Made with ❤️ by Sitraka*")

if __name__ == "__main__":
    main()
