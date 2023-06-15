def test_can_get_client_version(mock_client):
    resp = mock_client.get("/v1/client/version?client=1")

    assert resp.status_code == 200
    assert resp.json["version"] == {"major": 1, "minor": 2, "patch": 3}


def test_can_get_client_host_info(mock_client):
    resp = mock_client.get("/v1/client/info?client=1")

    assert resp.status_code == 200
    assert resp.json["host_info"]["os_name"] == "Linux Ubuntu"
