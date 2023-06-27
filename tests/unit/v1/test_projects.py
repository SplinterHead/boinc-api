def test_can_get_list_of_projects(mock_client):
    resp = mock_client.get("/v1/projects/all?client=1")

    assert resp.status_code == 200
    assert len(resp.json["projects"]) == 1


def test_can_start_the_project_attachment_process(mock_client):
    resp = mock_client.post(
        "/v1/projects/attach?client=1",
        json={
            "name": "Test Project",
            "url": "https://testproject.org",
            "key": "token_123",
        },
    )

    assert resp.status_code == 200
    assert resp.json == {"success": "true"}


def test_can_suspend_project(mock_client):
    resp = mock_client.post(
        "/v1/projects/suspend?client=1", json={"url": "https://testproject.org"}
    )

    assert resp.status_code == 200
    assert resp.json == {"success": "true"}


def test_can_resume_project(mock_client):
    resp = mock_client.post(
        "/v1/projects/resume?client=1", json={"url": "https://testproject.org"}
    )

    assert resp.status_code == 200
    assert resp.json == {"success": "true"}
