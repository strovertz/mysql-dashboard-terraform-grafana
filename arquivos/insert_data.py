import csv
import pymysql

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Minhasenha123@',
    'database': 'netflix'
}
def alter_table_column_size(table_name, column_name, new_size):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    alter_query = f"ALTER TABLE {table_name} MODIFY {column_name} VARCHAR({new_size})"
    cursor.execute(alter_query)

    conn.commit()
    conn.close()

# Exemplo de uso para alterar a coluna 'character' na tabela 'credits'
#alter_table_column_size('credits', 'character', 1000)

def create_database():
    db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Minhasenha123@',
   }
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS netflix")
    conn.commit()

    conn.close()

def create_table(nome_tabela, cabecalho):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    colunas = ','.join([f'`{nome_coluna}` VARCHAR(255)' for nome_coluna in cabecalho]) 
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})")
    conn.commit()

    conn.close()

def insert_data(nome_tabela, caminho_csv):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    with open(caminho_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabecalho = next(leitor_csv)
        create_table(nome_tabela, cabecalho)
        alter_table_column_size('credits', 'charac', 1000)
        for linha in leitor_csv:
            #listas = [valor.strip("[]").replace("'", "") for valor in linha[6:8]]
            #linha[6:8] = listas
            #personagem = linha[2][:255]
            #linha[2] = personagem
            valores = ','.join(['%s'] * len(linha))
            query = f"INSERT INTO {nome_tabela} VALUES ({valores})"
            cursor.execute(query, linha)
    conn.commit()
    conn.close()

def main():
    create_database()
    insert_data('credits', '/home/ubuntu/arquivos/credits.csv')
    #alter_table_column_size('credits', 'charac', 1000)
    insert_data('titles', '/home/ubuntu/arquivos/titles.csv')
    insert_data('person', '/home/ubuntu/arquivos/person.csv')
    print('Dados importados com sucesso!')

main()
