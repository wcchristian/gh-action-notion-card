from notion.client import NotionClient
from notion.block import TextBlock

token = "$NOTION_TOKEN"
collectionUrl = "$COLLECTION_URL"
cardTitle = "This is the title of the github issue"
cardDescription = "This is the content of the github issue"
tagList = ["Github Issue", "SomeTag"]


client = NotionClient(token_v2=token)
cv = client.get_collection_view(collectionUrl)
row = cv.collection.add_row()
row.name = cardTitle
row.tag = tagList