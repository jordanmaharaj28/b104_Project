# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

import pandas as pd 

# Load File 
df = pd.read_csv(r"/Users/lopez/Documents/Github/b104_Project/XXhq.csv")

# Columns names 
df.columns = df.columns.str.strip()

#Check data
print(df.head())
print(df.columns)
print(df["q66"].value_counts())
print(df["q67"].value_counts())

# Q66 - Find people who said slightly or very overweight (D or E)
overweight = df[(df["q66"] == "D") (df["q66"] == "E")]
# Q67 - From those people, find who is tryig to lose weight (A)
trying_lose = overweight[overweight["q67"] == "A"]

print('Overweight people trying to lose weight:', len(trying_lose))

# Calculate percent 

percent = (len(trying_lose) / len(overweight)) * 100 

# Final answer 
print("Percent of overweight people trying to lose weight: {:.2f}%".format(percent))









 





































































































