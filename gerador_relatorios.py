import pandas as pd
import os

def menu():
    print("[1] Txt")
    print("[2] MarkDown")
    print("[3] Xlsx")
    print("[4] Sair")
    while True:
        try:
            opc = int(input("Em qual formato você quer o relatorio? "))
            break
        except:
            print("Entrada invalida! Tente novamente.")
    
    return opc

if os.path.isfile("sua_planilha/modelo_planilha.xlsx"):

    alunos = pd.read_excel('sua_planilha/modelo_planilha.xlsx')
    alunos_dicionario = alunos.to_dict()
    alunos_dicionario['media'] = {}
    alunos_dicionario['status'] = {}

    for x in range(len(alunos)):
        media = (alunos_dicionario['nota1'][x] + alunos_dicionario['nota2'][x] + alunos_dicionario['nota3'][x] + alunos_dicionario['nota4'][x]) / 4

        alunos_dicionario['media'][x] = media

        alunos_dicionario['status'][x] = 'APROVADO' if media >= 7 else 'REPROVADO'

    if not os.path.exists('relatorios'):
        os.mkdir('relatorios')

    while True:
        opc = menu()

        if opc == 1:
            with open('relatorios/relatorio.txt', 'w') as arq:
                for x in range(len(alunos)):
                    arq.write(f"{alunos_dicionario['nome'][x]} {alunos_dicionario['media'][x]} {alunos_dicionario['status'][x]}\n")

        elif opc == 2:
            with open('relatorios/relatorio.md', 'w') as f:
                f.write("## Relatório de Notas\n")
                f.write("""| Alunos    | Notas | Status 
                | -------- | ------- | ------- |
                """)
                for x in range(len(alunos)):
                    f.write(f"""| {alunos_dicionario['nome'][x]}   | {alunos_dicionario['media'][x]}    | {alunos_dicionario['status'][x]} |
                """) 

        elif opc == 3:
            alunos = pd.DataFrame(alunos_dicionario)
            alunos.to_excel('relatorios/relatorio.xlsx', index=False)

        elif opc == 4:
            break

        else:
            print("Opção invalida!")

else:
    print("Planilha inexistente!")
    