import requests
from datetime import datetime

USERNAME = "Gebon69"
data = requests.get(f"https://www.codewars.com/api/v1/users/{USERNAME}").json()

stats = {
    "hard": data["ranks"]["languages"]["python"]["scores"]["1kyu"] + ...,
    "medium": ...,
    "last_update": datetime.now().strftime("%Y-%m-%d")
