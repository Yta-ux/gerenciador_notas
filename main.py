import os
import pandas as pd
from libs import notas, reports, earnings

def menu(title, options):
    print(f"\033[1m{title}\033[0m")
    for x, option in enumerate(options, start=1):
        print(f"[{x}] {option}")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("\033[31mOpção inválida. Por favor, digite um número.\033[0m")
        return None

def main_menu(data):
    while True:
        user_option = menu("MENU PRINCIPAL", ["Realizar buscas", "Verificar rendimentos", "Gerar relatórios", "Sair"])
        if user_option == 1:
            search_menu(data)
        elif user_option == 2:
            earnings_menu(data)
        elif user_option == 3:
            report_menu(data)
        elif user_option == 4:
            print("Saindo...")
            break
        else:
            print('\033[31mOpção inválida, digite novamente.\033[0m')

def search_menu(data):
    option = menu("BUSCA DE ALUNOS", ["Matrícula", "Nome", "Sexo", "Status"])
    if option in range(1, 5):
        notas.generate_search_students(data, option)
    else:
        print('\033[31mOpção inválida, retornando ao menu principal.\033[0m')

def earnings_menu(data):
    option = menu("RENDIMENTOS GERAIS", ["Visualizar dados", "Distribuição com base no sexo", "Distribuição das médias por aluno", "Distribuição com base na frequência de médias", "Gerar relatório geral das análises"])
    if option in range(1, 6):
        earnings.generate_earnings_class(data, option)
    elif option == 6:
        return
    else:
        print('\033[31mOpção inválida.\033[0m')

def report_menu(data):
    option = menu("MODELO DO RELATÓRIO", ["TXT", "Markdown", "Xlsx"])
    if option in range(1, 4):
        reports.generate_reports(data, option)
    elif option == 4:
        return
    else:
        print('\033[31mOpção inválida.\033[0m')

# Execução principal
print("\033[1mGERENCIADOR DE NOTAS\033[0m")
name_sheet = input('Digite o nome da planilha (Deve estar no diretório "sua_panilha"): ')

if os.path.isfile(f"sua_planilha/{name_sheet}.xlsx"):
    data = pd.read_excel(f'sua_planilha/{name_sheet}.xlsx', sheet_name='notas')
    main_menu(data)
else:
    print("\033[31mPlanilha não encontrada.\033[0m")
