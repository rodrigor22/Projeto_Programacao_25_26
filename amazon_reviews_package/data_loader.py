# -*- coding: utf-8 -*-
"""Leitura de Dados,Exceções e Logs"""
"""O propósito deste ficheiro é carregar o ficheiro CSV (Reviews.py), converter o mesmo numa lista de dicionários e tratar das exceções e logs"""
import csv

"""Esta função tem como objetivo ler o conteúdo do ficheiro CSV e armazená-lo numa lista de dicionários"""
def carregar_dados():
    # Lista vazia para armazenar os dicionários.(A estrutura final será [ {dados_da_review_1}, {dados_da_review_2}, ... ]
    dados = []
    file_path = "C:\\Users\\rodri\\Documents\\Ficheiro Trabalhos"
    file_name = "Reviews.csv"

    try:
        # Abertura do ficheiro no modo de leitura ("r")
        with open(file_path + file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for review in reader:
                # Conversão de tipos de dados
                # "HelpfullnessNumerator":Número de pessoas que consideraram a avaliação útil.(conversão de string para int)
                # "HelpfullnessDenominator":Número total de votos sobre a utilidade da avaliação.(conversão de string para int)
                #"Score": Avaliação dada (de 1 a 5 estrelas).(conversão de string para int)
                # Cria o dicionário da review
                review_dict = {
                    "Id": review["Id"],
                    "ProductId": review["ProductId"],
                    "UserId": review["UserId"],
                    "ProfileName": review["ProfileName"],
                    "HelpfulnessNumerator": int(review["HelpfulnessNumerator"]),
                    "HelpfullnessDenominator": int(review["HelpfulnessDenominator"]),
                    "Score": int(review["Score"]),
                    "Time": review["Time"],
                    "Summary": review["Summary"],
                    "Text": review["Text"]
                }
                # Adiciona o dicionário da review à lista 'dados'.
                dados.append(review_dict)

        # Retorna a lista completa de dicionários
        return dados

    except FileNotFoundError:
        print("ERROR: File not found")


