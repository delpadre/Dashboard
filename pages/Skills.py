import streamlit as st

st.markdown(
    """
    <style>
        /* Fundo escuro para melhor contraste e estética */
        .stApp {
            background-color: #1E1E1E !important;
            color: #E0E0E0;
            font-family: 'Arial', sans-serif;
        }

        /* Sidebar refinada */
        section[data-testid="stSidebar"] {
            background-color: #111111;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.6);
        }

        /* Conteúdo interno da sidebar */
        .sidebar-content {
            background-color: #1E1E1E;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4);
        }

        /* Links de navegação na sidebar */
        .stSidebarNav {
            background-color: #2B2B2B;
            border-radius: 10px;
            padding: 12px;
        }

        /* Estilo dos itens do menu */
        .sidebar-item {
            font-size: 18px;
            font-weight: 600;
            color: #FFFFFF;
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .sidebar-item:hover {
            background-color: #FF9F00;
            color: #111111;
            padding-left: 15px;
        }

        /* Estilização da imagem de perfil */
        .stImage img {
            border-radius: 10px;
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Hover na imagem */
        .stImage img:hover {
            transform: scale(1.08);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.6);
        }

        /* Estilo geral do texto */
        .stMarkdown {
            font-size: 16px;
            line-height: 1.6;
            color: #E0E0E0;
        }

        /* Títulos */
        h1, h2 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: bold;
            color: #FF9F00;
        }

        /* Cabeçalho refinado */
        header {
            background-color: #1E1E1E !important;
            padding: 10px;
        }

        /* Títulos das seções */
        .section-title {
            font-size: 22px;
            font-weight: bold;
            color: #FFFFFF;
            margin-top: 20px;
        }

        /* Animação suave de fade-in */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 0.6s ease-in-out;
        }

        /* Links sociais aprimorados */
        .social-links {
            margin-top: 40px;
            text-align: left;
        }
        .social-links a {
            display: inline-flex;
            align-items: center;
            margin-right: 30px;
            text-decoration: none;
            color: #E0E0E0;
            font-size: 16px;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        .social-links a:hover {
            color: #FF9F00;
        }
        .social-links img {
            width: 36px;
            height: 36px;
            margin-right: 10px;
            vertical-align: middle;
        }

        /* Contador de visitantes refinado */
        .visitor-counter {
            margin-top: 40px;
            text-align: center;
        }
        .visitor-counter span {
            background-color: #2B2B2B;
            padding: 12px 20px;
            border-radius: 10px;
            color: #E0E0E0;
            font-size: 16px;
            font-weight: bold;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
            display: inline-block;
            transition: box-shadow 0.3s ease;
        }
        .visitor-counter span:hover {
            box-shadow: 0 5px 12px rgba(0, 0, 0, 0.5);
        }
        
         /* Caixa de skills */
        .skill-box {
            background-color: #2B2B2B;
            padding: 15px;
            border-radius: 10px;
            color: #E0E0E0;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Hover nas caixas de skills */
        .skill-box:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.6);
        }
        
    </style>
    """,
    unsafe_allow_html=True
)


# Barra lateral
with st.sidebar:
    st.image("Perfil.jpeg", caption="Rafael Jorge Del Padre", use_container_width=True)

# Título principal
st.markdown("<h1>🛠 Skills</h1>", unsafe_allow_html=True)

# Seção de Hard Skills
st.markdown("<h2>💻 Hard Skills</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='skill-box'>🐍 Python</div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-box'>🗄 SQLServer</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='skill-box'>🌐 Desenvolvimento Web</div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-box'>☕ Java</div>", unsafe_allow_html=True)

# Seção de Soft Skills
st.markdown("<h2>🤝 Soft Skills</h2>", unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    st.markdown("<div class='skill-box'>🗣 Comunicação</div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-box'>💡 Criatividade</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='skill-box'>🛠 Resolução de Problemas</div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-box'>🤝 Trabalho em Equipe</div>", unsafe_allow_html=True)
