import json
import csv
from google.colab import files

# Upload file
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# Load data
with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned_data = []

for item in data:
    if "title" not in item or not item["title"]:
        continue

    cleaned_data.append({
        "post_id": item.get("post_id"),
        "title": item.get("title", "").strip(),
        "category": item.get("category"),
        "score": item.get("score", 0),
        "num_comments": item.get("num_comments", 0),
        "author": item.get("author", "").strip(),
        "collected_at": item.get("collected_at")
    })

# Save CSV safely
csv_file = "cleaned_trends.csv"

if len(cleaned_data) > 0:
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cleaned_data[0].keys())
        writer.writeheader()
        writer.writerows(cleaned_data)

    print("Saved:", csv_file)
    print("Total records:", len(cleaned_data))

    files.download(csv_file)
else:
    print("No valid data found!")