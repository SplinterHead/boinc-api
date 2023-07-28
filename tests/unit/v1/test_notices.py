def test_can_get_a_list_of_notices(mock_client):
    resp = mock_client.get("/v1/notices/all?client=1")

    assert resp.status_code == 200
    assert len(resp.json["notices"]) == 1
