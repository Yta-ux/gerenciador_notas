import pandas as pd

def generate_search_students(data, option):
# Matrícula ------------------------------------------------
    if option == 1:

        numero_matricula = int(input('Digite o numero de matrícula: '))
        aluno_por_matricula = data[data['matricula'] == numero_matricula]

        if not aluno_por_matricula.empty:
            print(aluno_por_matricula[['matricula', 'nome', 'sexo', 'nota1', 'nota2', 'nota3', 'nota4']])
        else:
            print('\033[31mNÚMERO DE MATRÍCULA NÃO ENCONTRADO!\033[0m')

# Nome -------------------------------------------------------------------
    elif option == 2:
        nome_aluno = input('Digite o nome do aluno: ').capitalize()
        por_nome = data[data['nome'] == nome_aluno]

        if not por_nome.empty:
            print(por_nome[['matricula', 'nome', 'sexo', 'nota1', 'nota2', 'nota3', 'nota4']])
        else:
            print('\033[31mALUNO NÃO ENCONTRADO\033[0m')

# Sexo -------------------------------------------------
    elif option == 3:
        sexo_aluno = input('Por qual sexo deseja buscar: ').capitalize()
        por_sexo = data[data['sexo'] == sexo_aluno]

        if not por_sexo.empty:
            print(por_sexo[['matricula', 'nome', 'sexo', 'nota1', 'nota2', 'nota3', 'nota4']])
        else:
            print('\033[31mPESQUISA NÃO ENCONTRADA\033[0m')
# Status --------------------------------------------------------
    elif option == 4:
        data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)
        data['status'] = data['media'].apply(lambda media: 'aprovado' if media >= 6 else 'reprovado')
        s_aluno = input('Status dos alunos deseja observar: ').lower()
        por_status = data[data['status'] == s_aluno]
        
        if not por_status.empty:
            print(por_status[['matricula', 'nome', 'sexo', 'nota1', 'nota2', 'nota3', 'nota4']])
        else:
            print('\033[31mPESQUISA NÃO ENCONTRADA\033[0m')
    else:
        print('\033[31mOpção inválida\033[0m')
