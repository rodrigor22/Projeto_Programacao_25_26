# -*- coding: utf-8 -*-
"""Leitura de Dados"""

"""O propósito deste ficheiro é carregar o ficheiro CSV (Reviews.py), converter o mesmo numa lista de dicionários e tratar das exceções e logs"""

import csv

def carregar_dados():
    """Esta função tem como objetivo ler o conteúdo do ficheiro CSV e armazená-lo numa lista de dicionários
    Args:
        O caminho (file_path) e nome do ficheiro CSV a ser lido ("Reviews.csv")
    Returns:
        Uma lista com o formato [ {Review 1}, {Review 2}, ... ], onde cada elemento é um dicionário que representa os dados de
        uma única review."""

    # Lista vazia para armazenar os dicionários.
    file_path = "C:\\Users\\rodri\\Documents\\Ficheiro Trabalhos"
    file_name = "Reviews.csv"

    try:
        with open(file_path + "\\" + file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            dados = []

            for review in reader:
                # Conversão de tipos de dados
                # "HelpfulnessNumerator":Número de pessoas que consideraram a avaliação útil.(conversão de string para int)
                # "HelpfulnessDenominator":Número total de votos sobre a utilidade da avaliação.(conversão de string para int)
                #"Score": Avaliação dada (de 1 a 5 estrelas).(conversão de string para int)
                # Cria o dicionário da review
                review_dict = {
                    "Id": review["Id"],
                    "ProductId": review["ProductId"],
                    "UserId": review["UserId"],
                    "ProfileName": review["ProfileName"],
                    # CORREÇÃO: Chave corrigida para 'HelpfulnessNumerator' (uma só 'l')
                    "HelpfulnessNumerator": int(review["HelpfulnessNumerator"]),
                    # CORREÇÃO: Chave corrigida para 'HelpfulnessDenominator' (uma só 'l')
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
    except KeyError as e:
        # Captura o erro de chave (ortografia) e permite que o main o imprima como erro crítico.
        raise Exception(f"Erro de chave na leitura do CSV: {e}")