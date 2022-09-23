# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    biblioteca.py

DESCRIÇÃO:
    Programa principal para acessar minha biblioteca pessoal.

AUTOR:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
"""

# ------- #
# Imports #
# ------- #
from utils import database


# ----------- #
#   Módulo    #
# ----------- #

def main():
    """
    Função para gerar o menu inicial
    """
    print('========= Gerenciamento do CRUD ==============')
    print('Selecione uma opção: ')
    print('1 - Listar livros.')
    print('2 - Inserir dados.')
    print('3 - Atualizar dados.')
    print('4 - Deletar dados.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            database.listar()
        elif opcao == 2:
            print("Informe em qual tabela deseja adicionar dados.")
            print("generos | autores | editoras | livros | livros_editoras | complementos")
            table = input()
            if table in ['generos', 'autores', 'editoras', 'livros', 'livros_editoras', 'complementos']:
                if table == 'generos':
                    database.inserir_genero()
                elif table == 'autores':
                    database.inserir_autor()
                elif table == 'editoras':
                    database.inserir_editora()
                elif table == 'livros':
                    database.inserir_livro()
                elif table == 'livros_editoras':
                    database.inserir_livro_editoras()
                elif table == 'complementos':
                    database.inserir_complemento()
            else:
                print("Tabela não encontrada. ")
        elif opcao == 3:
            print("Informe qual tabela deseja atualizar dados.")
            print("generos | autores | editoras | livros | livros_editoras | complementos")
            table = input()
            if table in ['generos', 'autores', 'editoras', 'livros', 'livros_editoras', 'complementos']:
                database.atualizar(table)
            else:
                print("Tabela não encontrada. ")
        elif opcao == 4:
            print("Informe em qual tabela deseja deletar dados.")
            print("generos | autores | editoras | livros | livros_editoras | complementos")
            table = input()
            if table in ['generos', 'autores', 'editoras', 'livros', 'livros_editoras', 'complementos']:
                database.deletar(table)
            else:
                print("Tabela não encontrada. ")
        else:
            print('Opção inválida.')
    else:
        print('Opção inválida')
    main()


if __name__ == "__main__":
    main()
