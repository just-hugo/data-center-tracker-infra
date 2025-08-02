from requests import Response


class NotionInterface:
    def __init__(self):
        self.integration_key = 
        self.DATABASE_ID = "239725ab821d802ebefdf07739df73f5"
        self.BASE_URL = "https://api.notion.com/v1/"
        self.endpoint = "/databases/" + self.DATABASE_ID + "/query"
        self.headers = {
            "Authorization": self.integration_key,
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json"
        }
        return self.headers
