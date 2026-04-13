import pandas as pd

# Get uploaded filename
filename = list(uploaded.keys())[0]

# Load CSV
df = pd.read_csv(filename)

# 1. Total stories
print("Total Stories:", len(df))

# 2. Stories per category
print("\nStories per Category:")
print(df["category"].value_counts())

# 3. Top 5 stories by score
print("\nTop 5 Stories by Score:")
top5 = df.sort_values(by="score", ascending=False)[["title", "score"]].head()
print(top5)

# 4. Average comments
print("\nAverage Comments:", df["num_comments"].mean())