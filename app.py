import streamlit as st
import pandas as pd
# Importation des modules
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {
    'usernames': 
        {   
            'utilisateur': 
            {   'name': 'utilisateur',
                'password': 'utilisateurMDP',
                'email': 'utilisateur@gmail.com',
                'failed_login_attemps': 0, # Sera géré automatiquement
                'logged_in': False, # Sera géré automatiquement
                'role': 'utilisateur'},
            'root': 
            {   'name': 'root',
                'password': 'rootMDP',
                'email': 'admin@gmail.com',
                'failed_login_attemps': 0, # Sera géré automatiquement
                'logged_in': False, # Sera géré automatiquement
                'role': 'administrateur'
            }
        }
    }

# Lecture user csv
df_user = pd.read_csv('./data/users.csv')

#créer le dictionnaire lesDonneesDesComptes à partir de df_user sur la base de l'exemple fourni ci-dessus
lesDonneesDesComptes = {}
lesDonneesDesComptes['usernames'] = {}
for i in range(len(df_user)):
    lesDonneesDesComptes['usernames'][df_user['name'][i]] = {}  # Assuming 'name' is the username column
    lesDonneesDesComptes['usernames'][df_user['name'][i]]['name'] = df_user['name'][i]
    lesDonneesDesComptes['usernames'][df_user['name'][i]]['password'] = df_user['password'][i]
    lesDonneesDesComptes['usernames'][df_user['name'][i]]['email'] = df_user['email'][i]
    lesDonneesDesComptes['usernames'][df_user['name'][i]]['failed_login_attemps'] = 0
    lesDonneesDesComptes['usernames'][df_user['name'][i]]['logged_in'] = False
    lesDonneesDesComptes['usernames'][df_user['name'][i]]['role'] = df_user['role'][i]


authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    st.title("Bienvenue chez toi Full Blue Monthy")
    st.image("img4.png") 


def photos():
    st.title("Nos plus belles photos")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Le jeu")
        st.image("img3.png")

    with col2:
        st.header("du matin...")
        st.image("img1.png")

    with col3:
        st.header("du soir...")
        st.image("img2.png")


if st.session_state["authentication_status"]:
 
    with st.sidebar:
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue *{st.session_state["name"]}*")
        selected = option_menu(None,["Accueil", "Nos plus belles photos"], 
            icons=['star', 'key'], menu_icon="cast", default_index=0)
        selected

    if selected == "Accueil":
        accueil()
    elif selected == "Nos plus belles photos":
        photos()        

    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


