import mysql.connector
from classe_estoque import db_estoque
from classe_produto import Produto

class DB:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'q1w2e3 ',
            database = 'db_estoque'
        )
        self.meu_cursor = self.conexao.cursor()
        
    def salva_produtos(self, cod, nome, fabricante, quantidade):
        obj_estoque = Produto(cod,nome,fabricante,quantidade)
        comando_sql = f'insert into Produto' \
                      f'(nome, fabricante, quantidade)value'  \
                      f'("{obj_estoque.nome}", "{obj_estoque.telefone}", "{obj_estoque.fabricante}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def lista_produto(self):
        comando_sql = f'select * from Produto'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_produto (self, atributo, valor, cod):
        comando_sql = f'update Produto set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir_produto(self, cod):
        comando_sql = f'delete from Produto where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
