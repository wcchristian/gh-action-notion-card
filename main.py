import sys
import os
import json
from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import BookmarkBlock

# Get data from github environment
path = os.environ.get("GITHUB_EVENT_PATH")
token = os.environ.get("NOTION_TOKEN")
collection_url = os.environ.get("COLLECTION_URL")

# Load the event from github
with open(path,"r") as f:
    github_event_string = f.read()

# convert event to json
github_event_json = json.loads(github_event_string)

# set card title and link from json event
card_title = github_event_json["issue"]["title"]
card_link = github_event_json["issue"]["html_url"]

# add row to notion collection and add a text block with link to the new card
client = NotionClient(token_v2=token)
cv = client.get_collection_view(collection_url)
row = cv.collection.add_row()
row.name = card_title
row.children.add_new(BookmarkBlock, link=card_link)