import pandas as pd
import matplotlib.pyplot as plt

# Load file
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename)

# Count categories
category_counts = df["category"].value_counts()

# Bar Chart
category_counts.plot(kind="bar")

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()
# Pie Chart
category_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("Category Distribution")
plt.ylabel("")

plt.show()