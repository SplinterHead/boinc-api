from pytest import fixture
from unit.mock_boinc import MockBoinc

from boinc_api.app import create_app


@fixture
def app():
    app = create_app()
    yield app


@fixture
def client(app):
    return app.test_client()


@fixture
def mock_app():
    app = create_app()
    app.config["clients"].update({"1": {"instance": MockBoinc()}})
    yield app


@fixture
def mock_client(mock_app):
    return mock_app.test_client()
