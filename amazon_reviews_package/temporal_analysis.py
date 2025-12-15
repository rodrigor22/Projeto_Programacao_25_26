# -*- coding: utf-8 -*-
"""Processo Temporal"""
import datetime

# --- Funções Auxiliares de Data ---

def _convert_timestamp_to_date_string(timestamp: int, format_str: str) -> str:
    """
    Função interna (privada, indicada pelo '_') para converter um timestamp Unix
    (número de segundos desde 01/01/1970) para uma string de data formatada.
    Lida com a lógica central da conversão.

    Args:
        timestamp: O valor do timestamp Unix (inteiro).
        format_str: O formato de saída desejado (ex: "%Y-%m-%d").

    Returns:
        A string de data formatada ou uma string vazia em caso de erro.
    """
    try:
        dt_object = datetime.datetime.fromtimestamp(timestamp)
        return dt_object.strftime(format_str)
    except Exception:
        return ""


def convert_unix_timestamp_to_date_readable(timestamp: str) -> str:
    """
    REQUISITO OBRIGATÓRIO: Converter corretamente o campo Time (em formato timestamp Unix)
    para uma data legível (ex.: YYYY-MM-DD).

    Args:
        timestamp: O timestamp Unix como string (vindo da leitura do CSV).

    Returns:
        A data formatada em YYYY-MM-DD.
    """
    try:
        unix_timestamp = int(timestamp)
        return _convert_timestamp_to_date_string(unix_timestamp, "%Y-%m-%d")
    except (ValueError, TypeError):
        # CORREÇÃO: Lida com exceção se a string for None ou não puder ser convertida em inteiro
        return ""


# --- Funções de Análise Temporal ---

def count_reviews_by_year(reviews: list) -> dict:
    """
    REQUISITO OBRIGATÓRIO: Contar quantas avaliações foram feitas por ano.

    Args:
        reviews: Uma lista de dicionários, onde cada dicionário é uma avaliação
                 (e deve conter a chave 'Time').

    Returns:
        Um dicionário onde as chaves são os anos (string YYYY) e os valores são
        o número total de avaliações nesse ano.
        Exemplo: {'2010': 1500, '2011': 4500}
    """
    reviews_per_year = {}
    yearformat = "%Y"

    for review in reviews:
        timestamp_str = review.get('Time')

        if timestamp_str:
            try:
                # CORREÇÃO: Robustez na conversão para inteiro
                unix_timestamp = int(timestamp_str)
                year = _convert_timestamp_to_date_string(unix_timestamp, yearformat)

                if year:
                    if year in reviews_per_year:
                        reviews_per_year[year] += 1
                    else:
                        reviews_per_year[year] = 1
            except (ValueError, TypeError):
                continue

    return reviews_per_year


def identify_busiest_period(reviews: list, period_format: str = "%Y-%m") -> dict:
    """
    REQUISITO OBRIGATÓRIO: Identificar o mês e o ano com maior número de avaliações.

    Esta função é genérica e pode ser usada para encontrar o ano/mês mais movimentado.

    Args:
        reviews: Uma lista de dicionários com a chave 'Time'.
        period_format: O formato para o período ('%Y-%m' para Mês/Ano, '%Y' para Ano).

    Returns:
        Um dicionário com o período mais ocupado e a sua contagem:
        {'periodo': 'YYYY-MM', 'contagem': N}
    """
    reviews_per_period = {}

    for review in reviews:
        timestamp_str = review.get('Time')

        if timestamp_str:
            try:
                # CORREÇÃO: Robustez na conversão para inteiro
                unix_timestamp = int(timestamp_str)
                period = _convert_timestamp_to_date_string(unix_timestamp, period_format)

                if period:
                    if period in reviews_per_period:
                        reviews_per_period[period] += 1
                    else:
                        reviews_per_period[period] = 1
            except (ValueError, TypeError):
                continue

    if not reviews_per_period:
        return {'periodo': None, 'contagem': 0}

    max_count = 0
    busiest_period = None

    for period, count in reviews_per_period.items():
        if count > max_count:
            max_count = count
            busiest_period = period

    return {'periodo': busiest_period, 'contagem': max_count}


def calculate_average_score_over_time(reviews: list, period: str = 'month') -> dict:
    """
    REQUISITO OBRIGATÓRIO: Analisar a variação do score médio ao longo do tempo
    (ex.: score médio por mês ou ano).

    Args:
        reviews: Uma lista de dicionários com as chaves 'Time' e 'Score'.
        period: O período de agregação ('year' para ano, 'month' para mês/ano).

    Returns:
        Um dicionário onde as chaves são os períodos (YYYY ou YYYY-MM) e os valores
        são o score médio nesse período.
        Exemplo: {'2010-04': 4.2, '2010-05': 4.5}
    """
    scores_by_period = {}

    if period == 'year':
        format_str = "%Y"
    elif period == 'month':
        format_str = "%Y-%m"
    else:
        format_str = "%Y-%m"

    for review in reviews:
        timestamp_str = review.get('Time')
        score_str = review.get('Score')

        if timestamp_str and score_str is not None:
            try:
                # CORREÇÃO: Robustez na conversão para inteiro para Time e Score
                unix_timestamp = int(timestamp_str)
                review_score = int(score_str)

                key = _convert_timestamp_to_date_string(unix_timestamp, format_str)

                if key:
                    if key not in scores_by_period:
                        scores_by_period[key] = [0, 0]

                    scores_by_period[key][0] += review_score
                    scores_by_period[key][1] += 1

            except (ValueError, TypeError):
                continue

    average_scores = {}
    for key, data in scores_by_period.items():
        total_score = data[0]
        count = data[1]

        if count > 0:
            average_scores[key] = total_score / count

    return average_scores