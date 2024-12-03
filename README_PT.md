# Pokedata

- [English Version](README.md)

## Introdução
Este repositório apresenta um website desenvolvido como parte de um projeto de **Análise Prospectiva de Dados**, que explora a mediocridade dos Pokémon em relação aos seus tipos. O objetivo principal é analisar padrões e gerar insights a partir de dados relacionados aos atributos dos Pokémon.

## Estrutura do Projeto
O desenvolvimento foi realizado utilizando a plataforma **Google Colab**, com o suporte de diversas bibliotecas do ecossistema Python para manipulação de dados, visualização e hospedagem da aplicação.

Assim como, a estrutura dele consiste em três arquivos Python (.py):
- [projeto](projeto.py): Contém o Streamlit do website.
- [colab](colab.py): Contém todas as funções, dados e dataframes os quais o website acessa.
- [imagens](imagens.py): Contém os endereços para as imagens exibidas no website (que não visualizações).
 
## Tecnologias e Bibliotecas Utilizadas
1. **Pandas:** Manipulação e análise de dados através de DataFrames.
2. **Matplotlib:** Criação de visualizações para representar padrões e tendências nos dados.
3. **NumPy:** Realização de cálculos matemáticos e operações numéricas avançadas.
4. **Streamlit:** Hospedagem e interface interativa para o website.
5. **Local Tunnel:** Integração entre o ambiente de desenvolvimento do Google Colab e a aplicação Streamlit para disponibilizar o website de forma acessível e portátil.

## Visualizações e Funcionalidades
Desenvolvemos a aplicação para disponibilizar quatro tipos distintos de visualizações para o usuário:
1. **Relação Média de Atributos:** Um gráfico de radar comparativo entre o Tipo/Pokemon e a média Pokemon geral.
2. **Dispersão Ofensividade/Defensividade:** Um gráfico de dispersão considerando a relação de OFensividade (total dos atributos ofensivos) e Defensividade (total de atributos defensivos).
3. **Relação Média de Altura:** Um gráfico de barras comparativo entre um humano médio, o Tipo/Pokemon e a média Pokemon geral.
4. **Relação Média de Peso:** Um gráfico de barras comparativo entre um humano médio, o Tipo/Pokemon e a média Pokemon geral.

Além disso, o website conta com mais duas funcionalidades:
1. **Pokemon Médio:** Encontra o Pokemon mais médio de determinado Tipo.
2. **Pokemon Mais Forte/Fraco:** Encontra os Pokemon mais forte e mais fraco de determinado Tipo.

## Como acessar
- [Tutorial](Tutorial_Como_abrir_o_projeto.pdf)
