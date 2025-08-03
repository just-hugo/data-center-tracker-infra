import NotionInterface
import requests
from requests import Response


url = NotionInterface.url()
header = {
    "Authorization": NotionInterface.get_private_key(),
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=header)

print(response.json())
