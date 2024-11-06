import os
import pandas as pd
from libs import notas, reports, earnings

def message_format(mensagem, tipo="info"):
    cores = {
        "info": "\033[1m",
        "erro": "\033[31m",
        "sucesso": "\033[32m"
    }
    print(f"{cores[tipo]}{mensagem.upper()}\033[0m")

#Exibe o menu e retorna a opção escolhida pelo usuário.
def menu(title, options):
    print(f"\033[1m{title}\033[0m")
    for x, option in enumerate(options, start=1):
        print(f"[{x}] {option}")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return None

# Menu principal
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
            message_format("Saindo...", "info")
            break
        else:
            message_format("Opção inválida, digite novamente.", "erro")

# Definem a função de cada um dos menus, além de adicionar o fluxo de retorno
def search_menu(data):
    option = menu("BUSCA DE ALUNOS", ["Matrícula", "Nome", "Sexo", "Status", "Voltar"])
    if option in range(1, 5):
        notas.generate_search_students(data, option)
    elif option == 5:
        return
    else:
        message_format("Opção inválida, retornando ao menu principal.", "erro")

def earnings_menu(data):
    option = menu("RENDIMENTOS GERAIS", [
        "Visualizar dados", "Distribuição com base no sexo",
        "Distribuição das médias por aluno", "Distribuição com base na frequência de médias",
        "Gerar relatório geral das análises", "Voltar"
    ])
    if option in range(1, 6):
        earnings.generate_earnings_class(data, option)
    elif option == 6:
        return
    else:
        message_format("Opção inválida, retornando ao menu principal.", "erro")

def report_menu(data):
    option = menu("MODELO DO RELATÓRIO", ["TXT", "Markdown", "Xlsx", "Voltar"])
    if option in range(1, 4):
        reports.generate_reports(data, option)
    elif option == 4:
        return
    else:
        message_format("Opção inválida, retornando ao menu principal.", "erro")

# Carrega os dados da planilha, se o tipo tiver correto
def load_data(type_sheet, name_sheet):
    path = f"sua_planilha/{name_sheet}.{type_sheet}"
    try:
        if type_sheet == "xlsx":
            return pd.read_excel(path, sheet_name='notas')
        elif type_sheet == "csv":
            return pd.read_csv(path, decimal=',')
        message_format("Arquivo encontrado.", "sucesso")
    except FileNotFoundError:
        message_format("Planilha não encontrada.", "erro")
    except Exception as e:
        message_format(f"Erro ao carregar o arquivo: {str(e)}", "erro")
    return None

# Encapsula todo o código em uma função para ser chamada no início
def init_project():
    message_format("GERENCIADOR DE NOTAS", "info")
    type_sheet = input('Digite o tipo de arquivo (xlsx ou csv): ').strip().lower()

    if type_sheet not in ['xlsx', 'csv']:
        message_format("Tipo de arquivo inválido.", "erro")
        return

    name_sheet = input('Digite o nome da planilha (Deve estar no diretório "sua_planilha"): ').strip()

    data = load_data(type_sheet, name_sheet)
    if data is not None:
        main_menu(data)

# Execução principal
if __name__ == "__main__":
    init_project()
