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


class UsersAnalysis:
    """
    Classe responsável pela análise do comportamento
    dos utilizadores com base nas avaliações.
    """

    def __init__(self, reviews):
        """
        Inicializa a classe e valida se reviews é uma lista.
        """
        try:
            if type(reviews) != list:
                raise TypeError
            self.reviews = reviews
        except TypeError:
            raise TypeError("reviews deve ser uma lista")

    def users_with_most_reviews(self, top_n=10):
        """
        Devolve os utilizadores com maior número de avaliações.
        """
        counter = {}

        for review in self.reviews:
            """
            Tenta obter o UserId da avaliação.
            Se falhar, ignora essa avaliação.
            """
            try:
                user_id = review["UserId"]
            except (TypeError, KeyError):
                continue

            if user_id:
                """
                Incrementa o contador de avaliações
                do utilizador.
                """
                try:
                    counter[user_id] += 1
                except KeyError:
                    counter[user_id] = 1

        """
        Ordena os utilizadores pelo número de avaliações
        e devolve apenas os top_n.
        """
        return sorted(counter.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def most_helpful_users(self, top_n=10):
        """
        Identifica os utilizadores mais úteis com base
        no total de votos úteis.
        """
        helpfulness = {}

        for review in self.reviews:
            """
            Tenta obter o UserId e os votos úteis.
            Se HelpfulnessNumerator não existir,
            assume o valor 0.
            """
            try:
                user_id = review["UserId"]
                votes = review["HelpfulnessNumerator"]
            except KeyError:
                try:
                    user_id = review["UserId"]
                    votes = 0
                except (TypeError, KeyError):
                    continue
            except TypeError:
                continue

            if user_id:
                """
                Soma os votos úteis ao utilizador.
                """
                try:
                    helpfulness[user_id] += votes
                except KeyError:
                    helpfulness[user_id] = votes

        """
        Ordena os utilizadores pelo total de votos úteis
        e devolve apenas os top_n.
        """
        return sorted(helpfulness.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def average_words_per_user(self):
        """
        Calcula a média de palavras por avaliação
        de cada utilizador.
        """
        stats = {}

        for review in self.reviews:
            """
            Tenta obter o UserId e o texto da avaliação.
            Se falhar, ignora a avaliação.
            """
            try:
                user_id = review["UserId"]
                text = review["Text"]
            except (TypeError, KeyError):
                continue

            """
            Verifica se o texto é uma string não vazia.
            """
            try:
                if not text.strip():
                    continue
            except AttributeError:
                continue

            """
            Atualiza o total de palavras e o número
            de avaliações do utilizador.
            """
            try:
                stats[user_id][0] += len(text.split())
                stats[user_id][1] += 1
            except KeyError:
                """
                Primeira avaliação do utilizador.
                """
                stats[user_id] = [len(text.split()), 1]

        averages = {}

        """
        Calcula a média de palavras por avaliação
        para cada utilizador.
        """
        for user_id in stats:
            try:
                averages[user_id] = stats[user_id][0] / stats[user_id][1]
            except ZeroDivisionError:
                averages[user_id] = 0

        return averages