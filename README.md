# Projeto de desenvolvimento de API usando DOCKER

Projeto de desenvolvimento de API Flask hospedando banco de dados PostgreSQL no Docker utilizando docker-compose para a implantação do serviço. 
Linguagens Python e Docker utilizadas no projeto.

# Primeiros passos:

- Efetuamos a clonagem do projeto usando o comando ```git clone (repositorio_git) ``` dentro do diretório que vai ser usado no projeto.

- Após a clonagem do projeto, iremos até a pasta ``` db ``` onde vamos encontrar o arquivo ``` docker-compose.yml ```.

- Utilizando o caminho até o arquivo ``` docker-compose.yml ``` vamos abrir o ``` CMD(prompt de comando Winodws) ``` e dentro do diretório ``` db ``` no CMD, executar o comando ``` docker-compose up -d```, isso fará com que o banco de dados ```PostgreSQL``` seja hospedado dentro do Docker.

- Para se conectar ao banco de dados, devemos abrir o arquivo ``` docker-compose.yml ``` para ter acesso aos dados do banco de dados, usuário e senha de acesso caso for utilizar uma ferramenta universal de banco de dados, no meu caso utilizei o ```DBeaver```.

- Podemos acessar o banco de dados também através do ```PgAdmin``` do próprio PostgreSQL acessando o link ``` http://localhost:5050/ ``` e utilizando o usuário e senha de acesso ao ```PgAdmin``` localizado dentro do arquivo ``` docker-compose.yml ```.

- Após concluir com a configuração do banco de dados, iremos executar alguns serviços para a criação das tabelas que iremos utilizar.

- Vamos até a pasta ```app``` e iremos abrir o arquivo ``` main.py ```, logo nas primeira linhas temos a variável ```host```, é necessário colocar o IP WSL(Windows 10) no lugar do IP que est. 
Vamos encontrar os comandos necessários para a criação de nossa tabela a partir da linha ```87```, só descomentar as linhas comentadas e executar o arquivo que criaremos a tabela chamada ``` owners ```.

- iremos até a pasta ``` src ``` onde iremos encontrar o arquivo ``` api.py ```, vamos abri-lo e executa-lo. Ele é responsavel por colocar no ar nossa api no link ``` http://localhost:5000/ ```. Ao copiar o link e colar no navegador, teremos acesso ao Home da API.

# Instalação do Docker:

- Segue link da documento do Docker onde pode ser encontrado o passo-a-passo da instalação do mesmo ```https://docs.docker.com/desktop/install/windows-install/```

#  Módulos necessários:

Necessário ter instalado junto ao Python as seguintes bibliotecas:
```
Pandas, Requests, Json , Flask, Psycopg2.
```
# Instalando os módulos:
Para instalar os módulos, basta acessar o terminal Python e executar o comando pip install "nome do módulo".

Abaixo temos os comandos prontos para serem utilizados:

```pip install time
pip install pandas
pip install requests
pip install json
pip install flask
pip install psycopg2
```

# Filtrando dados na API:

Com a API rodando podemos utilizar filtro para selecionar os notebooks pela marca. Por exemplo ``` http://localhost:5000/owners ```e ele trás os dados referente aos proprietários de veículos:

```

{
  "id": { 1
    
  },
  "name": { exemplo
    
  },
  "quantity_cars": { 3
    
  },
  "model_cars": { hatch
    
  },
  "colors_cars": { yellow
    
  }
}

```
