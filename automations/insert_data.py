import csv
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'netflix'
}

def insert_data(nome_tabela, caminho_csv):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE {nome_tabela} (coluna1 TIPO, coluna2 TIPO, ...)")

    with open(caminho_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv) 

        for linha in leitor_csv:
            valores = ','.join('%s' for _ in linha)
            query = f"INSERT INTO {nome_tabela} VALUES ({valores})"
            cursor.execute(query, linha)

    conn.commit()
    conn.close()
def main():
    insert_data('titles', '/tmp/titles.csv')
    insert_data('imdb_rating', '/tmp/credits.csv')
    insert_data('cast', '/tmp/person.csv')
    print('Dados importados com sucesso!')
