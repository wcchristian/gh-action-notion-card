from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import PageBlock
import sys
import os

path = os.environ.get("GITHUB_EVENT_PATH")
token = os.environ.get("NOTION_TOKEN")
collectionUrl = os.environ.get("COLLECTION_URL")
cardTitle = "This is the title of the github issue"
cardDescription = "This is the content of the github issue"
tagList = ["Github Issue", "SomeTag"]

with open(path,"r") as f:
    contents = f.read()


client = NotionClient(token_v2=token)
cv = client.get_collection_view(collectionUrl)
row = cv.collection.add_row()
row.name = cardTitle
row.tag = tagList
row.children.add_new(TextBlock, title=contents)