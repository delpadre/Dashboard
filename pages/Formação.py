import streamlit as st

# Aplica o estilo global para a página
st.markdown(
    """
    <style>
        .stApp {
            background-color: #1E1E1E !important;
        }
        
        section[data-testid="stSidebar"] {
            background-color: #111111;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.5);
        }

        /* Estilo da sidebar */
        .sidebar .sidebar-content {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.5);
        }


        /* Estilo para o menu de navegação */
        .stSidebarNav {
            background-color: #2b2b2b;
            border-radius: 10px;
        }

        /* Itens do menu */
        .sidebar .sidebar-item {
            font-size: 20px;
            font-weight: bold;
            color: white;
            margin-bottom: 12px;
            padding: 8px;
            border-radius: 8px;
            transition: background-color 0.3s ease, padding-left 0.3s ease;
        }
        
        .stImage img {
    border-radius: 10px;
    transform: translateY(-5px) scale(1.05);  /* Efeito de zoom e elevação */
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4); /* Sombra para destacar a imagem */
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transição suave */
}

/* Efeito hover: A imagem ficará mais zoomada e a sombra ficará mais forte */
.stImage img:hover {
    transform: translateY(-5px) scale(1.1); /* Aumento do zoom e mais elevação */
    box-shadow: 0 12px 25px rgba(0, 0, 0, 0.6); /* Sombra mais forte */
}
        /* Ajustes gerais para texto */
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            color: #E0E0E0;
        }

        /* Ajuste de fonte em headings */
        h1, h2 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: bold;
            color: #FF9F00;
        }
        
        /* Estilizando o cabeçalho */
        header {
            background-color: #1E1E1E !important;  /* Adicionando a mesma cor de fundo */
        }

        /* Melhorando a formatação dos textos */
        .section-title {
            font-size: 24px;
            font-weight: bold;
            color: white;
            margin-top: 20px;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 0.8s ease-in-out;
        }
        

        /* Estilizando o cabeçalho */
        header {
            background-color: #1E1E1E !important;  /* Adicionando a mesma cor de fundo */
        }

        /* Melhorando a formatação dos textos */
        .section-title {
            font-size: 24px;
            font-weight: bold;
            color: white;
            margin-top: 20px;
        }

        .content {
            font-size: 18px;
            color: white;
            line-height: 1.6;
        }

        /* Estilizando as colunas */
        .metric-box {
            text-align: center;
            padding: 10px;
            background-color: #333333;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown("<h1 class='title'>🎓 Formação e Experiência</h1>", unsafe_allow_html=True)

# Seção de Graduação
st.markdown("<h2 class='section-title'>🏫 Formação Acadêmica</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p class='content'>
    🎓 <b>Defesa Cibernética</b> - Faculdade de Informática e Administração Paulista (2021 - 2023) <br>
    🎓 <b>Engenharia de Software</b> - Faculdade de Informática e Administração Paulista (2023 - 2027) <br>
    🏆 <b>Projetos Acadêmicos:</b> <br>
    - Aplicativo de conexão entre mecânicos e clientes <br>
    - Desenvolvimento de um dashboard profissional <br>
    - Programa de suporte para espécies marinhas invasoras
    </p>
    """, 
    unsafe_allow_html=True
)

# Seção de Cursos
st.markdown("<h2 class='section-title'>📖 Cursos e Certificações</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p class='content'>
        ✅ Implementando Banco de Dados - Fundação Bradesco <br>
        ✅ Git e Github- Compartilhando e colaborando em projetos - Alura <br>
        ✅ Gestão e Infraestrutura de TI - Fiap
    </p>
    """, 
    unsafe_allow_html=True
)

# Seção de Experiência Profissional
st.markdown("<h2 class='section-title'>💼 Experiência Profissional</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p class='content'>
        🔹 <b>Estagiário</b> - Semi Sistemas e Automação Hidrelétrica (2024 - Presente) <br>
        🛠 Desenvolvimento de Softwares (CLP) e automação de processos internos utilizando C#, JS e SQLServer <br>
        🛠 Desenvolvimento e suporte de telas para engenheiros para que possam comandar a usina <br>
    </p>
    """, 
    unsafe_allow_html=True
)

# Exibindo Métricas
st.markdown("<h2 class='section-title'>📊 Estatísticas Profissionais</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-box'>🛠  5+ Projetos Desenvolvidos</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-box'>🎓 3+ Certificações Concluídas</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-box'>💡 1 Ano de Experiência</div>", unsafe_allow_html=True)


# Criando o menu nativo na sidebar
with st.sidebar:
    # Exibindo a imagem no topo
    st.image("Perfil.jpeg", caption="Rafael Jorge Del Padre", use_container_width=True)