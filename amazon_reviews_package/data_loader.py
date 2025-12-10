# -*- coding: utf-8 -*-
"""O propósito deste ficheiro é carregar o ficheiro CSV (Reviews.py), converter o mesmo numa lista de dicionários e tratar das exceções"""

import csv
import os
from datetime import datetime

"""Esta função lê o ficheiro CSV e armazena os dados numa lista de dicionários, trata exceções (FileNoTFoundError) e converte o campo Time"""


def load_data(file_path):
    reviews_data = []  # Lista que irá conter todos os dicionários(reviews)
    try:
        #Abertura do ficheiro no modo de leitura ("r")
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)  # Criar um leitor csv que irá ler o conteúdo do ficheiro
            # Obter e tratar do cabeçalho
            try:
                header = next(header)
            except StopIterarion:
                log_message("Ficheiro vazio ou apenas com cabeçalho.", "ERROR")
                return []
            # Mapeamento do cabeçalho e remooção de espaços, pontuação e converte minúsculas chaves padronizadas
            column_map = [col.strip().replace(' ', '').replace('.', '').replace('/', '').replace('\\', '') for col in
                          header]

            # Iterar sobre as linhas de dados presentes no ficheiro
            for i, line in enumerate(reader):
                if not line:
                    continue
                # Erro para as linhas com número incorreto de colunas
                if len(line) != len(header):
                    log_message(f"Linha {i + 2}(índice {i} ignorada: Número de colunas incorreto. Linha {line}",
                                "ERROR")
                    continue
                try:
                    # Criação do dicionário para cada review
                    review = {}
                    # Garantir que os dados são atribuidos corretamente com base no mapeamento feito ao cabeçalho
                    for col_name, col_index in zip(column_map, range(len(header))):
                        value = line[col_index]
                        if col_name == "Time":
                            # Conversão para data legível e armazenamento
                            review["Time_Original"] = value
                            review["Time_Date"] = convert_timestamp_to_date(value)
                        elif col_name in ["Id", "ProductId", "UserId", "ProfileName", "Summary", "Text"]:
                            review[col_name] = value
                        elif col_name in ["HelpfulnessNumerator", "HelpfulnessDenominator", "Score"]:
                            # Conversão para inteiro (para cálculos futuros)
                            review[col_name] = int(value)
                        else:
                            # Capturar outras colunas que possam existir
                            review[col_name] = value
                    reviews_data.append(review)
                except ValueError as ve:
                    # Lidar com eros de conversão do tipo (ex: int("abc"))
                    log_message(f"Erro de formato de dados na linha {i + 2}: {ve}. Linha: {line}", "ERROR")
        log_message(f"Carregamento concluído. {len(reviews_data)} avaliaçoes carregadas.", "INFO")
    except FileNotFoundError:
        log_message(f"ERRO FATAL:O ficheiro não foi encontrado em: {file_path}", "ERROR")
        return None
    except Exception as e:
        log_message(f"Ocorreu um erro inesperado durante o carregamento: {e}", "ERROR")
        return None
    return reviews_data


















