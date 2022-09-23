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

import sqlite3


def conectar():
    """
    Função para conectar ao banco de dados.
    :return: conn
    """
    conn = sqlite3.connect("psqlite3.rods")

    conn.execute("""CREATE TABLE IF NOT EXISTS
        """
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
    cursor.execute("")
    bib_ = cursor.fetchall()

    desconectar(conn)


def inserir():
    """
    Função para inserir um livro.
    :return: None
    """
    conn = conectar()
    cursor = conn.cursor()
