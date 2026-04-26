# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

# Libraries
# pandas helps me read the data file and work with it like a table
import pandas as pd
# seaborn helps me make the graphs
import seaborn as sns
# matplotlib helps me show the graphs and label them
import matplotlib.pyplot as plt
# tkinter helps me make the GUI window and buttons
import tkinter as tk

# this reads the data file and stores it in a variable called data
# sep="\t" means the file is separated by tabs
data = pd.read_csv("XXhq.txt", sep="\t")

# this shows the first 5 values from q67
# I used .head() just to make sure the data loaded correctly
print(data["q67"].head())

# this shows the first 5 values from q76
# I checked this one too for the same reason
print(data["q76"].head())

# this prints all the column names in the file
# I used this to make sure q67 and q76 were really there
print(data.columns)

# this changes q67 into numbers
# pd.to_numeric() tries to turn the values into numbers
# errors="coerce" means if something is not a real number, Python changes it to NaN
# NaN just means the value is missing or bad
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# this changes q76 into numbers too
# I did this so it would be easier to graph and compare
data["q76"] = pd.to_numeric(data["q76"], errors="coerce")

# this prints the correlation between q67 and q76
# .corr() checks if the two columns are related
print(data[["q67", "q76"]].corr())

# this function makes the q67 graph
# I made this function so the graph only shows when I click the button
def show_q67_graph():

    # this starts the graph and makes it bigger
    # I used 12 and 6 so the graph has enough room for the labels and legend
    plt.figure(figsize=(12, 6))

    # this makes a countplot for q67
    # it counts how many people picked each q67 response
    # hue="q67" gives each response its own color
    sns.countplot(
        x="q67",
        hue="q67",
        data=data,
        palette=["#9ecae1", "#6baed6", "#4292c6", "#2171b5"]
    )

    # this makes the graph background white
    # I used white so the graph looks cleaner
    plt.gca().set_facecolor("white")

    # this adds the title at the top
    plt.title("Q67 Responses")

    # this labels the x-axis
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    plt.ylabel("Number of People")

    # this changes the q67 code numbers into words
    # I did this so the graph is easier to understand
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this gets the legend parts from the graph
    # handles are the color boxes and labels are the names for them
    handles, labels = plt.gca().get_legend_handles_labels()

    # this makes clearer labels for the q67 legend
    # I wrote out what each number means so it is easier to read
    new_labels = [
        "0 = Lose Weight",
        "1 = Gain Weight",
        "2 = Stay the Same",
        "3 = Do Nothing"
    ]

    # this adds the legend to the side
    # I put it outside the graph so it does not block the bars
    plt.legend(
        handles,
        new_labels[:len(handles)],
        title="Q67 Response Meanings",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    # this fixes the spacing
    # I used this so nothing gets cut off
    plt.tight_layout()

    # this shows the graph
    plt.show()

# this function makes the q67 and q76 graph together
# I made this function so I can open the comparison graph with a button
def show_q67_q76_graph():

    # this starts a new graph and makes it bigger
    plt.figure(figsize=(12, 6))

    # this makes a countplot using q67 and q76
    # q67 goes on the x-axis
    # q76 is shown by different shades of blue
    sns.countplot(
        x="q67",
        hue="q76",
        data=data,
        palette=["#9ecae1", "#6baed6", "#4292c6", "#2171b5", "#08519c", "#6baed6", "#3182bd", "#08519c"]
    )

    # this makes the graph background white
    # I changed it to white so the bars show better
    plt.gca().set_facecolor("white")

    # this adds the title at the top
    plt.title("Relationship Between Q67 and Q76")

    # this labels the x-axis
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    plt.ylabel("Number of People")

    # this changes the q67 numbers into words
    # I did this so it is easier to understand than just seeing 0, 1, 2, and 3
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this gets the legend parts from the graph
    # handles are the color boxes and labels are the default names
    handles, labels = plt.gca().get_legend_handles_labels()

    # this list gives better names for q76
    # I used this so the legend shows what each number of days means
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

    # this adds the legend to the side of the graph
    # I put it outside the graph so it would not cover anything
    plt.legend(
        handles,
        new_labels[:len(labels)],
        title="Q76: Days Physically Active In The Past 7 Days",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    # this fixes the spacing so the legend fits better
    plt.tight_layout()

    # this shows the graph
    plt.show()

# this creates the GUI window
# I need this so the program has a window to put buttons on
window = tk.Tk()

# this gives the GUI window a title
window.title("YRBS Graph Viewer")

# this sets the size of the GUI window
# 500 is the width and 250 is the height
# I picked this size so the buttons and title would fit nicely
window.geometry("500x250")

# this changes the window background color
# I used a very light gray so it looks a little nicer
window.configure(bg="#f2f2f2")

# this makes the text at the top of the GUI
# I used a label so the user knows what to do
label = tk.Label(
    window,
    text="Click a button to display a graph",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)

# this puts the label on the window
# pady=20 adds space above and below it
label.pack(pady=20)

# this makes the first button
# when I click it, it runs the q67 graph function
button1 = tk.Button(
    window,
    text="Show Q67 Graph",
    command=show_q67_graph,
    width=25,
    bg="lightblue"
)

# this puts the first button on the window
# pady=10 adds some space around it
button1.pack(pady=10)

# this makes the second button
# when I click it, it runs the q67 and q76 graph function
button2 = tk.Button(
    window,
    text="Show Q67 and Q76 Graph",
    command=show_q67_q76_graph,
    width=25,
    bg="lightblue"
)

# this puts the second button on the window
button2.pack(pady=10)

# this keeps the GUI window open
# without this, the window would open and close right away
window.mainloop()
    
#------------------------End of Q66 and Q67 Analysis -------------------------#




















