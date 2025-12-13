# -*- coding: utf-8 -*-
"""Análise de Avaliações"""

"""Este ficheiro analisa as reviews, calculando as estatísticas das mesmas."""

def contar_distribuicao_scores(dados):
    """Esta função conta o número de reviews para cada score de 1 a 5.
    Args:
        dados ==> lista de dicionários (reviews) (criada pela função presente no data_loader.py)

    Returns:
        Dicionário no formato {Score (em int): contagem (em int}
        sendo a key do dicionário o Score o value atribuido a essa key é o número de vezes que esse Score é encontrado nas reviews"""

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

def media_scores_por_utilizador(dados):
    """Esta função calcula a media de scores por utilizador
    Args:
    dados ==> Lista de dicionários (reviews) (criada pela função presente no data_loader.py)

    Returns:
        Dicionário no formato score_medio_por_user = {userid (em str): media (em float)}
        sendo o userid a key do dicionário que indica o nome do id do utilizador e o valor dessa key a média entre a soma dos scores desse user e as reviews feitas por esse user"""
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

def avaliacao_maxima (dados):
    """Esta função identifica os produtos com maior número de avaliações com score 5
    Args:
        dados ==> Lista de dicionários (reviews) (criada pela função presente no data_loader.py)
    Returns:
        Dicionário (avl_max) dos produtos com reviews com 5 de score (contando o número de vezes que cada produto teve score = 5)"""

    avl_max = {}
    for review in dados:
        score = review.get("Score")
        product_id = review.get("ProductId")
        if score == 5:
            #Se a chave existir, soma 1 à contagem. Se for um produto novo, inicia a contagem em 1
            avl_max[product_id] = avl_max.get(product_id, 0) + 1

    return avl_max











