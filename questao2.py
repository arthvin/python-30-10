from pyDatalog import pyDatalog


pyDatalog.create_terms('Colaborador, Projeto, ParticipaDe, DepartamentoColaborador, NomeColaborador, NomeProjeto, Departamento')


def adicionar_fato_colaborador(nome):
    +Colaborador(nome)


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
            nome, _, departamento = linha.strip().split(',')
            adicionar_fato_colaborador(nome)
            adicionar_fato_departamento(nome, departamento)
            print(f"Fato adicionado: Colaborador({nome}), Departamento({departamento})")  


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


resultado = ParticipaDe(NomeColaborador, NomeProjeto) & DepartamentoColaborador(NomeColaborador, Departamento)


print("Colaboradores, Projetos e Departamentos:")
for r in resultado:
    print(f"Colaborador: {r[0]}, Projeto: {r[1]}, Departamento: {r[2]}")
