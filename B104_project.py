# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy 

import pandas as pd


# Data file  
df = pd.read_csv("/Users/lopez/Downloads/XXhq.csv")

# Remove people that didn't smoke (A = 0 days)

df_smokers = df[df["Q33"] != "A"]
# Compare how often they smoked (Q33)
# With if they tried to quit(Q40)

result = pd.crosstab(df_smokers["Q33"], df_smokers["Q40"])

# Show the table 
print(result)
