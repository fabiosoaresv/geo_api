# Quick guide para projeto Python usando FastAPI

# Criar env de um projeto novo
python -m venv venv

# Ativar a env
source venv/bin/activate

# Criar a pasta app + atribuir permissão correta
sudo chown -R fventurelli:fventurelli app/

# Instalar dependências
pip install lib
fastapi uvicorn dotenv sqlalchemy psycopg2-binary alembic pydantic

fastapi – framework web moderno, rápido e assíncrono.
uvicorn – servidor ASGI que roda o FastAPI.
dotenv - utilizar variáveis de ambiente
sqlalchemy – ORM (Mapeamento Objeto-Relacional) para interagir com o banco.
psycopg2-binary – driver para conectar com PostgreSQL.
alembic – ferramenta de migrations para versionar o schema do banco.
pydantic – validação e serialização de dados (usada no FastAPI para schemas).
requests - fazer requests em api externa
pytest - fazer testes unitários

# Startar projeto com o uvicorn
uvicorn app.main:app --reload

# Debbuger
import pdb
pdb.set_trace()

# Requests
GET weather Piraju
```bash
curl --location --request POST 'http://localhost:8000/weather/Piraju'
```

GET weather async Piraju
```bash
curl --location --request POST 'http://localhost:8000/async/weather/Piraju'
```

POST users
```bash
curl --location 'http://localhost:8000/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Fabio",
    "email": "fabio@email.io",
    "age": 28
}'
```

# Rodar testes unitários
```bash
pytest
```
