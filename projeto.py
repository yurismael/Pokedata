import streamlit as st
import numpy as np 
import colab as pkm
import matplotlib.pyplot as plt
import imagens as pki

# Customização
st.set_page_config(page_title="PokéData")

# Menu 
st.sidebar.title("Menu")
paginas = ['Home','Introdução', 'Explorar', 'Detalhes']
pagina_atual = st.sidebar.radio('Ir para:', paginas)

# Páginas
# Página inicial
if pagina_atual == 'Home':
  st.title("Bem-vindo ao PokéData!")
  st.write(
    """
    Este projeto visa explorar e visualizar dados sobre Pokémon e seus tipos de forma interativa. 
    Através da plataforma Streamlit, oferecemos uma interface intuitiva para analisar 
    estatísticas, tipos, características e outras informações sobre seus Pokémon favoritos.
    """
  )
  st.write('Recomendamos a leitura da **"Introdução"**.')
  # Tutorial
  st.header("Como usar:")
  st.markdown(
    """
    1. Acesse, pelo Menu lateral, a página "Explorar"
    2. Selecione um tipo deseja visualizar.
    3. Decida se deseja escolher seu Pokémon favorito (ou não).
    4. Escolha as projeções desejadas ou outras funcionalidades curiosas.
    5. Explore os gráficos para analisar os dados.
    5. Divirta-se!
    """
  )

  st.header("Funcionalidades:")
  st.markdown(
    """
    * Visualizar estatísticas de cada Pokémon (HP, Ataque, Defesa, etc.).
    * Filtrar Pokémon por tipo.
    * Comparar as estatísticas de diferentes Pokémon e seus tipos.
    * Explorar a distribuição e tendência de tipos entre os Pokémon.
    * Encontrar os Pokémon médios, fracos ou fortes entre seus tipos.
    """
  )
  st.markdown("**<center>Esperamos que você aproveite a jornada pelo mundo Pokémon!</center>**", unsafe_allow_html=True)

# Página principal
elif pagina_atual == 'Explorar':
  # Explorar
  st.header("Explorar:")
  tipoE = st.selectbox("Escolha o tipo:", pkm.df['type1'].unique())

  escolher = st.checkbox("Escolher um Pokémon")
  if escolher:
    pokemon = st.selectbox("Escolha o Pokémon:", pkm.df_tipo[tipoE]['name'].unique())
  else:
    pokemon = None

  # Checkboxes para os gráficos a serem exibidos
  st.write("Escolha os gráficos para exibição:")
  col1, col2, col3 = st.columns(3)
  grafs = [0, 0, 0, 0, 0, 0]

  with col1:
    grafs[0] = st.checkbox("Exibir gráfico de atributos.")
    grafs[1] = st.checkbox("Exibir gráfico de dispersão.")
  with col2:
    grafs[2] = st.checkbox("Exibir gráfico de altura.")
    grafs[3] = st.checkbox("Exibir gráfico de peso.")
  with col3:
    grafs[4] = st.checkbox("Pokémon médio.")
    grafs[5] = st.checkbox("Mais fraco / Mais forte.")

  # Customizando o botão
  st.markdown("""
    <style>
    div.stButton > button:first-child {
        width: 100%;
    }
    </style>""", unsafe_allow_html=True)

  if st.button('Começar análise!'):
    if grafs[0]:
      fig = pkm.plotar_stats(tipoE, pokemon_nome = pokemon)
      st.pyplot(fig)
    if grafs[1]:
      fig = pkm.plotar_disper(tipoE, pokemon_nome = pokemon)
      st.pyplot(fig)
    if grafs[2]:
      fig = pkm.plotar_altura(tipoE, pokemon_nome = pokemon)
      st.pyplot(fig)
    if grafs[3]:
      fig = pkm.plotar_peso(tipoE, pokemon_nome = pokemon)
      st.pyplot(fig)
    if grafs[4]:
      medio = pkm.pokemon_medio(tipo = tipoE)
      st.write(f"O Pokémon médio do tipo é **{medio}**")
      
      im_medio = pki.imagens_pokemon[medio]
      
      st.markdown   (
                    f"""
                    <style>
                    .center {{
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                        width: 200;
                    }}
                    </style>
                    <img src="{im_medio}" class="center">
                    """,
                    unsafe_allow_html=True,
                    )
      
    if grafs[5]:
      fraco, forte = pkm.pokemons_extremos(tipoE)
      
      st.write(f'O mais fraco do tipo é **{fraco}**')
      im_fraco = pki.imagens_pokemon[fraco]
      
      st.markdown   (
                    f"""
                    <style>
                    .center {{
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                        width: 200;
                    }}
                    </style>
                    <img src="{im_fraco}" class="center">
                    """,
                    unsafe_allow_html=True,
                    )
      
      st.write(f'O mais forte do tipo é **{forte}**')
      im_forte = pki.imagens_pokemon[forte]
      
      st.markdown   (
                    f"""
                    <style>
                    .center {{
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                        width: 200;
                    }}
                    </style>
                    <img src="{im_forte}" class="center">
                    """,
                    unsafe_allow_html=True,
                    )

elif pagina_atual == 'Introdução':
  # O Pokémon Médio
  poke_nome = pkm.pokemon_medio()
  pokemon = pkm.df[pkm.df['name'] == poke_nome] 
  tipo = pokemon['type1'].values[0]
  
  # Introdução
  st.write(
  """
  O que é um Pokémon médio?
  """)
  st.write("""
  A resposta é, de certa forma, impossível de ser dada. 
  Dependendo do método de julgamento, um Pokémon médio pode variar.
  Podemos abordar essa resposta pelos seguintes valores:
  """
  )
  st.markdown("""
  1. Estágio evolutivo
  2. Altura
  3. Geração
  4. Número da Pokedéx
  """)
  st.write("Entre outros...")
  st.write(
  """
  As respostas, a partir desses parâmetros, seriam, naturalmente distintas - às vezes múltiplas, dependendo do método.
  Dessa forma, nós, da Pokédata, nos propusemos a respondé-la a partir da perspectiva de seus atributos básicos - aqueles de vital importância nos jogos.
  E esse foi o resultado que atingimos:
  """)
  
  # Plotando gráfico
  fig = pkm.plotar_geral( )
  st.pyplot(fig)

  st.write(
  """
  Obviamente, esse gráfico não diz muito. 
  Mas, um Pokémon médio seria um que se aproximasse desse formato, dessa distribuição.
  Então, a pergunta que não quer calar: 
  """)
  st.markdown('**<center>"Qual o Pokémon mais médio hoje existente?"</center>**', unsafe_allow_html = True)
  st.write(f'A resposta é... rufem os tambores... **{poke_nome}**!')

  # Imagem do Pokémon
  st.markdown(
    """
    <style>
    .image-container {
        float: left; /* or float: right; */
        margin: 10px; 
        align-items: center;
    }
    </style>

    <div class = "image-container">
        <img src= 'https://archives.bulbagarden.net/media/upload/thumb/f/ff/0351Castform.png/250px-0351Castform.png' width="200"> 
    </div>

    Castform, o Pokémon Clima, é conhecido por sua habilidade única de mudar de forma de acordo com o clima. 
    Essa criatura adorável, de formato muito sugestivo, é capaz de se adaptar a diferentes condições climáticas, assumindo formas distintas em cada clima.
    Em dias ensolarados, Castform se transforma em um pequeno sol com nuvens. 
    Sob chuva, ele se torna numa grande gota d'água com nuvens. 
    E em tempestades de granizo, Castform assume a forma de um pequeno tornado com, advinhe, nuvens.
    """,
    unsafe_allow_html=True,
  )
  st.write("Mas, vamos nos aprofundar nos motivos:")
  st.write(f"Esse é o formato de {poke_nome}:")

  # Gráfico com os dados do Pokémon
  fig = pkm.plotar_stats(tipo, pokemon_nome = poke_nome)
  st.pyplot(fig)

  st.write("O Pokémon, assim, é quase do formato perfeito de um Pokémon médio - se distinguindo apenas por ser um pouco mais fraco e ter uma defesa ligeiramente menor.")
  st.write("Vejamos a partir de outra perspectiva:")

  # Gráfico de dispersão com o Pokémon
  fig = pkm.plotar_disper(tipo, pokemon_nome = poke_nome)
  st.pyplot(fig)

  st.write("""
    Esse gráfico representa o equilíbrio entre ofensividade (atributos voltados para o ataque) e defensividade (atributos voltados para a defesa).
    Assim, a reta de cor prata, representa a razão padrão entre as características que um Pokémon médio teria. 
    Além disso, a reta na cor dos pontos, representa a razão padrão entre as características que um Pokémon médio no seu tipo teria.
    Importante ressaltar, também, é que o gráfico está em escala com o gráfico de radar anteriormente apresentado, assim, as regiões no gráfico apresenta significado relevante.
  """)
  st.write(f'''
    {poke_nome}, representado pelo ponto vermelho, se encontra numa região curiosa desse gráfico de dispersão - perfeitamente sob as retas médias.
    Mais importante ainda, {poke_nome} está na região central do gráfico, demonstrando atributos de mesma magnitude de um Pokémon médio.
  ''')
  st.write(f"Assim, o Pokémon {poke_nome} é, para nossa métrica, verdadeiramente, **o Pokémon Médio**!")

elif pagina_atual == 'Detalhes':
  st.title('O Dataframe')
  st.write("O Dataframe original utilizado nesse projeto pode ser acessado em:")
  st.write("[Dataframe - Kagle](https://www.kaggle.com/datasets/guavocado/pokemon-stats-1025-pokemons)")

  st.write('Após o tratamento preliminar desse dataframe - que inclui a eliminação de algumas colunas e separação por tipo - passamos a trabalhar com ele nesse formato:')
  
  tipoE = st.selectbox("Escolha o tipo:", pkm.df['type1'].unique())
  df_inicial = pkm.df_tipo[tipoE]
  st.dataframe(df_inicial)