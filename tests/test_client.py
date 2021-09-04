import pytest

from adapters.client import ReqresClient


@pytest.fixture()
def client():
    return ReqresClient()


def test_get_user(client):
    response = client.get_user(2)
    assert response.status_code == 200


def test_get_user_not_found(client):
    response = client.get_user(23)
    assert response.status_code == 404


def test_get_users(client):
    response = client.get_users(2)
    assert response.status_code == 200


def test_create_user(client):
    response = client.create_user(
        name='morpheus', job='leader')
    assert response.status_code == 201


def test_update_user(client):
    response = client.update_user(
        user_id=2, name='morpheus', job='zion resident')
    assert response.status_code == 200


def test_delete_user(client):
    response = client.delete_user(2)
    assert response.status_code == 204
