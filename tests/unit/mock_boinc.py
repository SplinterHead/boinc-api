class MockBoinc:
    MOCK_PROJECT_LIST = {
        "projects": [
            {"name": "Test Project", "description": "Test Project Description"}
        ]
    }
    MOCK_CLIENT_VERSION = {"version": {"major": 1, "minor": 2, "patch": 3}}
    MOCK_CLIENT_INFO = {
        "host_info": {
            "timezone": 0,
            "domain_name": "localhost",
            "ip_addr": "10.10.10.10",
            "os_name": "Linux Ubuntu",
            "os_version": "Linux Ubuntu Testy Test v0",
        }
    }

    def get_all_projects(self):
        return self.MOCK_PROJECT_LIST

    def get_client_version(self):
        return self.MOCK_CLIENT_VERSION

    def get_host_info(self):
        return self.MOCK_CLIENT_INFO
