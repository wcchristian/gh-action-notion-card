FROM python:3.7-slim

LABEL "com.github.actions.name"="Notion Card Creator"
LABEL "com.github.actions.description"="Creates a notion card on an event from github"
LABEL "com.github.actions.icon"="check-circle"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/wcchristian/gh-action-hugo-build"
LABEL "homepage"="https://anderc.com"
LABEL "maintainer"="Christian Andersen <c.andersen2012@gmail.com>"

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY main.py ./
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/usr/src/app/main.py"]