import os
import pandas as pd

def generate_reports(data, option):
    for col in ['nota1', 'nota2', 'nota3', 'nota4']:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    alunos = data
    alunos_dicionario = alunos.to_dict()
    alunos_dicionario['media'] = {}
    alunos_dicionario['status'] = {}

    for x in range(len(alunos)):
        media = (alunos_dicionario['nota1'][x] + alunos_dicionario['nota2'][x] + alunos_dicionario['nota3'][x] + alunos_dicionario['nota4'][x]) / 4
        alunos_dicionario['media'][x] = media
        alunos_dicionario['status'][x] = 'APROVADO' if media >= 7 else 'REPROVADO'
    
    if not os.path.exists('reports'):
        os.mkdir('reports')

    if option == 1:
        with open('reports/relatorio.txt', 'w') as arq:
            for x in range(len(alunos)):
                arq.write(f"{alunos_dicionario['nome'][x]} {alunos_dicionario['media'][x]} {alunos_dicionario['status'][x]}\n")

    elif option == 2:
        with open('reports/relatorio.md', 'w') as f:
            f.write("## Relatório de Notas\n")
            f.write("""| Alunos    | Notas | Status 
| -------- | ------- | ------- |\n""")
            for x in range(len(alunos)):
                f.write(f"|{alunos_dicionario['nome'][x]}|{alunos_dicionario['media'][x]}|{alunos_dicionario['status'][x]}\n")

    elif option == 3:
        alunos = pd.DataFrame(alunos_dicionario)
        alunos.to_excel('reports/relatorio.xlsx', index=False)

    else:
        print("\033[31mOpção inválida, digite novamente.\033[0m")
    