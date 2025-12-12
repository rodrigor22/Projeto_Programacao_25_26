# -*- coding: utf-8 -*-
"""Análise de Avaliações"""

"""Este ficheiro analisa as reviews, calculando as estatísticas das mesmas."""

"""Esta função calcula a média de todos os scores na lista de reviews fornecida."""
#A função recebe a lista criada pela função criada no ficheiro "data_loader.py"
def media_avaliacoes_geral(dados):
    if not dados:
        return 0.0
    # Criamos uma lista através de uma list comprehension apenas dos scores em cada dicionário
    scores = [review["Score"] for review in dados]
    total_score = sum(scores)
    #A funcão dá-nos a média dos scores somando os valores todos de scores com o "sum(scores)" e divindo pela quantidade de scores existente na lista dado pelo "len(scores)"
    return total_score / len(dados)

"""Esta função calcula a utilidade média de todas as reviews"""
def calcular_utilidade_media(dados):
    total_helpfulness_ratio = 0.0
    valid_reviews_count = 0
    for review in dados:
        numerator = review["HelpfulnessNumerator"]
        denominator = review["HelpfullnessDenominator"]

        if denominator > 0:
            utilidade_da_review = numerator / denominator
            # O "total_helpfulless_ratio" simboliza o sumatório de review["HelpfulnessNumerator"]/review["HelpfullnessDenominator"]
            total_helpfulness_ratio += utilidade_da_review
            # O "valid_reviews_count" simboliza o número de reviews válidas (que o denomidanor não seja igual a 0)
            valid_reviews_count += 1
        # Ignorar reviews quando review["HelpfullnessDenominator"] == 0
        else:
            pass
    if valid_reviews_count > 0:
        utilidade_media = total_helpfulness_ratio / valid_reviews_count
        return utilidade_media
    else:
        # Garante que um valor é sempre devolvido
        return 0.0

"""Esta função conta o número de reviews para cada score de 1 a 5."""
def contar_distribuicao_scores(dados):
    # Dicionário que armazena a contagem de cada score
    distribuicao = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    if not dados:
        return distribuicao
    # Itera sobre cada review
    for review in dados:
        #Tira a nota ("Score") de cada review
        score = review.get("Score")
        # Verifica se o score é um valor válido (entre 1 e 5) e soma ao value do score no dicionário "distribuição"
        if score in distribuicao:
            distribuicao[score] += 1

    return distribuicao

"""Esta função calcula a media de scores por utilizador"""
def media_scores_por_utilizador(dados):
    scores_totais = {}
    reviews_contadas = {}
    score_medio_por_user = {}

    for review in dados:
        # Score atribuido pelo user
        score = review.get("Score")
        # Id do user
        user_id = review.get("UserId")

        # Se o Id do user ja estiver presente na lista scores_totais, soma-se o valor da nova review à antiga e adiciona-se 1 ao número de reviews feitas pelo user
        if user_id in scores_totais:
            scores_totais[user_id] += score
            reviews_contadas[user_id] += 1
        # Se o Id do user for novo na lista scores_totais, atribui-se o valora da review atual como a única e iguala-se o número de reviews do user a 1
        else:
            scores_totais[user_id] = score
            reviews_contadas[user_id] = 1

    for user_id in scores_totais:
        # Não necessita de sum pois o ciclo for anterior ja fez a soma dos scores em cada avaliação por user
        soma_scores = scores_totais[user_id]
        contagem_reviews = reviews_contadas[user_id]
        media = soma_scores / contagem_reviews
        # Armazenamos a média calculada no dicionário final, usando o UserId como chave.
        score_medio_por_user[user_id] = media
    return score_medio_por_user

"""Esta função identifica os produtos com maior número de avaliações com score 5"""
def avaliacao_maxima (dados):
    avl_max = {}
    for review in dados:
        score = review.get("Score")
        product_id = review.get("ProductId")
        if score == 5:
            #Se a chave existir, soma 1 à contagem. Se for um produto novo, inicia a contagem em 1
            avl_max[product_id] = avl_max.get(product_id, 0) + 1

    return avl_max











