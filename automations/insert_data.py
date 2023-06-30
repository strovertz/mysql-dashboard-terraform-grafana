import csv
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'netflix'
}

def create_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE netflix")
    conn.commit()

    conn.close()

def create_table(nome_tabela, cabecalho):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    colunas = ','.join([f'{nome_coluna} VARCHAR(255)' for nome_coluna in cabecalho])
    cursor.execute(f"CREATE TABLE {nome_tabela} ({colunas})")
    conn.commit()

    conn.close()

def insert_data(nome_tabela, caminho_csv):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    with open(caminho_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabecalho = next(leitor_csv)
        create_table(nome_tabela, cabecalho)

        for linha in leitor_csv:
            valores = ','.join('%s' for _ in linha)
            query = f"INSERT INTO {nome_tabela} VALUES ({valores})"
            cursor.execute(query, linha)

    conn.commit()
    conn.close()

def main():
    create_database()
    insert_data('titles', '/tmp/titles.csv')
    insert_data('imdb_rating', '/tmp/credits.csv')
    insert_data('cast', '/tmp/person.csv')
    print('Dados importados com sucesso!')

main()
