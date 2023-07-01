import requests
import mysql.connector

grafana_url = 'http://localhost:3000'  
grafana_username = 'admin'  
grafana_password = 'Gleison123@'  

mysql_host = 'localhost' 
mysql_user = 'root' 
mysql_password = 'root' 
mysql_database = 'netflix' 

def create_api_key():
    session = requests.Session()
    session.auth = (grafana_username, grafana_password)
    
    api_key_name = 'Minha API Key'
    role = 'Admin'
    
    response = session.post(f'{grafana_url}/api/auth/keys', json={'name': api_key_name, 'role': role})
    
    if response.status_code == 200:
        return response.json()['key']
    else:
        raise Exception('Erro ao criar a chave de API:', response.text)

def configure_mysql_data_source(api_key):
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    data_source_name = 'MySQL'
    
    response = session.get(f'{grafana_url}/api/datasources')
    data_sources = response.json()
    for data_source in data_sources:
        if data_source['name'] == data_source_name:
            return
    
    session.post(f'{grafana_url}/api/datasources', json={
        'name': data_source_name,
        'type': 'mysql',
        'url': f'{mysql_host}:3306',
        'database': mysql_database,
        'user': mysql_user,
        'password': mysql_password
    })

try:
    api_key = create_api_key()
    print('Chave de API criada:', api_key)
    
    configure_mysql_data_source(api_key)
    print('MySQL configurado como fonte de dados no Grafana')
    
except Exception as e:
    print('Ocorreu um erro:', str(e))
