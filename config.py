import json

with open("data/token.json", "r", encoding="utf-8") as file:
    data = json.load(file)

TOKEN = data["token"]