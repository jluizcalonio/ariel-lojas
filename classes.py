import mysql.connector

class Listagem():
    def __init__(self, *args):
        self.ordenar_listagem = ["loja", "categoria", "produto", "preco"]  # Escolhe o tipo de listagem.
        # Vai influenciar como o pandas vai exibir os dados.
        self.loja = ""  # acessar BD loja
        self.produto = ""  # acessar BD produto
        self.categoria = ""  # acessar BD cat
        self.preco = float(0)  # acessar BD preço
        self.observacoes = ""  # acessar BD obs

class BancoDeDados():
    def __init__(self):
        self.bancodedados = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        self.cursor = self.bancodedados.cursor()

        self.criar_bd()

        self.bancodedados.commit()

        self.conectar_bd()

        self.cursor = self.bancodedados.cursor()

        self.criar_tabelas()

        self.bancodedados.commit()

    def criar_bd(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS lojasariel")

    def conectar_bd(self):
        self.bancodedados = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lojasariel"
        )

    def criar_tabelas(self):
        # Crie um dicionário parecido com esse:
        # https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
        tabelas = {
            "lojas": (
                "CREATE TABLE IF NOT EXISTS lojas ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "nome VARCHAR(255) NOT NULL)"
            ),
            "categorias": (
                "CREATE TABLE IF NOT EXISTS categorias ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "loja_id INT,"
                "nome VARCHAR(255) NOT NULL,"
                "FOREIGN KEY (loja_id) REFERENCES lojas(id) ON DELETE CASCADE)"
            ),
            "produtos": (
                "CREATE TABLE IF NOT EXISTS produtos ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "categoria_id INT,"
                "nome VARCHAR(255) NOT NULL,"
                "FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE)"
            ),
            "precos": (
                "CREATE TABLE IF NOT EXISTS precos ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "produto_id INT,"
                "preco DECIMAL(10, 2) NOT NULL,"
                "FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE CASCADE)"
            ),
            "observacoes": (
                "CREATE TABLE IF NOT EXISTS observacoes ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "produto_id INT,"
                "observacao TEXT,"
                "FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE CASCADE)"
            )
        }

        for nome_tabela, tabela_ordens in tabelas.items():
            self.cursor.execute(tabela_ordens)

    def fechar_conexao(self):
        self.cursor.close()
        self.bancodedados.close()

    def adicionar_loja(self, nome):  # QUANDO PROGRAMAR A INTERFACE, COLOCAR O PARÂMETRO COMO O INPUT DO USUÁRIO
        # self.conectar_bd()

        # self.cursor = self.bancodedados.cursor()

        self.cursor.execute(f"INSERT INTO lojas (nome) VALUES ('{nome}');")
        self.bancodedados.commit()

    def excluir_loja(self):
        pass

    def adicionar_categoria(self, nome):
        self.cursor.execute(f"INSERT INTO categorias (nome) VALUES ('{nome}')")
        self.bancodedados.commit()

    def adicionar_produto(self):
        pass

    def excluir_produto(self):
        pass

    def buscar_loja(self):
        pass

    def buscar_categoria(self):
        pass

    def buscar_produto(self):
        pass

class Loja():
    def __init__(self, nome, categoria, produtos_lista, observacoes):
        self.nome = nome
        self.categoria = categoria
        self.produtos_lista = produtos_lista  # list
        self.observacoes = observacoes

    def mudar_categoria(self):
        pass

class Produto():
    def __init__(self, nome, categoria, preco, observacoes):
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.observacoes = observacoes

