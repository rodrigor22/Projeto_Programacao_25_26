# -*- coding: utf-8 -*-
"""Calcula a média de todos os scores (pontuações) na lista de reviews fornecida."""
#A função recebe a lista criada pela função criada no ficheiro "data_loader.py"
def media_avaliacoes(dados):
    if not dados:
        return 0.0

    # Criamos uma lista através de uma list comprehension apenas dos scores em cada dicionário
    scores = [review["Score"] for review in dados]

    total_score = sum(scores)
    #A funcão dá-nos a média dos scores somando os valores todos de scores com o "sum(scores)" e divindo pela quantidade de scores existente na lista dado pelo "len(scores)"
    return total_score / len(dados)


def calcular_helpfulness_medio(dados):
    """
    Calcula a utilidade média (helpfulness ratio) de todas as reviews.
    """
    if not dados:
        return 0.0

    total_helpfulness_ratio = 0.0
    valid_reviews_count = 0

    for review in dados:
        numerator = review["HelpfulnessNumerator"]
        denominator = review["HelpfullnessDenominator"]

        if denominator > 0:
            ratio = numerator / denominator
            total_helpfulness_ratio += ratio
            valid_reviews_count += 1

    if valid_reviews_count > 0:
        return total_helpfulness_ratio / valid_reviews_count
    else:
        return 0.0

