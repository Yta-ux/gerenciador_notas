import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Gera um gráfico de pizza para mostrar a proporção de gênero na turma.
def graphic_by_sex(data):
  genero_counts = data['sexo'].value_counts()  # Conta ocorrências de cada gênero
  plt.figure(figsize=(8, 8))
  plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', colors=['blue', 'red'])
  plt.title('Proporção de Gênero na Turma')
  plt.show()

# Gera um gráfico de barras mostrando a média de rendimento de cada aluno.
def graphic_by_students(data):
  data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)  # Calcula a média de cada aluno
  media_alunos = data.groupby('nome')['media'].mean()  # Agrupa por nome e calcula média

  plt.figure(figsize=(10, 6))
  media_alunos.plot(kind='bar', color='skyblue')
  plt.title('Média de rendimento por aluno')
  plt.xlabel('Nome do Aluno')
  plt.ylabel('Média')
  plt.xticks(rotation=45)
  plt.show()

# Gera um histograma para mostrar a distribuição das médias das notas.
def graphic_mean_frequency(data):
  data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)  # Calcula a média de cada aluno

  plt.figure(figsize=(10, 6))
  plt.hist(data['media'], bins=10, color='purple', alpha=0.7)  # Cria histograma
  plt.title('Distribuição das Médias das Notas')
  plt.xlabel('Média')
  plt.ylabel('Frequência')
  plt.show()

# Gera um relatório geral para os dados, com gráficos de pizza, barras e histograma
def generate_pdf(data):
  if not os.path.exists('reports'):
    os.mkdir('reports')  # Cria o diretório 'reports' caso não exista

  with PdfPages('reports/relatorio_graficos.pdf') as pdf:
  # Adiciona um gráfico de pizza com a proporção de gênero
    genero_counts = data['sexo'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', colors=['blue', 'red'])
    plt.title('Proporção de Gênero na Turma')
    pdf.savefig()  # Salva a página no PDF
    plt.close()

    # Adiciona gráfico de barras com a média de rendimento dos alunos
    data['media'] = data[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)
    media_alunos = data.groupby('nome')['media'].mean()
    plt.figure(figsize=(10, 6))
    media_alunos.plot(kind='bar', color='skyblue')
    plt.title('Média de rendimento por aluno')
    plt.xlabel('Nome do Aluno')
    plt.ylabel('Média')
    plt.xticks(rotation=45)
    pdf.savefig()
    plt.close()

    # Adiciona um histograma com a distribuição das médias das notas
    plt.figure(figsize=(10, 6))
    plt.hist(data['media'], bins=10, color='purple', alpha=0.7)
    plt.title('Distribuição das Médias das Notas')
    plt.xlabel('Média')
    plt.ylabel('Frequência')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

# Define o gráfico selecionado pelo usuário, a partir da opção desejada
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
        print('')
