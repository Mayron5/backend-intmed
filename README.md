# Desafio IntMed - Backend

### Pre-requisitos

Antes de iniciar a aplicacao, insira o seguinte comando no terminal para que todas as dependencias sejam instaladas:

```console
pip install -r requirements.txt
```

---
### Rodando a aplicacao
- Antes de rodas a aplicacao, execute os testes automatizados, afim de verificar possiveis erros na aplicacao. O comando para este evento segue abaixo:

```console
python manage.py test
```


- Para iniciar a aplicacao, insira o seguinte comando:

```console
python manage.py runserver
```

Com a aplicacao iniciada, acesse a pagina:

<a href='http://127.0.0.1:8000/admin'>Pagina de administracao da aplicacao</a>

Nela o administrador podera popular dados, exclui-los e edita-los.

---

Os caminhos da aplicacao sao os seguintes:

POST - <b>http://127.0.0.1/api/register</b> - Para cadastrar um usuario na aplicacao
POST - <b>http://127.0.0.1/api/login</b> - Para realizar login de um usuario cadastrado na aplicacao

GET - <b>http://127.0.0.1/api/medicos</b> - Para listar os medicos da aplicacao (Autenticacao requerida)
GET - <b>http://127.0.0.1/api/medicos/medico_id</b> - Para retornar os detalhes do madico (Autenticacao requerida)
GET - <b>http://127.0.0.1/api/medicos/search?=especialidade</b> - Para medicos por sua especialidade (Autenticacao requerida)

GET - <b>http://127.0.0.1/api/consultas</b> - Para listar as consultas do usuario logado na aplicacao (Autenticacao requerida)
GET - <b>http://127.0.0.1/api/consultas/consulta_id</b> - Para retornar uma consulta baseada em seu ID de um usuario logado (Autenticacao requerida)
POST - <b>http://127.0.0.1/api/consultas</b> - Para criar uma consulta de um usuario logado na aplicacao (Autenticacao requerida)

GET - <b>http://127.0.0.1/api/agendas</b> - Para listar as agendas disponiveis dos medicos registrados na aplicacao (Autenticacao requerida)

