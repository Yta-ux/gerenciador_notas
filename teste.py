import pandas as pd

turma = {
    'alunos': [],
    'notas': []
}

def Menu():
    print('\n(1) Adicionar alunos e notas')
    print('(2) SAIR')

usuario = 0

while usuario != 2:
    Menu()
    usuario = int(input('\nDigite sua opção: '))

    if usuario == 2:
        print('ATIVIDADES ENCERRADAS!')
        break
    elif usuario == 1:
        quantidade_aluno = int(input('Quantos alunos deseja cadastrar? '))
        
        for _ in range(quantidade_aluno):
            nome_aluno = input('Digite o nome do aluno: ')
            turma['alunos'].append(nome_aluno)

            nota_aluno = input('Digite a lista de notas do aluno separadas por espaço: ')
            
            notas = list(map(float, nota_aluno.split(' ')))
            turma['notas'].append(notas)

        t = pd.DataFrame(turma)

        t['Media'] = t['notas'].apply(lambda notas: sum(notas) / len(notas) if len(notas) > 0 else 0)

        t['Status'] = t['Media'].apply(lambda media: 'aprovado' if media >= 6 else 'reprovado')

        print("\nMédias dos alunos:\n", t[['alunos', 'Media' , 'Status']])


            



























