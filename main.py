# -*- coding: utf-8 -*-
from data_loader import carregar_dados
from review_analysis import contar_distribuicao_scores, media_scores_por_utilizador, media_scores_por_produto, \
    calculo_score_medio_ponderado, avaliacao_maxima
from temporal_analysis import _convert_timestamp_to_date_string, convert_unix_timestamp_to_date_readable, \
    count_reviews_by_year, identify_busiest_period, calculate_average_score_over_time
from user_analysis import users_with_most_reviews, most_helpful_users, average_words_per_user


def main():
    try:
        dados = carregar_dados()
        print("Dados carregados com sucesso.")
    except Exception as e:
        print(f"ERRO CRÍTICO: Falha ao carregar dados. O programa será encerrado. {e}")
        return

    while True:
        print("\n--- MENU ---")
        print("1 - Análise de Avaliações  ")
        print("2 - Processamento Temporal ")
        print("3 - Análise de Utilizadores ")
        print("0 - Sair")

        option_principal = input("Escolha uma opção: ")

        if option_principal == "1":
            while True:
                print("\n--- MENU ANÁLISE DE AVALIAÇÕES ---")
                print("1 - Contagem do número por score (1 a 5 estrelas)")
                print("2 - Média de avaliações por utilizador (Top 10)")
                print("3 - Produtos com maior número de avaliações com score 5 (Top 10)")
                print("4 - Score médio por produto (Top 10)")
                print("5 - Score médio ponderado por utilidade de avaliação (Top 10)")
                print("0 - Voltar ao Menu Principal")

                option_sub = input("Escolha uma opção do sub-menu: ")

                if option_sub == "1":
                    result = contar_distribuicao_scores(dados)
                    print("\nContagem do número por score (1 a 5 estrelas):", result)

                elif option_sub == "2":
                    result = media_scores_por_utilizador(dados)
                    top_10 = dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])
                    print("\nMédia de avaliações por utilizador (Top 10):", top_10)

                elif option_sub == "3":
                    result = avaliacao_maxima(dados)
                    top_10 = dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])
                    print("\nProdutos com maior número de avaliações com score 5 (Top 10):", top_10)

                elif option_sub == "4":
                    result = media_scores_por_produto(dados)
                    top_10 = dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])
                    print("\nScore médio por produto (Top 10):", top_10)

                elif option_sub == "5":
                    result = calculo_score_medio_ponderado(dados)
                    top_10 = dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])
                    print("\nScore médio ponderado por utilidade de avaliação (Top 10):", top_10)

                elif option_sub == "0":
                    break

                else:
                    print("Opção inválida no sub-menu. Tente novamente.")

        elif option_principal == "2":
            while True:
                print("\n--- MENU PROCESSAMENTO TEMPORAL ---")
                print("1 - Converter o campo Time para uma data legível (Amostra)")
                print("2 - Mês e o ano com maior número de avaliações")
                print("3 - Número de avaliações feitas por ano (Completo)")
                print("4 - Variação do score médio ao longo do tempo (Amostra)")
                print("0 - Voltar ao Menu Principal")

                option_sub = input("Escolha uma opção do sub-menu: ")

                if option_sub == "1":
                    timestamp_to_convert = dados[0].get('Time') if dados and dados[0].get('Time') else ""
                    result = convert_unix_timestamp_to_date_readable(timestamp_to_convert)
                    print("\nConversão do primeiro registro para data legível:", result)

                elif option_sub == "2":
                    result = identify_busiest_period(dados)
                    print("\nMês e o ano com maior número de avaliações:", result)

                elif option_sub == "3":
                    result = count_reviews_by_year(dados)
                    print("\nNúmero de avaliações feitas por ano:", result)

                elif option_sub == "4":
                    result = calculate_average_score_over_time(dados)
                    sample_5 = dict(list(result.items())[:5])
                    print("\nVariação do score médio ao longo do tempo (Amostra de 5 períodos):", sample_5)

                elif option_sub == "0":
                    break
                else:
                    print("Opção inválida no sub-menu. Tente novamente.")

        elif option_principal == "3":
            while True:
                print("\n--- MENU ANÁLISE DE UTILIZADORES ---")
                print("1 - Utilizadores com maior número de avaliações (Top 10)")
                print("2 - Utilizadores mais úteis (Top 10)")
                print("3 - Média de palavras por avaliação de cada utilizador (Top 10)")
                print("0 - Voltar ao Menu Principal")

                option_sub = input("Escolha uma opção do sub-menu: ")

                if option_sub == "1":
                    result = users_with_most_reviews(dados)
                    print("\nOs utilizadores com maior número de avaliações:", result)
                elif option_sub == "2":
                    result = most_helpful_users(dados)
                    print("\nOs utilizadores mais úteis são:", result)
                elif option_sub == "3":
                    result = average_words_per_user(dados)
                    top_10 = dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])
                    print("\nA Média de palavras por avaliação de cada utilizador (Top 10):", top_10)

                elif option_sub == "0":
                    break
                else:
                    print("Opção inválida no sub-menu. Tente novamente.")

        elif option_principal == "0":
            print("\nEncerrando o programa.")
            break
        else:
            print("Opção inválida no menu principal. Tente novamente.")


if __name__ == "__main__":
    main()