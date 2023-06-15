class MockBoinc:
    MOCK_PROJECT_LIST = {
        "projects": [
            {"name": "Test Project", "description": "Test Project Description"}
        ]
    }

    def get_all_projects(self):
        return self.MOCK_PROJECT_LIST
