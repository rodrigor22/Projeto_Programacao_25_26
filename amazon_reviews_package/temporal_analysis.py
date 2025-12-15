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
        # Cria um objeto datetime a partir do timestamp
        dt_object = datetime.datetime.fromtimestamp(timestamp)
        # Formata o objeto datetime para a string de saída desejada
        return dt_object.strftime(format_str)
    except Exception:
        # Captura qualquer erro (ex: timestamp inválido ou muito grande)
        return ""


def convert_unix_timestamp_to_date_readable(timestamp: str) -> str:
    """
    REQUISITO OBRIGATÓRIO: Converter corretamente o campo Time (em formato timestamp Unix)
    para uma data legível (ex.: YYYY-MM-DD)[cite: 64].

    Args:
        timestamp: O timestamp Unix como string (vindo da leitura do CSV).

    Returns:
        A data formatada em YYYY-MM-DD.
    """
    try:
        # Converte a string do CSV para inteiro
        unix_timestamp = int(timestamp)
        # Chama a função auxiliar para fazer a conversão no formato YYYY-MM-DD
        return _convert_timestamp_to_date_string(unix_timestamp, "%Y-%m-%d")
    except ValueError:
        # Lidar com exceção se a string não puder ser convertida em inteiro
        return ""


# --- Funções de Análise Temporal ---

def count_reviews_by_year(reviews: list) -> dict:
    """
    REQUISITO OBRIGATÓRIO: Contar quantas avaliações foram feitas por ano[cite: 66].

    Args:
        reviews: Uma lista de dicionários, onde cada dicionário é uma avaliação
                 (e deve conter a chave 'Time').

    Returns:
        Um dicionário onde as chaves são os anos (string YYYY) e os valores são
        o número total de avaliações nesse ano.
        Exemplo: {'2010': 1500, '2011': 4500}
    """
    reviews_per_year = {}
    yearformat = "%Y"  # Formato só para o ano

    for review in reviews:
        # Aceder ao valor do timestamp (assumindo que está em string no dicionário)
        timestamp_str = review.get('Time')

        if timestamp_str:
            try:
                unix_timestamp = int(timestamp_str)
                # Converte o timestamp para a string do ano
                year = _convert_timestamp_to_date_string(unix_timestamp, yearformat)

                if year:
                    # Contagem básica usando dicionário
                    if year in reviews_per_year:
                        reviews_per_year[year] += 1
                    else:
                        reviews_per_year[year] = 1
            except ValueError:
                # Se o timestamp não for um número, ignora a review
                continue

    return reviews_per_year


def identify_busiest_period(reviews: list, period_format: str = "%Y-%m") -> dict:
    """
    REQUISITO OBRIGATÓRIO: Identificar o mês e o ano com maior número de avaliações[cite: 65].

    Esta função é genérica e pode ser usada para encontrar o ano/mês mais movimentado.

    Args:
        reviews: Uma lista de dicionários com a chave 'Time'.
        period_format: O formato para o período ('%Y-%m' para Mês/Ano, '%Y' para Ano).

    Returns:
        Um dicionário com o período mais ocupado e a sua contagem:
        {'periodo': 'YYYY-MM', 'contagem': N}
    """
    reviews_per_period = {}  # Dicionário para armazenar as contagens por período

    for review in reviews:
        timestamp_str = review.get('Time')

        if timestamp_str:
            try:
                unix_timestamp = int(timestamp_str)
                # Converte o timestamp para o formato de período (ex: "2010-04")
                period = _convert_timestamp_to_date_string(unix_timestamp, period_format)

                if period:
                    # Contagem
                    if period in reviews_per_period:
                        reviews_per_period[period] += 1
                    else:
                        reviews_per_period[period] = 1
            except ValueError:
                continue

    if not reviews_per_period:
        return {'periodo': None, 'contagem': 0}

    # Lógica para encontrar o período com a maior contagem sem usar a função max complexa
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
    (ex.: score médio por mês ou ano) [cite: 67].

    Args:
        reviews: Uma lista de dicionários com as chaves 'Time' e 'Score'.
        period: O período de agregação ('year' para ano, 'month' para mês/ano).

    Returns:
        Um dicionário onde as chaves são os períodos (YYYY ou YYYY-MM) e os valores
        são o score médio nesse período.
        Exemplo: {'2010-04': 4.2, '2010-05': 4.5}
    """
    # scores_by_period armazena [soma_scores, contagem_reviews] para cada período
    scores_by_period = {}

    # Define o formato de data com base no período de agregação solicitado
    if period == 'year':
        format_str = "%Y"
    elif period == 'month':
        format_str = "%Y-%m"
    else:
        # Usa o formato padrão se o argumento 'period' for inválido
        format_str = "%Y-%m"

    for review in reviews:
        timestamp_str = review.get('Time')
        score_str = review.get('Score')

        if timestamp_str and score_str is not None:
            try:
                unix_timestamp = int(timestamp_str)
                review_score = int(score_str)

                # Determinar a chave do período (YYYY ou YYYY-MM)
                key = _convert_timestamp_to_date_string(unix_timestamp, format_str)

                if key:
                    # Inicializa a lista [soma_scores, contagem_reviews] se o período for novo
                    if key not in scores_by_period:
                        scores_by_period[key] = [0, 0]

                    # Atualiza a soma total do score e o contador de reviews para o período
                    scores_by_period[key][0] += review_score
                    scores_by_period[key][1] += 1

            except (ValueError, TypeError):
                # Ignora reviews se o timestamp ou o score não forem números válidos
                continue

    # --- Calcular as Médias ---
    average_scores = {}
    for key, data in scores_by_period.items():
        total_score = data[0]
        count = data[1]

        if count > 0:
            # Calcula a média (divisão float)
            average_scores[key] = total_score / count

    return average_scores