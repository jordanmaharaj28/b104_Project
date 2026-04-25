# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

# Libraries
# pandas reads the data file and lets me work with it like a table
import pandas as pd
# seaborn is the library I used to make the graphs
import seaborn as sns
# matplotlib helps show the graph and change titles, labels, colors, and spacing
import matplotlib.pyplot as plt

# this reads the YRBS text file into a table called data
# pd.read_csv() opens the file and loads it into Python
# "XXhq.txt" is the name of the file I am using
# sep="\t" means the values in the file are separated by tabs
data = pd.read_csv("XXhq.txt", sep="\t")

# this prints the first 5 values from q67
# data["q67"] selects the q67 column
# .head() shows only the first 5 rows so I can quickly check if it loaded right
print(data["q67"].head())

# this prints the first 5 values from q76 for the same reason
print(data["q76"].head())

# this prints all the column names in the dataset
# .columns gives the names of every column in the file
print(data.columns)

# this converts q67 into numbers
# pd.to_numeric() changes the values into numeric form
# errors="coerce" means if Python finds a bad value, it changes it into NaN instead of crashing
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# this converts q76 into numbers too
# I did this because numeric values are easier to compare and graph
data["q76"] = pd.to_numeric(data["q76"], errors="coerce")

# this prints the correlation between q67 and q76
# data[["q67", "q76"]] picks only those two columns
# .corr() calculates whether the two columns move together or not
print(data[["q67", "q76"]].corr())

# this starts the first graph
# plt.figure() creates a new graph space
# figsize=(12, 6) sets the size of the graph
# 12 means the graph is wider
# 6 means the graph is not as tall
# I picked 12 and 6 so the labels and bars have more room and do not look cramped
plt.figure(figsize=(12, 6))

# this makes a countplot for q67
# sns.countplot() counts how many times each q67 value appears
# x="q67" means q67 goes across the bottom on the x-axis
# data=data tells seaborn to use the dataframe named data
# color="skyblue" makes all the bars the same soft blue color
sns.countplot(x="q67", data=data, color="skyblue")

# this changes the graph background color
# plt.gca() means "get current axes"
# the axes is the main graph area where the bars are drawn
# .set_facecolor("lightgray") changes that graph area's background color to light gray
plt.gca().set_facecolor("lightgray")

# this adds the title at the top of the graph
# plt.title() is used to name the graph
plt.title("Q67 Responses")

# this labels the x-axis
# plt.xlabel() puts a label under the bottom axis
plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

# this labels the y-axis
# plt.ylabel() puts a label on the side axis
plt.ylabel("Number of People")

# this changes the x-axis values from numbers to words
# plt.xticks() changes the labels that appear on the x-axis
# ticks=[0, 1, 2, 3] are the actual q67 code values in the data
# labels=[...] replaces those code values with words people can understand better
plt.xticks(
    ticks=[0, 1, 2, 3],
    labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
)

# this fixes the spacing of the graph
# plt.tight_layout() automatically adjusts things so titles and labels fit better
plt.tight_layout()

# this displays the first graph
# plt.show() tells Python to actually show the graph window
plt.show()

# this starts the second graph
# I used the same figure size again so both graphs look consistent
plt.figure(figsize=(12, 6))

# this makes a countplot for q67 and q76 together
# x="q67" puts q67 on the x-axis
# hue="q76" means q76 is shown using different colors inside each q67 group
# palette="Blues" uses different shades of blue for the q76 groups
sns.countplot(x="q67", hue="q76", data=data, palette="Blues")

# this changes the graph background color to light gray again
plt.gca().set_facecolor("lightgray")

# this adds the title
plt.title("Relationship Between Q67 and Q76")

# this labels the x-axis
plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

# this labels the y-axis
plt.ylabel("Number of People")

# this changes the x-axis numbers into words again
# I used the same tick values because q67 still uses 0, 1, 2, and 3
plt.xticks(
    ticks=[0, 1, 2, 3],
    labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
)

# this gets the legend information from the graph
# plt.gca() gets the current graph area again
# .get_legend_handles_labels() pulls out two things from the legend:
# handles = the colored boxes or symbols
# labels = the default text labels that seaborn made for those colors
handles, labels = plt.gca().get_legend_handles_labels()

# this list stores the meaning of each q76 code
# I made this list so the legend shows clear day labels instead of just numbers
new_labels = [
    "0 days active",
    "1 day active",
    "2 days active",
    "3 days active",
    "4 days active",
    "5 days active",
    "6 days active",
    "7 days active"
]

# this adds the legend to the graph
# plt.legend() creates the legend box
# handles tells Python which color boxes to show
# new_labels[:len(labels)] matches the right number of labels to the number of color groups
# [:len(labels)] means "only use as many labels as the graph actually needs"
# title= adds the title above the legend
# bbox_to_anchor=(1.05, 1) moves the legend outside the graph
# the 1.05 moves it a little to the right of the graph
# the 1 places it level with the top of the graph
# I used 1.05 so the legend would not cover the bars
# loc="upper left" tells Python which corner of the legend box to line up with that anchor point
# "upper left" means the top-left corner of the legend box is attached there
plt.legend(
    handles,
    new_labels[:len(labels)],
    title="Q76: Days Physically Active In The Past 7 Days",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

# this fixes spacing again
# I used it here so the legend and labels fit without getting cut off
plt.tight_layout()

# this shows the second graph
plt.show()
    
#------------------------End of Q66 and Q67 Analysis -------------------------#













 





































































































