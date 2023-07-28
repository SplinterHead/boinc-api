def test_can_get_a_list_of_messages(mock_client):
    resp = mock_client.get("/v1/messages/all?client=1")

    assert resp.status_code == 200
    assert len(resp.json["messages"]) == 2
