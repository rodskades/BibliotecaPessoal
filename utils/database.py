# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    database.py

DESCRIÇÃO:
    Módulo de definição do banco de dados.

AUTOR:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
"""

# ------- #
# Imports #
# ------- #

import sqlite3


# ----------- #
#   Módulo    #
# ----------- #

def conectar():
    """
    Função para conectar ao banco de dados.
    :return: conn
    """
    conn = sqlite3.connect("psqlite3.rods")
    # Tabela de gêneros dos livros:
    conn.execute("""CREATE TABLE IF NOT EXISTS generos(
        idgeneros INTEGER PRIMARY KEY AUTOINCREMENT,
        generos TEXT NOT NULL);"""
                 )
    # Tabela de autores dos livros:
    conn.execute("""CREATE TABLE IF NOT EXISTS autores(
            idautores INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL);"""
                 )
    # Tabela de editoras dos livros:
    conn.execute("""CREATE TABLE IF NOT EXISTS editoras(
            ideditoras INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL);"""
                 )
    # Tabela de livros:
    conn.execute("""CREATE TABLE IF NOT EXISTS livros(
            idlivros INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            paginas INTEGER NOT NULL,
            terminado TEXT NOT NULL,
            id_genero INTEGER REFERENCES generos(idgeneros) NOT NULL,
            id_autor INTEGER REFERENCES autores(idautores) NOT NULL);"""
                 )
    # Tabela para relacionar um livro a mais de uma editora:
    conn.execute("""CREATE TABLE IF NOT EXISTS livros_editoras(
            idlivros_editoras INTEGER PRIMARY KEY AUTOINCREMENT,
            id_livro INTEGER REFERENCES livros(idlivros) NOT NULL,
            id_editora INTEGER REFERENCES editoras(ideditora) NOT NULL);"""
                 )
    # Tabela para relacionar um livro e seus livros complementares:
    conn.execute("""CREATE TABLE IF NOT EXISTS complementos(
                idcomplementos INTEGER PRIMARY KEY AUTOINCREMENT,
                id_livro_base INTEGER REFERENCES livros(idlivros) NOT NULL,
                id_livro_complementar INTEGER REFERENCES livros(idlivros) NOT NULL);"""
                 )

    return conn


def desconectar(conn):
    """
    Função para desconectar do servidor.
    :param conn: conexão
    :return: None
    """
    conn.close()


def listar():
    """
    Uma função para listar os livros.
    :return:
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT l.idlivros AS 'Código', l.nome AS 'Nome', g.genero AS 'Gênero', a.nome AS 'Autor', e.nome AS 
        'Editora', l.paginas AS 'Número de Páginas', l.terminado AS 'Concluído?'
            FROM livros AS l, generos AS g, autores AS a, editoras AS e, livros_editoras AS le
            WHERE l.id_genero = g.idgeneros AND l.id_autor = a.idautores AND l.idlivros = le.id_livro AND 
            le.id_editora = e.ideditoras;
        """
    )

    livros = cursor.fetchall()
    if len(livros) > 0:
        print("Livros registrados: ")
        print("--------------------")
        for livro in livros:
            print(f'ID: {livro[0]}')
            print(f'Nome: {livro[1]}')
            print(f'Gênero: {livro[2]}')
            print(f'Autor: {livro[3]}')
            print(f'Editora: {livro[4]}')
            print(f'Número de Páginas: {livro[5]}')
            print(f'Concluído? {livro[6]}')
            print("--------------------")
    else:
        print('Não existem livros registrados ainda.')
    desconectar(conn)


def inserir_genero():
    """
    Função para inserir dados na tabela generos.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
    genero = input("Informe o gênero: ")

    cursor.execute(f"INSERT INTO generos (genero) VALUES ('{genero}')")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O gênero {genero} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o dado.')

    desconectar(conn)


def inserir_autor():
    """
    Função para inserir dados na tabela autores.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
    autor = input("Informe o nome do autor: ")

    cursor.execute(f"INSERT INTO autores (nome) VALUES ('{autor}')")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O autor {autor} foi inserido com sucesso.")
    else:
        print('Não foi possível inserir o dado.')

    desconectar(conn)


def inserir_editora():
    """
    Função para inserir dados na tabela editoras.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
    editora = input("Informe o nome da editora: ")

    cursor.execute(f"INSERT INTO editoras (nome) VALUES ('{editora}')")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"A editora {editora} foi inserida com sucesso.")
    else:
        print('Não foi possível inserir o dado.')

    desconectar(conn)


def inserir_livro():
    """
    Função para inserir dados na tabela livros.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
    nome = input("Informe o nome do livro: ")
    paginas = int(input("Informe o número de páginas: "))
    terminado = input("Terminado? (Sim ou Não): ")
    id_genero = int(input("Código do gênero: "))
    id_autor = int(input("Código do autor: "))

    cursor.execute(f"INSERT INTO livros (nome, paginas, terminado, id_genero, id_autor) VALUES "
                   f"('{nome}', {paginas}, '{terminado}', {id_genero}, {id_autor})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O livro {nome} foi inserido com sucesso.")
    else:
        print('Não foi possível inserir os dados.')

    desconectar(conn)


def inserir_livro_editoras():
    """
    Função para inserir dados na tabela livros_editoras.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
    id_livro = int(input("Informe o código do livro: "))
    id_editora = int(input("Código da editora: "))

    cursor.execute(f"INSERT INTO livros_editoras (id_livro, id_editora) VALUES ({id_livro}, {id_editora})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O livro e a editora foram inseridos com sucesso.")
    else:
        print('Não foi possível inserir os dados.')

    desconectar(conn)


def inserir_complemento():
    """
    Função para inserir dados na tabela complementos.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
    id_base = int(input("Código do livro base: "))
    id_comp = int(input("Código do livro complemento: "))

    cursor.execute(f"INSERT INTO complementos (id_livro_base, id_livro_complementar) VALUES ({id_base}, {id_comp})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O complemento foi inserido com sucesso.")
    else:
        print('Não foi possível inserir os dados.')

    desconectar(conn)


def atualizar(table):
    """
    Função para atualizar dados da tabela fornecida
    :param table: str - Nome da tabela
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()

    id_generico = int(input(f"Informe o id{table}: "))
    if table in ['generos', 'Generos', 'GENEROS']:
        genero = input("Informe o gênero: ")
        cursor.execute(f"UPDATE generos SET genero='{genero}' WHERE idgenero={id_generico}")
        conn.commit()

    elif table in ['autores', 'Autores', 'AUTORES']:
        autor = input("Informe o nome do autor: ")
        cursor.execute(f"UPDATE autores SET nome='{autor}' WHERE idautores={id_generico}")
        conn.commit()

    elif table in ['editoras', 'Editoras', 'EDITORAS']:
        editora = input("Informe o nome da editora: ")
        cursor.execute(f"UPDATE editoras SET nome='{editora}' WHERE ideditoras={id_generico}")
        conn.commit()

    elif table in ['livros', 'Livros', 'LIVROS']:
        nome = input("Informe o nome do livro: ")
        paginas = int(input("Informe o número de páginas: "))
        terminado = input("Terminado? (Sim ou Não): ")
        id_genero = int(input("Código do gênero: "))
        id_autor = int(input("Código do autor: "))

        cursor.execute(f"UPDATE livros SET nome='{nome}', paginas={paginas}, terminado={terminado}, "
                       f"id_genero={id_genero}, id_autor={id_autor} WHERE idlivros={id_generico}")
        conn.commit()

    elif table in ['livros_editoras', 'Livros_editoras', 'LIVROS_EDITORAS']:
        id_livro = int(input("Informe o código do livro: "))
        id_editora = int(input("Código da editora: "))

        cursor.execute(f"UPDATE livros_editoras SET id_livro={id_livro}, id_editora={id_editora} "
                       f"WHERE idlivros_editoras={id_generico}")
        conn.commit()

    elif table in ['complementos', 'Complementos', 'COMPLEMENTOS']:
        id_base = int(input("Código do livro base: "))
        id_comp = int(input("Código do livro complemento: "))

        cursor.execute(f"UPDATE complementos SET id_livro_base={id_base}, id_livro_complementar={id_comp} "
                       f"WHERE idcomplementos={id_generico}")
        conn.commit()

    else:
        print("Tabela não encontrada.")

    if cursor.rowcount == 1:
        print("Atualização realizada com sucesso.")
    else:
        print("Não foi possível realizar a atualização.")

    desconectar(conn)


def deletar(table):
    """
    Função para deletar um dado da tabela fornecida.
    :param table: str
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()

    id_generico = int(input(f"Informe o id{table}: "))
    if table in ['generos', 'Generos', 'GENEROS']:
        cursor.execute(f"DELETE FROM generos WHERE idgenero={id_generico}")
        conn.commit()

    elif table in ['autores', 'Autores', 'AUTORES']:
        cursor.execute(f"DELETE FROM autores WHERE idautores={id_generico}")
        conn.commit()

    elif table in ['editoras', 'Editoras', 'EDITORAS']:
        cursor.execute(f"DELETE FROM editoras WHERE ideditoras={id_generico}")
        conn.commit()

    elif table in ['livros', 'Livros', 'LIVROS']:
        cursor.execute(f"DELETE FROM livros WHERE idlivros={id_generico}")
        conn.commit()

    elif table in ['livros_editoras', 'Livros_editoras', 'LIVROS_EDITORAS']:
        cursor.execute(f"DELETE FROM livros_editoras WHERE idlivros_editoras={id_generico}")
        conn.commit()

    elif table in ['complementos', 'Complementos', 'COMPLEMENTOS']:
        cursor.execute(f"DELETE FROM complementos WHERE idcomplementos={id_generico}")
        conn.commit()

    else:
        print("Tabela não encontrada.")

    if cursor.rowcount == 1:
        print("Entrada excluída com sucesso.")
    else:
        print("Não foi possível excluir o dado.")

    desconectar(conn)
