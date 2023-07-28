def test_can_get_client_version(mock_client):
    resp = mock_client.get("/v1/client/version?client=1")

    assert resp.status_code == 200
    assert resp.json["version"] == {"major": 1, "minor": 2, "patch": 3}


def test_can_get_client_host_info(mock_client):
    resp = mock_client.get("/v1/client/info?client=1")

    assert resp.status_code == 200
    assert resp.json["host_info"]["os_name"] == "Linux Ubuntu"


def test_can_get_basic_info(mock_client):
    resp = mock_client.get("/v1/client/basicinfo?client=1")

    assert resp.status_code == 200
    assert resp.json == {
        "version": {"major": 1, "minor": 2, "patch": 3},
        "host_info": {"os_name": "Linux Ubuntu"},
    }


def test_can_get_client_state(mock_client):
    resp = mock_client.get("/v1/client/state?client=1")

    assert resp.status_code == 200
    assert resp.json["version"] == {"major": 1, "minor": 2, "patch": 3}


def test_can_get_disk_stats(mock_client):
    resp = mock_client.get("/v1/client/diskstats?client=1")

    assert resp.status_code == 200
    assert resp.json["disk_stats"] == {
        "d_total": 123345,
        "d_free": 12345,
        "d_boinc": 1234,
        "projects": [],
    }


def test_can_get_network_stats(mock_client):
    resp = mock_client.get("/v1/client/networkstats?client=1")

    assert resp.status_code == 200
    assert resp.json["network_transfers"] == {"01-01-1970": {"down": 10, "up": 10}}
