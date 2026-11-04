# API de Cadastro, Login e Formulário (Flask)

API REST em Python/Flask com upload e donwload, a senhas criptografadas (hash) e um formulário de dados pessoais vinculado a cada usuário. O banco de dados é SQLite.

## Tecnologias

- Python 3
- Flask
- SQLite (módulo `sqlite3`)
- Werkzeug (hash de senhas)
- Gunicorn (para execução em produção)

## Estrutura do projeto

```
Teste_corrigido/
├── app.py                  # Cria o app, registra os blueprints e inicia o servidor
├── config.py               # Configurações (chave JWT e nome do banco)
├── requirements.txt        # Dependências
├── database.db             # Banco SQLite
├── database/
│   └── db.py               # Conexão e criação das tabelas
├── models/                 # Acesso ao banco (consultas SQL)
│   ├── download_model.py
│   └── upload_model.py
├── controllers/            # Regras de negócio e validações
│   ├── download_controller.py
│   └── upload_controller.py
└── routes/                 # Rotas da API (blueprints)
    ├── download_route.py
    └── upload_route.py
```

O projeto segue uma divisão em camadas: **routes → controllers → models → database**.

## Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```



3. Inicie a aplicação:

   ```bash
   python app.py
   ```

   A API ficará disponível em `https://ad-kauan-3tri.onrender.com`. As tabelas são criadas automaticamente na primeira execução.





### Usuários (`/users`)

| Método | Rota              | Protegida | Descrição                          |
|--------|-------------------|-----------|------------------------------------|
| POST   | `/users/register` | Não       | Upload um novo usuário           |
| GET    | `/users/me`       | Sim       | Retorna os dados do usuário logado |


### Formulários (`/formularios`)

| Método | Rota                | Protegida | Descrição                              |
|--------|---------------------|-----------|----------------------------------------|
| POST   | `/formularios/`     | Sim       | Cria um formulário para o usuário      |
| GET    | `/formularios/`     | Sim       | Retorna o formulário do usuário logado |
| PUT    | `/formularios/<id>` | Sim       | Atualiza um formulário seu             |
| DELETE | `/formularios/<id>` | Sim       | Exclui um formulário seu               |

## Exemplos de uso

**Upload**

```bash
curl -X POST https://ad-kauan-3tri.onrender.com/uploads/upload \
  -H "Content-Type: application/json" \
  -d '{"username": "maria", "password": "123456"}'
```

Resposta (201): `{"message": "Usuário registrado com sucesso"}`

**Download**

```bash
curl -X GET https://ad-kauan-3tri.onrender.com/downloads/download \
  -H "Content-Type: application/json" \
  -d '{"username": "maria", "password": "123456"}'
```

Resposta (200): `{"access_token": "<token>"}`



## Códigos de resposta

| Código | Significado                                              |
|--------|----------------------------------------------------------|
| 200    | Operação realizada com sucesso                           |
| 201    | Recurso criado                                           |
| 400    | Dados obrigatórios ausentes ou usuário já existente      |
| 404    | Recurso não encontrado ou sem permissão de acesso        |

## Banco de dados

**users**: `id`, `username` (único), `password` (hash)


## Segurança

- As senhas são armazenadas com hash (`generate_password_hash`), nunca em texto puro.
- As consultas SQL usam parâmetros (`?`), o que evita SQL injection.
- As rotas protegidas exigem um token JWT válido.
- Cada usuário só consegue alterar ou excluir os próprios formulários.
- Em produção, defina a variável `JWT_SECRET_KEY` e desative o `debug=True` do `app.py`.
