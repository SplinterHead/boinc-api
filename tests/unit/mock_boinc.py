class MockBoinc:
    MOCK_GENERIC_SUCCESS = {"success": "true"}
    MOCK_CLIENT_INFO = {
        "host_info": {
            "timezone": 0,
            "domain_name": "localhost",
            "ip_addr": "10.10.10.10",
            "os_name": "Linux Ubuntu",
            "os_version": "Linux Ubuntu Testy Test v0",
        }
    }
    MOCK_CLIENT_STATE = {
        "client_state": {
            "host_info": {
                "timezone": 0,
                "domain_name": "boincclient.local",
                "ip_addr": "10.10.10.10",
                "os_name": "Linux Ubuntu",
                "os_version": "Ubuntu 20.04.2 LTS",
            },
            "net_stats": {},
            "time_stats": {},
            "projects": [
                {
                    "master_url": "http://www.worldcommunitygrid.org/",
                    "project_name": "World Community Grid",
                }
            ],
            "apps": [{}],
            "app_versions": [{}],
            "work_units": [{}],
            "results": [{}],
            "platform_name": "x86_64-pc-linux-gnu",
            "core_client_major_version": 1,
            "core_client_minor_version": 2,
            "core_client_release": 3,
            "platform": "x86_64-pc-linux-gnu",
            "global_preferences": {},
        }
    }
    MOCK_CLIENT_VERSION = {"version": {"major": 1, "minor": 2, "patch": 3}}
    MOCK_PROJECT_LIST = {
        "projects": [
            {"name": "Test Project", "description": "Test Project Description"}
        ]
    }

    def attach_project(self, name, url, key):
        return self.MOCK_GENERIC_SUCCESS

    def suspend_project(self, url):
        return self.MOCK_GENERIC_SUCCESS

    def resume_project(self, url):
        return self.MOCK_GENERIC_SUCCESS

    def get_all_projects(self):
        return self.MOCK_PROJECT_LIST

    def get_client_state(self):
        return self.MOCK_CLIENT_STATE

    def get_client_version(self):
        return self.MOCK_CLIENT_VERSION

    def get_host_info(self):
        return self.MOCK_CLIENT_INFO
