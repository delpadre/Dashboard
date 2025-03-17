import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm, binom
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.markdown(
    """
    <style>
        /* Fundo escuro para contraste */
        .stApp {
            background-color: #1E1E1E !important;
        }
        
        /* Sidebar (menu nativo) com cor escura */
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

        /* Estilizando a imagem do perfil */
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
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar com imagem e nome
with st.sidebar:
    st.image("Perfil.jpeg", caption="Rafael Jorge Del Padre", use_container_width=True)

# Título da página
st.title("📊 Análise de Dados")
st.write("Análise de dados aplicada ao acesso a água potável e saneamento (WHO/UNICEF).")

# Carregando o banco de dados
file_path = "pages/Sleep_Efficiency_Updated.csv"
df = pd.read_csv(file_path)

# Exibindo o banco de dados
st.write("### Visualização dos Dados")
st.dataframe(df.head())
st.write("Colunas disponíveis:", df.columns.tolist())

# Opções de análise
st.write("### Selecione as análises desejadas")
analises = st.multiselect("Escolha as análises:", [
    "Apresentação dos Dados e Tipos de Variáveis",
    "Medidas Centrais e Dispersão",
    "Correlação entre Variáveis",
    "Aplicação de Distribuições Probabilísticas"
])

# Apresentação dos dados e tipos de variáveis
if "Apresentação dos Dados e Tipos de Variáveis" in analises:
    st.write("## 📌 Apresentação dos Dados e Tipos de Variáveis")
    st.write(df.dtypes)
    st.write("Principais perguntas de análise:")
    st.write("- Como as variáveis influenciam a eficiência do sono?")
    st.write("- Existe correlação entre fatores como idade e tempo total de sono?")
    st.write("- Quanto mais sono profundo eu tiver, menor sera meu sono rem?")
    

# Medidas Centrais e Dispersão
if "Medidas Centrais e Dispersão" in analises:
    st.write("## 📊 Medidas Centrais e Dispersão")
    df_numerico = df.select_dtypes(include=np.number)  # Filtrar apenas colunas numéricas
    
    st.write("Média:", df_numerico.mean())
    st.write("Mediana:", df_numerico.median())
    st.write("Moda:", df_numerico.mode().iloc[0])
    st.write("Desvio Padrão:", df_numerico.std())
    
    if "Sleep efficiency" in df_numerico.columns:
        fig, ax = plt.subplots()
        sns.histplot(df_numerico["Sleep efficiency"].dropna(), kde=True, ax=ax)
        ax.set_title("Distribuição da Eficiência do Sono")
        st.pyplot(fig)
        st.write("\n")
        st.write(" Interpretação: A distribuição parece assimétrica, com uma cauda à esquerda (valores menores de eficiência são menos frequentes), o que sugere que a maioria das pessoas tem sono eficiente, enquanto casos de baixa eficiência são exceções. A presença da curva indica que os dados podem seguir uma distribuição aproximada de uma campainha (normal ou semelhante), mas com uma inclinação para valores mais altos de eficiência.")
        st.write("Conclusões Possíveis: A amostra analisada (seja de indivíduos, noites de sono ou outro critério) tende a ter uma qualidade de sono elevada, com a maioria alcançando eficiência acima de 90%.")
        st.write("Poderia haver um viés na coleta de dados, como a inclusão de pessoas com bons hábitos de sono ou o uso de dispositivos que favorecem registros de alta eficiência.Valores abaixo de 0,7 são raros, o que pode indicar que pessoas com sono muito fragmentado ou problemas de insônia estão sub-representadas.")
        st.write("Se você tiver mais contexto sobre os dados (como a fonte ou o tamanho da amostra), posso refinar a análise. Caso queira uma investigação mais detalhada, posso oferecer buscar informações adicionais!.")
        

# Correlação entre variáveis
if "Correlação entre Variáveis" in analises:
    st.write("## 🔍 Correlação entre Variáveis")
    df_corr = df.select_dtypes(include=np.number)  # Garantir que apenas colunas numéricas sejam analisadas
    corr = df_corr.corr()
    fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
    st.write("Iterpretação: Fatores que mais afetam a eficiência do sono:O consumo de cafeína (-0,91) e os despertares (-0,81) são os fatores mais fortemente associados a uma menor eficiência do sono.  consumo de álcool também tem um impacto negativo moderado (-0,39).  porcentagem de sono REM (0,62) e a frequência de exercícios (0,28) têm associações positivas com a eficiência do sono.")
    st.write("Relação entre as fases do sono: ono profundo e sono leve têm uma forte correlação negativa (-0,97), indicando que eles competem pelo tempo total de sono. Sno REM tem uma correlação positiva moderada com eficiência do sono (0,62), sugerindo que um sono mais eficiente pode favorecer o sono REM.")
    st.write("Estilo de vida: afeína e álcool têm impactos negativos claros na qualidade do sono, aumentando despertares e sono leve, e reduzindo a eficiência e o sono profundo. xercícios têm um efeito positivo, mas relativamente fraco, na eficiência e nas fases do sono.")
    st.write("Poderia haver um viés na coleta de dados, como a inclusão de pessoas com bons hábitos de sono ou o uso de dispositivos que favorecem registros de alta eficiência.Valores abaixo de 0,7 são raros, o que pode indicar que pessoas com sono muito fragmentado ou problemas de insônia estão sub-representadas.")
    st.write("\n")

if "Aplicação de Distribuições Probabilísticas" in analises:
    st.write("## 🎲 Aplicação de Distribuições Probabilísticas")
    
    if "Sleep efficiency" in df.columns:
        sleep_efficiency = df["Sleep efficiency"].dropna()
        
        if not sleep_efficiency.empty:
            mu, sigma = sleep_efficiency.mean(), sleep_efficiency.std()
            x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
            y = norm.pdf(x, mu, sigma)
            fig, ax = plt.subplots()
            ax.plot(x, y, label="Distribuição Normal", color='orange')
            ax.set_title("Distribuição Normal da Eficiência do Sono")
            st.pyplot(fig)
            st.write("\n")
            st.write("A distribuição normal foi escolhida porque a eficiência do sono é uma variável contínua e tende a seguir uma distribuição simétrica em torno da média. Isso permite analisar a dispersão e a probabilidade de diferentes níveis de eficiência do sono.")
            st.write("\n")
            
            # Distribuição Binomial
            n = 10  # Número de noites analisadas
            p = min(max(mu, 0.01), 0.99)  # Probabilidade baseada na média do dataset
            x_binom = np.arange(0, n + 1)
            y_binom = binom.pmf(x_binom, n, p)
            
            fig, ax = plt.subplots()
            ax.bar(x_binom, y_binom, color='blue', alpha=0.7, label="Distribuição Binomial")
            ax.set_title("Distribuição Binomial da Eficiência do Sono")
            ax.set_xlabel("Número de Noites com Boa Eficiência do Sono")
            ax.set_ylabel("Probabilidade")
            ax.legend()
            
            st.pyplot(fig)
            st.write("\n")
            st.write("A distribuição binomial foi escolhida para modelar a probabilidade de uma pessoa ter um certo número de noites com boa eficiência do sono em um período de 10 noites. Como a eficiência do sono pode ser interpretada como um sucesso ou falha em cada noite, a binomial se ajusta bem a esse contexto.")
            st.write("\n")
        else:
            st.write("⚠️ Não há dados suficientes para calcular as distribuições.")
    else:
        st.write("⚠️ A coluna 'Sleep efficiency' não está disponível no dataset.")

st.write("### 🚀 Análise Concluída! Selecione novas opções para explorar mais insights.")