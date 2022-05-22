from app import app # Flask instance of the API

def test_index_route():
    response = app.test_client().get('/')
    print(response.json)
    assert response.status_code == 200
    assert b"<h1>Hello from" in response.data

