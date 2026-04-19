# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Load File 

path = r"/Users/lopez/Documents/Github/b104_Project/XXhq.csv"

df = pd.read_csv(
    r"/Users/lopez/Documents/Github/b104_Project/XXhq.csv",
    on_bad_lines="skip"
)
    

# Columns names 
df.columns = df.columns.str.strip()    


#Check data
print(df.head())
print(df.columns.tolist())

print(df["Q66"].value_counts())
print(df["Q67"].value_counts())

# Q66 - Find people who said slightly or very overweight (D or E)
overweight = df[(df["Q66"] == "D") | (df["Q66"] == "E")]
trying_lose = overweight[overweight["Q67"] == "A"]

print('Overweight people trying to lose weight:', len(trying_lose))

# Calculate percent 

percent = (len(trying_lose) / len(overweight)) * 100 

# Final answer 
print("Percent of overweight people trying to lose weight: {:.2f}%".format(percent))

# Graph 

sns.countplot(x="Q67", data=overweight)
plt.title("Are Overweigght people trying to lose Weight?")
plt.xlabel("Response (A = Yes)")
plt.ylabel("Count")
plt.show()

#------------------------End of Q66 and Q67 Analysis --------------------------









 





































































































