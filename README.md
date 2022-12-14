# Basic User Management Project

> ## Depelopment Enviroment

Configure `.env` file:
```
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=users
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

COGNITO_REGION=
COGNITO_POOL_ID=
```

Run this command in the root dir:
```
$ docker compose -f "docker-compose.dev.yml" up -d --build 
```

In this part, you should have three containers:
1. [FastAPI](http://localhost:8000/docs)
2. Postgres database
3. [PgAdmin](http://localhost:80)

For login to the PgAdmin enter the username and password from the `.env` file, as follows:

* username - postgres-username@admin.com
* password - postgres-password

> ## Add new model ( SQL Table)

1. go to [database/models.py](./database/models.py)
2. crete new class using the Base class

```python
class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True) , primary_key=True , default=uuid.uuid4)
    name = Column(String(100))
```

This line will create the table the next time you run this project (if it is not already exists)
```python
Base.metadata.create_all(engine)
```

> ## Add new route
1. go to [routes/users.py](./routes/users.py) (or any other script related to the route you want to add)
2. add new route in this format:
```python
@router.get("/name-of-route" , status_code=status.HTTP_200_OK , )
def name_of_function(
    db: Session = Depends(get_db),
):

    # you can write what this route will do
    # in here and return a response

    return some_response

    # or at a seperate function as follows

    return create_new_record(db=db)

    # the seperate function will be added to the 
    # related crud operations at the utils folder
```

it is better to add a new function at the [utils](./utils/) folder and import that function back to were you implament the route function

## Routes with authentication dependency

you can see an example for a secure route in [here](./auth/user_handlers.py)

```python
@router.get("/secure", 
description="this route is an example for a secure route",
dependencies=[Depends(auth)],)
async def secure() -> bool:
    
    return auth.jwt_creds
```

another simpler way of adding authentication dependency to a group of routes is at the [main script](./main.py) like this:
```python
# this line add a group of routes to the FastAPI application
app.include_router(router=users.router , prefix="/users" , dependencies=[Depends(auth)])
# by adding the dependencies=[Depends(auth)], no every route 
# expect a JWT that can be authenticaded with the JWKS from AWS Cognito
```


if a request that was sent to this route, contain in the **headers**: 
```
{
    "Authorization" : "Bearer some.json.webtoken"
}
```
than, the route will check first if this is an authenticated one comes from the AWS Cognito UserPool, as specified in the relevant environment variable `COGNITO_POOL_ID`. in this specific example , the route will also return the jwt cresentials as decoded from the JWT. this variable has this structure:
```

{
  "jwt_token": "the original JWT string",
  "header": {
    "kid": "NkMpoZmqv4UBEWkN/yCvN/W2rSFnHRswDa6PjiyAUuc=",
    "alg": "RS256"
  },
  "claims": {
    "sub": "ec108666-34f7-4224-9ba7-89afe5aa6202",
    "cognito:groups": [
      "DEVELOPER"
    ],
    "iss": "https://cognito-idp.us-east-2.amazonaws.com/us-east-2_JA8KShbIm",
    "version": 2,
    "client_id": "7hn1v7k92bq9thva39l0floorm",
    "token_use": "access",
    "scope": "aws.cognito.signin.user.admin openid profile",
    "auth_time": 1671202410,
    "exp": 1671206010,
    "iat": 1671202410,
    "jti": "7e97bdaf-b074-4bc4-931b-cb50d72482ea",
    "username": "username string"
  },
  "signature": "the jwt signature string",
  "message": "some string"
}
```

So there is a lot of information here about the user who sent the request and with which you can later decide what is displayed in the client

> ## Handle Resources

For checking a user's permissions there is a class called `PermissionCheck` in the [auth/permission.py](./auth/permission.py) script. This class depend on the authentication method so by adding this dependency to a certain route, it automaticly check the JWT authentication and user's permissions.

### How to use it :
import the relevent class:
```python 
from auth.permission import PermissionCheck
```
create a check instance as follows:
```python
users_read_permission_check = PermissionCheck(statments=["events:read" , "events:write" , "aoi:read"])
```
Add the check instance as a dependency at a specific route:
```python
@router.get("/secure", 
description="this route is an example for a secure route",
dependencies=[Depends(users_read_permission_check)],)
async def secure():
    
    return "You have access"
```

or on a group of routes:
```python
app.include_router(router=user_router, prefix="/auth" , dependencies=[Depends(users_read_permission_check)]) 
```

Now every route in the API that depends on this class will be obliged to perform authentication with the JWT sent to it, and then search the database according to the groups that appear in the JWT's payload under `cognito:groups` for all the roles associated with this group.





