import streamlit as st

# Configuration des pages
st.set_page_config(
    page_title="Application de Texte",
    page_icon=":memo:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Sidebar pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Formatage de Texte", "Ajout d'Émoji", "Donation"])

# Page 1: Formatage de Texte
if page == "Formatage de Texte":
    st.title("Formatage de Texte")
    
    user_text = st.text_area("Entrez votre texte ici:")
    
    if st.button("Mettre en Gras"):
        st.markdown(f"**{user_text}**")
    
    if st.button("Mettre en Italique"):
        st.markdown(f"*{user_text}*")
    
    if st.button("Mettre en Gras Italique"):
        st.markdown(f"***{user_text}***")

# Page 2: Ajout d'Émoji
elif page == "Ajout d'Émoji":
    st.title("Ajout d'Émoji")
    
    user_text = st.text_area("Entrez votre texte ici:")
    
    emojis = ["😊", "😂", "😍", "🥺", "😭", "😎", "👍", "🎉"]
    selected_emoji = st.selectbox("Choisissez un émoji à ajouter:", emojis)
    
    if st.button("Ajouter l'Émoji"):
        st.write(user_text + " " + selected_emoji)

# Page 3: Donation
elif page == "Donation":
    st.title("Donation")
    st.write("Si vous aimez cette application, pensez à offrir un café ou un trophée au créateur.")
    
    coffee_url = "https://www.buymeacoffee.com"
    trophy_url = "https://www.patreon.com"
    
    st.markdown(f"[Offrir un Café]({coffee_url})")
    st.markdown(f"[Offrir un Trophée]({trophy_url})")
