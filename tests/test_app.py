def test_hello_world(client):
    """Start with a blank database."""

    response = client.get('/')
    assert b'{"message":"Hello World"}' in response.data

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200