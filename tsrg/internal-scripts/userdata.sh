#!/bin/bash

# Instalação do Grafana
sudo apt-get install -y libfontconfig1
wget https://dl.grafana.com/oss/release/grafana_8.0.6_amd64.deb
sudo dpkg -i grafana_8.0.6_amd64.deb
sudo apt-get update
sudo apt-get install -y grafana
sudo apt-get install -y python3.9
sudo apt-get install -y python3.9-pip
python3.9 -m pip install mysql-connector-python


# Instalação do MySQL
sudo apt-get install -y mysql-server
sudo systemctl enable mysql
sudo systemctl start mysql

# Configuração do MySQL (substitua as credenciais e configurações conforme necessário)
sudo mysql_secure_installation <<EOF
y
root
root
0
n
n
n
n
EOF

# Definir usuário e senha do Grafana
sudo grafana-cli admin reset-admin-password Gleison123@

# Definir usuário e senha do MySQL
sudo mysql -u root -p"senha_root" -e "CREATE DATABASE netflix;"


# Configuração do Grafana para usar o MySQL
sudo grafana-cli plugins install grafana-piechart-panel
sudo grafana-cli plugins install grafana-worldmap-panel
sudo grafana-cli plugins install grafana-clock-panel
sudo grafana-cli plugins install grafana-simple-json-datasource

sudo systemctl enable grafana-server
sudo systemctl start grafana-server



