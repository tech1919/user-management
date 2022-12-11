# Basic User Management Project

### Depelopment

Configure `.env` file:
```
DATABASE_URL=postgresql://username:password@postgres:5432/users
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=users
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

Run this command in the root dir:
```
$ docker compose -f "docker-compose.dev.yml" up -d --build 
```

In this part, you should have three containers:
1. [FastAPI](http://localhost:8000/docs)
2. PostGres
3. [PgAdmin](http://localhost:80)

For login to the PgAdmin enter the username and password from the `.env` file, as follows:

* username - postgres-username@admin.com
* password - postgres-password




