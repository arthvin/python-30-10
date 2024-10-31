from pyDatalog import pyDatalog


pyDatalog.create_terms('Colaborador, Projeto, Nome')


def adicionar_fato_colaborador(nome):
    +Colaborador(nome)


def adicionar_fato_projeto(nome):
    +Projeto(nome)


def importar_dados_colaboradores(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            nome = linha.split(',')[0]  
            adicionar_fato_colaborador(nome)
            print(f"Fato adicionado: Colaborador({nome})")  


def importar_dados_projetos(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            nome = linha.split(',')[0]  
            adicionar_fato_projeto(nome)
            print(f"Fato adicionado: Projeto({nome})")  


importar_dados_colaboradores('colaboradores.txt')
importar_dados_projetos('projetos.txt')


alunos_colaboradores = Colaborador(Nome)
alunos_projetos = Projeto(Nome)


print("Colaboradores:")
for resultado in alunos_colaboradores:
    print(resultado[0])


print("Projetos:")
for resultado in alunos_projetos:
    print(resultado[0])
