import pandas as pd

df = pd.read_csv('credits.csv')

arquivo1 = df[['person_id', 'id', 'character', 'role']]
arquivo1.columns = ['id_filme', 'person_id', 'character', 'role']

arquivo1.to_csv('arquivo1.csv', index=False)

arquivo2 = df[['person_id', 'name']]
arquivo2 = arquivo2.drop_duplicates()
arquivo2.to_csv('arquivo2.csv', index=False)
