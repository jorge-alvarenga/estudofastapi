from http import HTTPStatus

# client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundi(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'olá Mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeusernamne',
            'password': 'password',
            'email': 'teste@teste.com',
        },
    )
    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusernamne',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusernamne',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }


def test_read_user_1(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testeusernamne',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_user_1_not_found(client):
    response = client.get('/users/-1')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testeuseratualizado',
            'password': 'passwordatualizado',
            'email': 'emailatualizado@teste.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'testeuseratualizado',
        'email': 'emailatualizado@teste.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/-1',
        json={
            'username': 'testeuseratualizado',
            'password': 'passwordatualizado',
            'email': 'emailatualizado@teste.com',
            'id': 1,
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/-1')
    assert response.status_code == HTTPStatus.NOT_FOUND
