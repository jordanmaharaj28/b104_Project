# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project

# import libraries 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loads the YRBS data
df = pd.read_csv('XXhq.txt', sep = '\t')
 
print(df['q66'].head())
print(df['q67'].head())
print(df.columns)

#convert q66 into numbers
df["q66"] = pd.to_numeric(df["q66"], errors="coerce")
#convert q67 into numbers
df["q67"] = pd.to_numeric(df["q67"], errors="coerce")

# correlation between question 66 and question 67
df[["q66", "q67"]].corr()

#countplot made with bars and customized colors
sns.countplot(x="q66", 
              hue="q67", 
              data=df, 
              palette=['green', 'skyblue', 'darkblue', 'orange']
              )

# added a title and axis labels to better clarify it
plt.title("Relationship Between (Q66) and Weight Goals (Q67)")
plt.xlabel("Q66: Perception of Weight (1=Very Underweight to 5=Very Overweight)")
plt.ylabel("Number of Students")
# show the graph
plt.show()












