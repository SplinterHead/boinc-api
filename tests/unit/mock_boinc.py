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
    MOCK_DISK_STATS = {
        "disk_stats": {
            "d_total": 123345,
            "d_free": 12345,
            "d_boinc": 1234,
            "projects": [],
        }
    }
    MOCK_MESSAGES = {
        "messages": {
            109: {
                "project": "World Community Grid",
                "pri": "1",
                "body": "Finished download of MCM1_FILENAME.txt",
                "time": 1676897897,
            },
            110: {
                "project": "World Community Grid",
                "pri": "1",
                "body": "Started download of MCM2_FILENAME.txt",
                "time": 1676897897,
            },
        }
    }
    MOCK_NETWORK_STATS = {"network_transfers": {"01-01-1970": {"down": 10, "up": 10}}}
    MOCK_NOTICES = {
        "notices": {
            1: {
                "title": "Notice A",
                "description": "This is a notice",
                "create_time": 123,
                "arrival_time": 124,
                "is_private": False,
                "project_name": "proja",
                "category": "test",
                "link": "https://linky.link",
            }
        }
    }
    MOCK_PROJECT_LIST = {
        "projects": [
            {"name": "Test Project", "description": "Test Project Description"}
        ]
    }
    MOCK_RESULT_LIST = {
        "results": [
            {
                "name": "MCM1_0196917_7759_0",
                "wu_name": "MCM1_0196917_7759",
                "platform": "x86_64-pc-linux-gnu",
                "version_num": 761,
                "project_url": "http://www.worldcommunitygrid.org/",
                "final_cpu_time": 0.000000,
                "final_elapsed_time": 0.000000,
                "exit_status": 0,
                "state": 2,
                "estimated_cpu_time_remaining": 15050.234471,
            }
        ]
    }

    def attach_project(self, name, url, key):
        return self.MOCK_GENERIC_SUCCESS

    def detach_project(self, url):
        return self.MOCK_GENERIC_SUCCESS

    def suspend_project(self, url):
        return self.MOCK_GENERIC_SUCCESS

    def resume_project(self, url):
        return self.MOCK_GENERIC_SUCCESS

    def get_all_projects(self):
        return self.MOCK_PROJECT_LIST

    def get_project_status(self):
        return self.MOCK_PROJECT_LIST

    def get_client_state(self):
        return self.MOCK_CLIENT_STATE

    def get_client_version(self):
        return self.MOCK_CLIENT_VERSION

    def get_host_info(self):
        return self.MOCK_CLIENT_INFO

    def get_messages(self):
        return self.MOCK_MESSAGES

    def get_public_notices(self):
        return self.MOCK_NOTICES

    def get_results(self):
        return self.MOCK_RESULT_LIST

    def get_disk_stats(self):
        return self.MOCK_DISK_STATS

    def get_network_stats(self):
        return self.MOCK_NETWORK_STATS
