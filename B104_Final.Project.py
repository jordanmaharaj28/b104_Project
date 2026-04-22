# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load file
path = r"/Users/lopez/Documents/Github/b104_Project/XXhq.csv"
df = pd.read_csv(path, skiprows=3, on_bad_lines="skip")

# Clean column names
df.columns = df.columns.str.strip()

# Check columns
print(df.columns.tolist())

# Find columns containing Q66 and Q67
q66_cols = [col for col in df.columns if "Q66" in col]
q67_cols = [col for col in df.columns if "Q67" in col]

print("Q66 matches:", q66_cols)
print("Q67 matches:", q67_cols)

# Stop if not found
if not q66_cols or not q67_cols:
    print("Q66 or Q67 was not found in the columns.")
else:
    q66_col = q66_cols[0]
    q67_col = q67_cols[0]

    print(df[q66_col].value_counts())
    print(df[q67_col].value_counts())

    overweight = df[(df[q66_col] == "D") | (df[q66_col] == "E")]
    trying_lose = overweight[overweight[q67_col] == "A"]

    print("Overweight people trying to lose weight:", len(trying_lose))

    percent = (len(trying_lose) / len(overweight)) * 100
    print(f"Percent of overweight people trying to lose weight: {percent:.2f}%")

    sns.countplot(x=q67_col, data=overweight)
    plt.title("Are overweight people trying to lose weight?")
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.show()

#------------------------End of Q66 and Q67 Analysis --------------------------









 





































































































