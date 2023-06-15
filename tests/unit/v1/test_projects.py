def test_can_get_list_of_projects(mock_client):
    resp = mock_client.get("/v1/projects/all?client=1")

    assert resp.status_code == 200
    assert len(resp.json["projects"]) == 1
