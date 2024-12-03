# Pokedata

- [Versão em Português](README_PT.md)

## Introduction
This repository presents a website developed as part of a **Prospective Data Analysis** project, which explores the mediocrity of Pokémon in relation to their types. The main objective is to analyze patterns and generate insights based on data related to Pokémon attributes.

## Project Structure
The development was carried out using the **Google Colab** platform, supported by various Python libraries for data manipulation, visualization, and application hosting.

Additionally, the project structure consists of three Python (.py) files:
- [projeto](projeto.py): Contains the Streamlit implementation of the website.
- [biblio](biblio.py): Contains all functions, data, and dataframes accessed by the website.
- [imagens](imagens.py): Contains the URLs for images displayed on the website (not related to visualizations).

## Technologies and Libraries Used
1. **Pandas:** Data manipulation and analysis using DataFrames.
2. **Matplotlib:** Creation of visualizations to represent patterns and trends in the data.
3. **NumPy:** Performing advanced mathematical calculations and numerical operations.
4. **Streamlit:** Hosting and interactive interface for the website.
5. **Local Tunnel:** Integration between the Google Colab development environment and the Streamlit application to make the website accessible and portable.

## Visualizations and Features
The application provides four distinct types of visualizations for the user:
1. **Average Attribute Comparison:** A radar chart comparing the Type/Pokémon with the overall Pokémon average.
2. **Offensiveness/Defensiveness Scatter Plot:** A scatter plot analyzing the relationship between Offensiveness (sum of offensive attributes) and Defensiveness (sum of defensive attributes).
3. **Average Height Comparison:** A bar chart comparing an average human, the Type/Pokémon, and the overall Pokémon average.
4. **Average Weight Comparison:** A bar chart comparing an average human, the Type/Pokémon, and the overall Pokémon average.

Additionally, the website offers two extra features:
1. **Average Pokémon:** Finds the most average Pokémon of a given Type.
2. **Strongest/Weakest Pokémon:** Finds the strongest and weakest Pokémon of a given Type.

## How to Access
- [Tutorial](Tutorial_EN.pdf)

