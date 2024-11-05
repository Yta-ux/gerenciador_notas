import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def graphic_by_sex(data):
  genero_counts = data['sexo'].value_counts()
  plt.figure(figsize=(8, 8))
  plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', colors=['blue', 'red'])
  plt.title('Proporção de Gênero na Turma')
  plt.show()

def graphic_by_students(data):
  data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)

  media_alunos = data.groupby('nome')['media'].mean()

  plt.figure(figsize=(10, 6))
  media_alunos.plot(kind='bar', color='skyblue')
  plt.title('Média de rendimento por aluno')
  plt.xlabel('Nome do Aluno')
  plt.ylabel('Média')
  plt.xticks(rotation=45)
  plt.show()

def graphic_mean_frequency(data):
  data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)

  plt.figure(figsize=(10, 6))
  plt.hist(data['media'], bins=10, color='purple', alpha=0.7)
  plt.title('Distribuição das Médias das Notas')
  plt.xlabel('Média')
  plt.ylabel('Frequência')
  plt.show()

def generate_pdf(data):
  if not os.path.exists('reports'):
    os.mkdir('reports')

  with PdfPages('reports/relatorio_graficos.pdf') as pdf:
    data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)
    media_alunos = data.groupby('nome')['media'].mean()
    genero_counts = data['sexo'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', colors=['blue', 'red'])
    plt.title('Proporção de Gênero na Turma')
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(10, 6))
    media_alunos.plot(kind='bar', color='skyblue')
    plt.title('Média de rendimento por aluno')
    plt.xlabel('Nome do Aluno')
    plt.ylabel('Média')
    plt.xticks(rotation=45)
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.hist(data['media'], bins=10, color='purple', alpha=0.7)
    plt.title('Distribuição das Médias das Notas')
    plt.xlabel('Média')
    plt.ylabel('Frequência')

    plt.tight_layout()
    pdf.savefig()
    plt.close()

def generate_earnings_class(data, option):
  match option:
    case 1:
      print(data)
    case 2:
      graphic_by_sex(data)
    case 3:
      graphic_by_students(data)
    case 4:
      graphic_mean_frequency(data)
    case 5:
      generate_pdf(data)
    case _ :
      print('\033[31mOpção inválida, digite novamente.\033[0m')
