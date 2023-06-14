from flask import Flask


def test_create_app_returns_flask_app(app):
    assert isinstance(app, Flask)


def test_app_has_slot_for_clients(app):
    assert app.config["clients"] == {}
