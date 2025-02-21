# Q.6.2

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": ["Math", "Science", "English", "SST", "Hindi"],
    "Score": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
barplot = sns.barplot(x="Subject", y="Score", data=df, palette="Set2")

for index, row in df.iterrows():
    barplot.text(index, row["Score"] + 1, str(row["Score"]), ha="center", va="bottom", fontsize=10)

plt.title("Scores by Subject", fontsize=14)
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Scores", fontsize=12)
plt.grid(axis='y', linestyle="--", alpha=0.7)

plt.show()
