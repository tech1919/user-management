import pytest
from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def pytest_namespace():
    return {
        'admin_role_id': None,
        'developer_role_id' : None,
        'user_cognito_group_name' : None,
        'group_role_record_id' : None,
        }

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}

def test_secure_route():
    response = client.get("/auth/secure")
    
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}

@pytest.mark.dependency()
def test_pass_secure_route():
    jwt_token = "eyJraWQiOiJkeW1MTWJxaDF6WHhWTDBqMldFVCtSTVNPbjc4Y0pmdlE2TXlaKzVDMVVnPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiXzlUX2g5alNLemFqZ0o1UGFTdHpzdyIsInN1YiI6ImVjMTA4NjY2LTM0ZjctNDIyNC05YmE3LTg5YWZlNWFhNjIwMiIsImNvZ25pdG86Z3JvdXBzIjpbIkRFVkVMT1BFUiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMi5hbWF6b25hd3MuY29tXC91cy1lYXN0LTJfSkE4S1NoYkltIiwiY29nbml0bzp1c2VybmFtZSI6Im9mcnkubWFrZGFzeSIsImF1ZCI6IjdobjF2N2s5MmJxOXRodmEzOWwwZmxvb3JtIiwiZXZlbnRfaWQiOiI2Y2MyNDcyMS1kYjdkLTRlYzAtOGY5ZS1mZWNlYTkxMzU0NTUiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY3MTQ3MzE0NiwiZXhwIjoxNjcxNDc2NzQ2LCJpYXQiOjE2NzE0NzMxNDYsImp0aSI6ImNjZjFiZTZkLTVlOWItNDkwMS04ZjU2LTY5M2U2NGRhOGFlYiIsImVtYWlsIjoib2ZyeTYwMDAwQGdtYWlsLmNvbSJ9.PoAxXehIf912PaVKclN_jcF98oXUd416c04PAXpoCraIrTEMu8p7M0pel1pyflTZ_0lppQ67_VO0RfQrxGa3-9WrbXTD0OWe57KglWJcNdj5cK9ZXejvP5DRhq3njXEEBOdFnxvRC-zxFOnkNJJYXb3JPBBa9erdA2Egp7L-Rc3P4Y4W3SaCovof5MRfOfJneZ5UtHiR0v4bifU18KuIEZpRW787qZbk4dHu_ayVlEiyZQQKmomPCfUnXCDMSXxecYtiv8pUb-a6yW45vYxfEQKQ_-qsg7GZEimE6Htxu45NCCJNQ-my2c_t1X5tIsQOyJqUdKVDcu60U3IhZmkM1Q"
    headers = {
        "Authorization" : f"Bearer {jwt_token}",
        "Content-Type" : "application/json",
    }

    response = client.get("/auth/secure" , headers=headers)
    assert response.status_code == 200

    pytest.user_cognito_group_name = response.json()["claims"]["cognito:groups"][0]

# CREATE THE ROLES RECORDS

@pytest.mark.dependency(depends=["test_pass_secure_route"])
def test_create_admin_role():
    body = {
        "name": "admin",
        "permissions": {}
        }
    response = client.post("/roles/create" , json=body)

    assert response.status_code == 201
    assert response.json()["name"] == body["name"]
    assert response.json()["permissions"] == body["permissions"]
    assert response.json()["permissions"] == body["permissions"]

    pytest.admin_role_id = response.json()["id"]

@pytest.mark.dependency(depends=["test_pass_secure_route"])
def test_create_developer_role():
    body = {
        "name": "developer",
        "permissions": {}
        }
    response = client.post("/roles/create" , json=body)

    assert response.status_code == 201
    assert response.json()["name"] == body["name"]
    assert response.json()["permissions"] == body["permissions"]
    assert response.json()["permissions"] == body["permissions"]

    pytest.developer_role_id = response.json()["id"]

@pytest.mark.dependency(depends=["test_create_admin_role" , "test_create_developer_role"])
def test_create_group_role_connection():

    response = client.post(f"/groups/add-a-role/{pytest.admin_role_id}/{pytest.user_cognito_group_name}")

    assert response.status_code == 201
    assert response.json()["role_id"] == pytest.admin_role_id
    assert response.json()["cognito_group_name"] == pytest.user_cognito_group_name


    pytest.group_role_record_id = response.json()["id"]

# ADD PERMISSIONS TO THE ROLES

# TEST FOR PERMISSIONS



# DELETE THE TEST RECORDS

@pytest.mark.dependency(depends=["test_create_group_role_connection"])
def test_remove_role_from_group():

    response = client.delete(f"/groups/remove-a-role/{pytest.admin_role_id}/{pytest.user_cognito_group_name}")

    assert response.status_code == 202
    assert response.json() == {"message": "Record deleted"}

@pytest.mark.dependency(depends=["test_create_admin_role"])
def test_delete_admin_role():

    response = client.delete(f"/roles/delete/{pytest.admin_role_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Record deleted"}

@pytest.mark.dependency(depends=["test_create_developer_role"])
def test_delete_developer_role():

    response = client.delete(f"/roles/delete/{pytest.developer_role_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Record deleted"}





