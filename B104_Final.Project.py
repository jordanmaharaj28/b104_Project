# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load file path
path = r"/Users/lopez/Documents/GitHub/b104_Project/XXhq.csv"

# Check that the file path is correct
print("Path:", path)
print("Exists:", os.path.exists(path))

# Print the first 5 lines of the file to make sure it is really the CSV
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    for i in range(5):
        print(f.readline())

# Read the CSV file into a dataframe
df = pd.read_csv(path)

# Clean up column names by removing extra spaces
df.columns = df.columns.str.strip()

# Print all column names so we can check whether Q66 and Q67 exist
print("Columns:", df.columns.tolist())

# Find the real column names that contain Q66 and Q67
q66_cols = [col for col in df.columns if "Q66" in col]
q67_cols = [col for col in df.columns if "Q67" in col]

# Print the matching column names
print("Q66 matches:", q66_cols)
print("Q67 matches:", q67_cols)

# If Q66 or Q67 is not found, print a message
if not q66_cols or not q67_cols:
    print("Q66 or Q67 was not found in the columns.")

# Otherwise, continue with the analysis
else:
    # Save the actual column names
    q66_col = q66_cols[0]
    q67_col = q67_cols[0]

    # Print response counts for Q66 and Q67
    print(df[q66_col].value_counts())
    print(df[q67_col].value_counts())

    # Q66: Find people who said slightly or very overweight (D or E)
    overweight = df[(df[q66_col] == "D") | (df[q66_col] == "E")]

    # Q67: From those people, find who is trying to lose weight (A)
    trying_lose = overweight[overweight[q67_col] == "A"]

    # Print how many overweight people are trying to lose weight
    print("Overweight people trying to lose weight:", len(trying_lose))

    # Calculate the percent of overweight people trying to lose weight
    percent = (len(trying_lose) / len(overweight)) * 100

    # Print the final answer
    print(f"Percent of overweight people trying to lose weight: {percent:.2f}%")

    # Create a graph of Q67 responses for overweight people
    sns.countplot(x=q67_col, data=overweight)
    plt.title("Are overweight people trying to lose weight?")
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.show()
#------------------------End of Q66 and Q67 Analysis --------------------------









 





































































































