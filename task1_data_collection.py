import requests
import time
import json
import os
from datetime import datetime

headers = {"User-Agent": "TrendPulse/1.0"}

TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

categories = {
    "technology": ["ai","software","tech","code","computer","data","cloud","api","gpu","llm"],
    "worldnews": ["war","government","country","president","election","climate","attack","global"],
    "sports": ["nfl","nba","fifa","sport","game","team","player","league","championship"],
    "science": ["research","study","space","physics","biology","discovery","nasa","genome"],
    "entertainment": ["movie","film","music","netflix","game","book","show","award","streaming"]
}

def get_category(title):
    title = title.lower()
    for cat, keys in categories.items():
        for k in keys:
            if k in title:
                return cat
    return None

collected = []
count = {c:0 for c in categories}

# Fetch top 500 IDs
try:
    ids = requests.get(TOP_URL, headers=headers).json()[:500]
except:
    ids = []

# Loop category-wise
for cat in categories:
    for i in ids:
        if count[cat] >= 25:
            break
        try:
            res = requests.get(ITEM_URL.format(i), headers=headers).json()
            if not res or "title" not in res:
                continue

            if get_category(res["title"]) == cat:
                data = {
                    "post_id": res.get("id"),
                    "title": res.get("title"),
                    "category": cat,
                    "score": res.get("score",0),
                    "num_comments": res.get("descendants",0),
                    "author": res.get("by","unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                collected.append(data)
                count[cat]+=1

        except:
            print("Error fetching:", i)

    time.sleep(2)

# Save JSON
os.makedirs("data", exist_ok=True)
file = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(file,"w") as f:
    json.dump(collected,f,indent=4)

print(f"Collected {len(collected)} stories. Saved to {file}")