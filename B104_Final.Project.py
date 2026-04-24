# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

# Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loads the YRBS data from the text file
# sep="\t" means the values are separated by tabs
data = pd.read_csv("XXhq.txt", sep="\t")

# prints the first 5 answers from q67
# this helps check that the column loaded correctly
print(data["q67"].head())

# prints the first 5 answers from q76
# this also helps make sure the data is reading correctly
print(data["q76"].head())

# prints all of the column names in the dataset
# this is useful for checking that q67 and q76 are really there
print(data.columns)

# converts q67 into numbers
# errors="coerce" changes anything that is not a number into NaN
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# converts q76 into numbers too
# this makes it easier to graph and compare the answers
data["q76"] = pd.to_numeric(data["q76"], errors="coerce")

# finds the correlation between q67 and q76
# correlation shows whether the two questions have a relationship
print(data[["q67", "q76"]].corr())

# makes a countplot for q67
# this shows how many people chose each response for q67
sns.countplot(x="q67", data=data, palette=["green", "skyblue", "orange", "red"])

# title for the graph
plt.title("Q67 Responses")

# label for the x-axis
plt.xlabel("Q67: Trying to Lose Weight")

# label for the y-axis
plt.ylabel("Number of People")

# displays the graph
plt.show()

# makes a boxplot comparing q67 and q76
# q67 goes on the x-axis and q76 goes on the y-axis
# this helps show how physical activity changes based on q67 responses
sns.boxplot(
    x="q67",
    y="q76",
    data=data,
    palette=["lightgreen", "skyblue", "pink", "orange"]
)

# title for the second graph
plt.title("Relationship Between Q67 and Q76")

# label for the x-axis
plt.xlabel("Q67: Trying to Lose Weight")

# label for the y-axis
plt.ylabel("Q76: Days Physically Active")

# displays the second graph
plt.show()
    
#------------------------End of Q66 and Q67 Analysis --------------------------













 





































































































