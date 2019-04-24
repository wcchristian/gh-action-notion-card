from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import PageBlock
import sys
import os
import json

path = os.environ.get("GITHUB_EVENT_PATH")
token = os.environ.get("NOTION_TOKEN")
collectionUrl = os.environ.get("COLLECTION_URL")

with open(path,"r") as f:
    contents = f.read()

githubPayloadJson = json.loads(contents)

cardTitle = githubPayloadJson["issue"]["title"]
cardDescription = githubPayloadJson["issue"]["url"]
tagList = ["Github Issue", "SomeTag"]

client = NotionClient(token_v2=token)
cv = client.get_collection_view(collectionUrl)
row = cv.collection.add_row()
row.name = cardTitle
row.children.add_new(TextBlock, title=cardDescription)