# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

# Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("/Users/lopez/Documents/GitHub/b104_Project/XXhq.csv",
                 skiprows=11,
                 on_bad_lines='skip'
)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check available columns
print("Available columns:", df.columns.tolist())

# Update these variables with the correct column names
weight_col = "q66 - How do you describe your weight?"  
lose_weight_col = "q67 - Are you trying to lose weight?" 

# Check if the column names are in the file
if weight_col not in df.columns or lose_weight_col not in df.columns:
    print("How do you describe your weight.")
    print("Are you trying to lose weight.")
else:
    # Show how many people answered each way
    print(df[weight_col].value_counts())
    print(df[lose_weight_col].value_counts())

    # Find people who said they are slightly or very overweight
    overweight = df[(df[weight_col] == "D") | (df[weight_col] == "E")]

    # From those people, find who said they are trying to lose weight
    trying_to_lose = overweight[overweight[lose_weight_col] == "A"]

    # Print how many
    print("Overweight people trying to lose weight:", len(trying_to_lose))

    # Calculate the percent
    percent = (len(trying_to_lose) / len(overweight)) * 100

    # Print final answer
    print("Percent of overweight people trying to lose weight: {:.2f}%".format(percent))

    # Make graph
    sns.countplot(x=lose_weight_col, data=overweight)
    plt.title("Are overweight people trying to lose weight?")
    plt.xlabel("Q67 Response")
    plt.ylabel("Count")
    plt.show()
#------------------------End of Q66 and Q67 Analysis --------------------------














 





































































































