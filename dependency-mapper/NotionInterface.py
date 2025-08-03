import requests
from requests import Response
from dotenv import load_dotenv
import os


class NotionInterface:
    def __init__(self):
        self.DATABASE_ID = "239725ab821d802ebefdf07739df73f5"
        self.BASE_URL = "https://api.notion.com/v1/"
        self.endpoint = "databases/" + self.DATABASE_ID + "/query"


def get_private_key() -> str:
    load_dotenv()
    integration_key = os.getenv("NOTION_PRIVATE_TOKEN")
    if not integration_key:
        raise ValueError("NOTION_PRIVATE_TOKEN environment variable not set in .env.")
    return integration_key


def url() -> str:
    return NotionInterface().BASE_URL + NotionInterface().endpoint


def post_query(self, url: str, header: dict) -> Response:
    response = requests.request("POST", url, headers=header)
    return response
