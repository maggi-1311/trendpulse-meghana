import requests
import time
import json
from datetime import datetime

# Header
headers = {"User-Agent": "TrendPulse/1.0"}

# API URLs
TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Improved categories (more keywords)
categories = {
    "technology": ["ai","software","tech","code","computer","data","cloud","api","gpu","llm","startup","app","programming"],
    "worldnews": ["war","government","country","president","election","climate","attack","global","policy","nation"],
    "sports": ["nfl","nba","fifa","sport","game","team","player","league","championship","match","tournament"],
    "science": ["research","study","space","physics","biology","discovery","nasa","genome","experiment","scientist"],
    "entertainment": ["movie","film","music","netflix","game","book","show","award","streaming","series","tv"]
}

# Function to detect category
def get_category(title):
    title = title.lower()
    for cat, keys in categories.items():
        for k in keys:
            if k in title:
                return cat
    return None

# Storage
collected = []
count = {c: 0 for c in categories}

# Fetch top 500 IDs
try:
    ids = requests.get(TOP_URL, headers=headers).json()[:500]
except:
    ids = []

# Loop category-wise
for cat in categories:
    print(f"Processing category: {cat}")

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
                    "score": res.get("score", 0),
                    "num_comments": res.get("descendants", 0),
                    "author": res.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                collected.append(data)
                count[cat] += 1

        except:
            print("Error fetching:", i)

    # Required delay
    time.sleep(2)

# Save JSON (Colab-friendly)
file = f"trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(file, "w") as f:
    json.dump(collected, f, indent=4)

print(f"\nCollected {len(collected)} stories.")
print(f"Saved to {file}")