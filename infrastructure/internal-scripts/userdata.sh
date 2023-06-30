#!/bin/bash

# Instalação do Grafana
sudo apt-get install -y libfontconfig1
wget https://dl.grafana.com/oss/release/grafana_8.0.6_amd64.deb
sudo dpkg -i grafana_8.0.6_amd64.deb
sudo apt-get update
sudo apt-get install -y grafana
sudo apt-get install -y python3.9
sudo apt-get install -y python3-pip
python3 -m pip install mysql-connector-python
python3 -m pip install pandas
sudo systemctl enable grafana-server.server
sudo systemctl start grafana-server.server

# Instalação do MySQL
sudo apt-get install -y mysql-server
sudo systemctl enable mysql
sudo systemctl start mysql

# Definir usuário e senha do Grafana
sudo grafana-cli admin reset-admin-password Gleison123@

# Configuração do MySQL
sudo mysql -u root <<EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
EOF

# Configuração do Grafana para usar o MySQL
sudo grafana-cli plugins install grafana-piechart-panel
sudo grafana-cli plugins install grafana-worldmap-panel
sudo grafana-cli plugins install grafana-clock-panel
sudo grafana-cli plugins install grafana-simple-json-datasource

