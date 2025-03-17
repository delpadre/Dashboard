import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Meu Dashboard Profissional",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização global com CSS
st.markdown(
    """
    <style>
        /* Fundo escuro para contraste */
        .stApp {
            background-color: #1E1E1E !important;
        }

        /* Sidebar estilizada */
        section[data-testid="stSidebar"] {
            background-color: #111111;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.5);
        }

        /* Estilo do conteúdo da sidebar */
        .sidebar .sidebar-content {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.5);
        }

        /* Navegação da sidebar */
        .stSidebarNav {
            background-color: #2b2b2b;
            border-radius: 10px;
        }

        /* Itens do menu */
        .sidebar .sidebar-item {
            font-size: 20px;
            font-weight: bold;
            color: #FFFFFF;
            margin-bottom: 12px;
            padding: 8px;
            border-radius: 8px;
            transition: background-color 0.3s ease, padding-left 0.3s ease;
        }

        /* Estilo da imagem de perfil */
        .stImage img {
            border-radius: 10px;
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Efeito hover na imagem */
        .stImage img:hover {
            transform: translateY(-5px) scale(1.1);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.6);
        }

        /* Estilo geral do texto */
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            color: #E0E0E0;
        }

        /* Estilo dos títulos */
        h1, h2 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: bold;
            color: #FF9F00;
        }

        /* Cabeçalho */
        header {
            background-color: #1E1E1E !important;
        }

        /* Títulos de seção */
        .section-title {
            font-size: 24px;
            font-weight: bold;
            color: #FFFFFF;
            margin-top: 20px;
        }

        /* Animação de fade-in */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 0.8s ease-in-out;
        }

        /* Estilo dos links sociais */
        .social-links {
            margin-top: 50px;
            text-align: left;
        }
        .social-links a {
            display: inline-flex;
            align-items: center;
            margin-right: 35px;
            text-decoration: none;
            color: #E0E0E0;
            font-size: 18px;
            font-family: 'Arial', sans-serif;
            transition: color 0.3s ease;
        }
        .social-links a:hover {
            color: #FF9F00;
        }
        .social-links img {
            width: 40px;
            height: 40px;
            margin-right: 12px;
            vertical-align: middle;
        }

        /* Estilo do contador de visitantes */
        .visitor-counter {
            margin-top: 50px;
            text-align: center;
        }
        .visitor-counter span {
            background-color: #2b2b2b;
            padding: 15px 25px;
            border-radius: 12px;
            color: #E0E0E0;
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            display: inline-block;
        }
        .visitor-counter span:hover {
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.5);
            transition: box-shadow 0.3s ease;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo da página Home
st.title("🏠 Home")
st.markdown(
    """
    <div class="fade-in">
        <p style="font-size: 20px; font-weight: bold;">Bem-vindo ao Meu Dashboard Profissional</p>
        <p style="font-size: 24px; color: #FFFFFF;">Rafael Jorge Del Padre</p>
        <p>Aqui você vai encontrar um pouco da minha paixão por tecnologia e esportes, além do meu gosto por novos desafios e aprendizado constante. Estou sempre buscando soluções criativas e resultados que façam a diferença – espero que curta explorar isso comigo!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Links sociais com ícones
st.markdown(
    """
    <div class="social-links fade-in">
        <a href="https://www.linkedin.com/in/rafaeldelpadre/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"> LinkedIn
        </a>
        <a href="mailto:delpadre40@gmail.com" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" alt="Email"> Email
        </a>
        <a href="https://github.com/delpadre" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub"> GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



# Sidebar com imagem de perfil
with st.sidebar:
    st.image("Perfil.jpeg", caption="Rafael Jorge Del Padre", use_container_width=True)