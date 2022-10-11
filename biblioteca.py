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
            database.inserir(table)

        elif opcao == 3:
            print("Informe qual tabela deseja atualizar dados.")
            print("generos | autores | editoras | livros | livros_editoras | complementos")
            table = input()
            database.atualizar(table)

        elif opcao == 4:
            print("Informe em qual tabela deseja deletar dados.")
            print("generos | autores | editoras | livros | livros_editoras | complementos")
            table = input()
            database.deletar(table)

        else:
            print('Opção inválida.')
    else:
        print('Opção inválida')
    main()


if __name__ == "__main__":
    main()
