from unittest.mock import Mock, patch
from uuid import UUID

from pytest import fixture

MOCK_UUID = "00000000-1111-2222-3333-444444444444"


def _mock_uuid():
    return UUID(MOCK_UUID)


@fixture
def test_client():
    return {
        "name": "test_client",
        "hostname": "localhost",
        "port": 31416,
        "password": "password",
    }


@fixture
def short_client():
    return {"name": "test_client", "hostname": "localhost", "id": MOCK_UUID}


def test_add_pushes_client_to_internal_storage(app, client, test_client):
    client.post("/v1/clients/add", json=test_client)
    assert len(app.config["clients"]) is 1


@patch("uuid.uuid4", Mock(return_value=_mock_uuid()))
def test_added_client_is_assigned_a_uuid(app, client, test_client):
    client.post("/v1/clients/add", json=test_client)

    assert MOCK_UUID in app.config["clients"].keys()


@patch("uuid.uuid4", Mock(return_value=_mock_uuid()))
def test_client_uuid_is_returned_on_successful_storage(client, test_client):
    resp = client.post("/v1/clients/add", json=test_client)
    assert resp.json == {"client_id": MOCK_UUID}


def test_getall_returns_empty_list_when_no_clients_saved(client):
    resp = client.get("/v1/clients/getall")

    assert resp.status_code == 200
    assert resp.json == []


@patch("uuid.uuid4", Mock(return_value=_mock_uuid()))
def test_getall_returns_known_client(client, test_client, short_client):
    client.post("/v1/clients/add", json=test_client)
    resp = client.get("/v1/clients/getall")

    assert resp.json == [short_client]
