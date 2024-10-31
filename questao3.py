from pyDatalog import pyDatalog


pyDatalog.create_terms('Colaborador, Projeto, ParticipaDe, DepartamentoColaborador, Senior, NomeColaborador, NomeProjeto, Departamento, Idade')


def adicionar_fato_colaborador(nome, idade):
    +Colaborador(nome)
    +Idade(nome, idade)


def adicionar_fato_projeto(nome):
    +Projeto(nome)


def adicionar_fato_participacao(nome_colaborador, nome_projeto):
    +ParticipaDe(nome_colaborador, nome_projeto)


def adicionar_fato_departamento(nome_colaborador, departamento):
    +DepartamentoColaborador(nome_colaborador, departamento)


def importar_dados_colaboradores(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            nome, idade, departamento = linha.strip().split(',')
            idade = int(idade) 
            adicionar_fato_colaborador(nome, idade)
            adicionar_fato_departamento(nome, departamento)
            print(f"Fato adicionado: Colaborador({nome}), Idade({idade}), Departamento({departamento})")  


def importar_dados_projetos(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            nome = linha.split(',')[0]  
            adicionar_fato_projeto(nome)
            print(f"Fato adicionado: Projeto({nome})")  


def importar_dados_alocacoes(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            nome_colaborador, nome_projeto = linha.strip().split(',')
            adicionar_fato_participacao(nome_colaborador, nome_projeto)
            print(f"Fato adicionado: ParticipaDe({nome_colaborador}, {nome_projeto})")  


importar_dados_colaboradores('colaboradores.txt')
importar_dados_projetos('projetos.txt')
importar_dados_alocacoes('alocacoes.txt')


Senior(NomeColaborador) <= Colaborador(NomeColaborador) & Idade(NomeColaborador, Idade) & (Idade > 30)


resultado_seniores = Senior(NomeColaborador) & DepartamentoColaborador(NomeColaborador, Departamento)


print("Colaboradores Sêniors e seus Departamentos:")
for r in resultado_seniores:
    print(f"Colaborador: {r[0]}, Departamento: {r[1]}")


departamento_contagem = {}
for r in resultado_seniores:
    dep = r[1]
    if dep in departamento_contagem:
        departamento_contagem[dep] += 1
    else:
        departamento_contagem[dep] = 1


print("\nContagem de Colaboradores Sêniors por Departamento:")
for dep, count in departamento_contagem.items():
    print(f"Departamento: {dep}, Colaboradores Sêniors: {count}")
