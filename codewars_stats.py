import requests
from datetime import datetime

USERNAME = "Gebon69"

def get_codewars_stats():
    data = requests.get(f"https://www.codewars.com/api/v1/users/{USERNAME}").json()
  
    hard = sum(score for kyu, score in data["ranks"]["languages"]["python"]["scores"].items() 
              if kyu in ["1kyu", "2kyu", "3kyu"])
    
    medium = sum(score for kyu, score in data["ranks"]["languages"]["python"]["scores"].items() 
              if kyu in ["4kyu", "5kyu"])
    
    easy = sum(score for kyu, score in data["ranks"]["languages"]["python"]["scores"].items() 
              if kyu in ["6kyu", "7kyu", "8kyu"])
    
    return {
        "hard": hard,
        "medium": medium,
        "easy": easy,
        "total": hard + medium + easy,
        "last_update": datetime.now().strftime("%Y-%m-%d")
    }

stats = get_codewars_stats()
