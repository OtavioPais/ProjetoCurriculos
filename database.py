import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        self.cursor = self.conn.cursor()
        self.create_database()
        self.conn.close()

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="atividade_p4"
        )
        self.cursor = self.conn.cursor()
        self.create_table()
        self.inserir_dados_iniciais()  # Adicione essa linha

    def create_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS atividade_p4")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Candidatos (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(50),
                telefone VARCHAR(11),
                minibio TEXT,
                nota_entrevista INT,
                nota_teorico INT,
                nota_pratica INT,
                nota_softskills INT
            )
        """)
        self.conn.commit()

    def inserir_dados_iniciais(self):
        query = "TRUNCATE TABLE Candidatos" # Utilizado para limpar a tabela antes de inserir a importação
        self.cursor.execute(query)
        self.conn.commit()

        query = """
        INSERT INTO Candidatos (id, nome, telefone, minibio, nota_entrevista, nota_teorico, nota_pratica, nota_softskills)
        VALUES
        (1, 'Luis Otavio Pais', '15981001090', 'Olá, tenho interesse em trabalhar na área de T.I', 9, 7, 8, 10),
        (2, 'Fábio Deodato', '15999999999', 'Olá, tenho interesse em trabalhar na área da Logística', 7, 7, 8, 7),
        (3, 'Gabriel Rodrigues', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 8, 8, 10, 7),
        (4, 'Lucas Vieira', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 8, 9, 9, 8),
        (5, 'Gabriel Flaise', '15999999999', 'Olá, tenho interesse em trabalhar na área de Mecânica', 9, 5, 10, 7),
        (6, 'Ana Laura', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 7, 10, 10, 6),
        (7, 'Jovelina Paes', '15999999999', 'olá, tenho interesse em atuar na área de enfermagem', 9, 8, 9, 8),
        (8, 'Elisangela Paes', '15999999999', 'Olá, tenho interesse em atuar na área educacional', 9, 9, 8, 7),
        (9, 'Vinicius Pantojo', '15999999999', 'olá, tenho interesse em atuar na área de logística', 8, 7, 9, 9),
        (10, 'Lucas Souza', '15999999999', 'olá, tenho interesse em atuar na área do esporte', 9, 8, 8, 7),
        (11, 'João Jesus', '15999999999', 'olá, tenho interesse em atuar na área de T.I', 8, 9, 10, 7),
        (12, 'Ruan Patrick', '15999999999', 'olá, tenho interesse em trabalhar na área de entrega', 9, 7, 8, 9),
        (13, 'Glória Queiroz', '15999999999', 'Olá, tenho interesse em trabalhar na área de Compras', 9, 7, 6, 7),
        (14, 'Maicon Douglas', '15999999999', 'Olá, tenho interesse em atuar na área de Mecância Automotiva', 6, 7, 6, 5),
        (15, 'Adrian Roberto', '15999999999', 'Olá, tenho interesse em atuar na área de Esportes', 5, 6, 6, 4),
        (16, 'Ana Julia', '15999999999', 'Olá, tenho interesse em atuar na área educacional', 9, 8, 7, 9),
        (17, 'Giovanna Luvizoto', '15999999999', 'Olá, tenho interesse em atuar na área Administrativa', 8, 7, 8, 6),
        (18, 'Ryan Hessel', '15999999999', 'Olá, tenho interesse in atuar na área Administrativa', 7, 7, 8, 8),
        (19, 'Thiago Antunes', '15999999999', 'Olá, tenho interesse em atuar na área de T.I', 8, 8, 7, 8),
        (20, 'Helena Camargo', '15999999999', 'Olá, tenho interesse em atuar na área de Vendas', 7, 6, 6, 8);
        """
        self.cursor.execute(query)
        self.conn.commit()

    def cad_candidato(self, candidato):
        query = "INSERT INTO Candidatos (nome, telefone, minibio, nota_entrevista, nota_teorico, nota_pratica, nota_softskills) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (candidato.nome, candidato.telefone, candidato.minibio, candidato.nota_entrevista, candidato.nota_teorico, candidato.nota_pratica, candidato.nota_softskills)
        self.cursor.execute(query, values)
        self.conn.commit()

    def busca_candidatos(self, min_nota_entrevista, min_nota_teorico, min_nota_pratica, min_nota_softskills):
        query = "SELECT * FROM Candidatos WHERE nota_entrevista >= %s AND nota_teorico >= %s AND nota_pratica >= %s AND nota_softskills >= %s"
        values = (min_nota_entrevista, min_nota_teorico, min_nota_pratica, min_nota_softskills)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

if __name__ == "__main__":
    db = Database()