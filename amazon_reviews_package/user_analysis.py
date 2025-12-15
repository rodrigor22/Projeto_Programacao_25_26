# -*- coding: utf-8 -*-

"""Análise de Utilizadores"""
"""
BREVE DESCRIÇÃO
Este módulo tem como objetivo analisar os utilizadores do conjunto
de dados de avaliações de produtos alimentares da Amazon.

DESCRIÇÃO DETALHADA
Neste módulo encontram-se funções que analisam o comportamento dos
utilizadores com base nas avaliações armazenadas em memória.
Permite identificar quais os utilizadores mais ativos, quais os que
contribuem com avaliações mais úteis e calcular a média de palavras
por avaliação. Todo o processamento é realizado utilizando apenas
estruturas de dados básicas da linguagem Python.
"""



def validate_reviews(reviews):
    """
    Valida se reviews é uma lista.
    """
    # CORREÇÃO: Lançar a exceção diretamente para ser capturada e propagada
    if type(reviews) != list:
        raise TypeError("reviews deve ser uma lista")


def users_with_most_reviews(reviews, top_n=10):
    """
    Devolve os utilizadores com maior número de avaliações.
    """
    try:
        validate_reviews(reviews)
    except TypeError:
        return []

    counter = {}

    for review in reviews:
        try:
            # CORREÇÃO: Usamos .get() e tratamos AttributeError se 'review' não for um dict
            user_id = review.get("UserId")
        except AttributeError:
            continue

        if user_id:
            try:
                counter[user_id] += 1
            except KeyError:
                counter[user_id] = 1

    return sorted(counter.items(), key=lambda x: x[1], reverse=True)[:top_n]


def most_helpful_users(reviews, top_n=10):
    """
    Identifica os utilizadores mais úteis com base
    no total de votos úteis.
    """
    try:
        validate_reviews(reviews)
    except TypeError:
        return []

    helpfulness = {}

    for review in reviews:
        try:
            # CORREÇÃO: Usamos .get() e Robustez na conversão de votos
            user_id = review.get("UserId")
            # Assume 0 se não encontrar a chave ou valor
            votes = int(review.get("HelpfulnessNumerator", 0))
        except (TypeError, ValueError):
            continue

        if user_id:
            try:
                helpfulness[user_id] += votes
            except KeyError:
                helpfulness[user_id] = votes

    return sorted(helpfulness.items(), key=lambda x: x[1], reverse=True)[:top_n]


def average_words_per_user(reviews):
    """
    Calcula a média de palavras por avaliação
    de cada utilizador.
    """
    try:
        validate_reviews(reviews)
    except TypeError:
        return {}

    stats = {}

    for review in reviews:
        try:
            # CORREÇÃO: Usamos .get() para evitar KeyError e atribuir valor padrão
            user_id = review.get("UserId")
            text = review.get("Text", "")
        except AttributeError:
            continue

        # Trata casos em que 'text' pode não ser uma string ou está vazio
        try:
            if not isinstance(text, str) or not text.strip():
                continue
        except AttributeError:
            continue

        word_count = len(text.split())

        try:
            stats[user_id][0] += word_count
            stats[user_id][1] += 1
        except KeyError:
            stats[user_id] = [word_count, 1]

    averages = {}

    for user_id in stats:
        try:
            averages[user_id] = stats[user_id][0] / stats[user_id][1]
        except ZeroDivisionError:
            averages[user_id] = 0

    return averages