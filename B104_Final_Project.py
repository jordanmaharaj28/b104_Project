# Developer: Maharaj, Jordan Lopez, Luis
# Course: B104
# Assignment: Final Project Copy

# Step 1: Import the libraries
# In this step I import the libraries I need for the program.

# Libraries
# pandas helps me read the data file and work with it like a table
import pandas as pd
# seaborn helps me make the graphs
import seaborn as sns
# matplotlib helps me show the graphs and add labels and titles
import matplotlib.pyplot as plt
# tkinter helps me make the GUI window, text, and buttons
import tkinter as tk

# Step 2: Load the data
# In this step I open the data file and store it in a variable called data.

# this reads the data file
# pd.read_csv() opens the file and loads it into Python
# sep="\t" means the file is tab separated
data = pd.read_csv(
    "/Users/lopez/Documents/GitHub/b104_Project/XXhq.txt", sep="\t")

# Step 3: Check the data
# In this step I print a few values and the column names.
# this prints the first 5 values from q67
# .head() is just a quick way to check that the data loaded right
print(data["q67"].head())

# this prints the first 5 values from q76
print(data["q76"].head())

# this prints all the column names
# I used this to make sure q67 and q76 were in the file
print(data.columns)

# Step 4: Clean up the data
# this changes q67 into numbers
# pd.to_numeric() tries to turn the values into numbers
# errors="coerce" means bad values get changed into NaN instead of crashing
# NaN means the value is missing or not a real number
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# this changes q76 into numbers too
# I did this so it would be easier to graph and compare
data["q76"] = pd.to_numeric(data["q76"], errors="coerce")

# Step 5: Check the relationship between q67 and q76
# In this step I print the correlation.

# this shows the correlation between q67 and q76
# .corr() checks if the two columns are related
print(data[["q67", "q76"]].corr())

# Step 6: Make the first graph function
# def means define
# this is how I make a function in Python
# a function is a block of code that I can run later
# I made this function so the q67 graph only shows when I click the button


def show_q67_graph():

    # this starts a new graph
    # plt.figure() creates the graph area
    # figsize means figure size
    # 12 is the width and 6 is the height
    # I picked 12 and 6 so the graph has enough room for the labels and legend
    plt.figure(figsize=(12, 6))

    # this makes the q67 graph
    # sns.countplot() counts how many times each q67 value appears
    # x="q67" puts q67 on the x-axis
    # hue="q67" gives each q67 response its own color
    # data=data tells seaborn to use my dataset called data
    # palette picks the colors for each q67 bar
    sns.countplot(
        x="q67",
        hue="q67",
        data=data,
        palette=["lightblue", "skyblue", "cornflowerblue", "steelblue"]
    )

    # this changes the graph background color
    # plt.gca() means get current axes
    # the axes is the actual graph area where the bars are drawn
    # set_facecolor() changes the background color of that area
    plt.gca().set_facecolor("white")

    # this adds the title at the top
    # plt.title() gives the graph a name
    plt.title("Q67 Responses")

    # this labels the x-axis
    # plt.xlabel() puts words under the graph
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    # plt.ylabel() puts words on the side of the graph
    plt.ylabel("Number of People")

    # this changes the q67 code numbers into words
    # plt.xticks() changes the labels on the x-axis
    # ticks are the real number codes in the data
    # labels are the words I want to show instead
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this gets the legend parts from the graph
    # handles are the little color boxes in the legend
    # labels are the default words next to those boxes
    handles, labels = plt.gca().get_legend_handles_labels()

    # This list gives clearer legend labels for q67
    # I wrote what each number means so the graph is easier to read
    new_labels = [
        "0 = Lose Weight",
        "1 = Gain Weight",
        "2 = Stay the Same",
        "3 = Do Nothing"
    ]

    # this adds the legend to the graph
    # plt.legend() makes the legend box
    # handles gives the color boxes
    # new_labels[:len(handles)] only uses as many labels as I need
    # len() counts how many items are in something
    # len(handles) counts how many legend color boxes there are
    # bbox_to_anchor moves the legend to a different spot
    # 1.05 moves it a little to the right of the graph
    # 1 keeps it lined up near the top
    # I picked 1.05 and 1 so the legend would not cover the bars
    # loc means location
    # loc="upper left" means use the upper-left corner of the legend box there
    plt.legend(
        handles,
        new_labels[:len(handles)],
        title="Q67 Response Meanings",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    # this fixes the spacing
    # plt.tight_layout() helps stop labels or the legend from getting cut off
    plt.tight_layout()

    # this shows the graph
    # plt.show() displays the graph window
    plt.show()

# Step 7: Make the second graph function
# I made another function for the comparison graph.
# this makes the second graph function
# It also opens when I click the second button


def show_q67_q76_graph():

    # this starts a new graph
    # I used the same size so both graphs look consistent
    plt.figure(figsize=(12, 6))

    # this makes the comparison graph
    # x="q67" puts q67 on the x-axis
    # hue="q76" means q76 is shown using different colors
    # palette gives each q76 response its own shade of blue
    sns.countplot(
        x="q67",
        hue="q76",
        data=data,
        palette=[
            "lightblue",
            "skyblue",
            "deepskyblue",
            "cornflowerblue",
            "royalblue",
            "steelblue",
            "dodgerblue",
            "navy"
        ]
    )

    # I used white so the bars are easier to see
    plt.gca().set_facecolor("white")

    # this adds the title
    plt.title("Relationship Between Q67 and Q76")

    # this labels the x-axis
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    plt.ylabel("Number of People")

    # this changes the q67 code numbers into words
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this gets the legend parts from the graph
    # handles are the color boxes
    # labels are the default legend names
    handles, labels = plt.gca().get_legend_handles_labels()

    # this gives better labels for q76
    # I used this so the legend explains what each number of days means
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

    # this adds the legend to the side
    # bbox_to_anchor=(1.05, 1) moves the legend a little to the right and near the top
    # I picked these numbers so the legend would not block the graph
    # loc="upper left" tells Python which corner of the legend to place at that spot
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

# Step 8: Build the GUI window
# In this step I create the main GUI window.
# this creates the main GUI window
# tk means tkinter
# tk.Tk() starts the actual GUI window
window = tk.Tk()

# this gives the window a title
# this is the name that shows at the top of the GUI
window.title("YRBS Graph Viewer")

# this sets the size of the GUI window
# geometry("500x250") means 500 pixels wide and 250 pixels tall
# I picked this size because it gives enough room for the title and both buttons
window.geometry("500x250")

# this changes the background color of the whole window
# bg means background color
window.configure(bg="#f2f2f2")

# this makes the text at the top of the window
# tk.Label() creates text inside the GUI
# text is what the label says
# font changes the style and size of the text
# bg changes the label background so it matches the window
label = tk.Label(
    window,
    text="Click a button to display a graph",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)

# this puts the label on the window
# pack() is a simple way to place something in tkinter
# pady means padding on the y direction, so top and bottom space
# pady=20 means add 20 pixels of space above and below the label
# I picked 20 so the text would not be too close to the top edge
label.pack(pady=20)

# this makes the first button
# tk.Button() creates a button
# text is what the button says
# command tells the button which function to run when clicked
# width=25 makes the button wider so the text fits nicely
# bg changes the button background color
button1 = tk.Button(
    window,
    text="Show Q67 Graph",
    command=show_q67_graph,
    width=25,
    bg="lightblue"
)

# this puts the first button on the window
# pady=10 means add 10 pixels of space above and below the button
# I picked 10 so there is some space but not too much
button1.pack(pady=10)

# this makes the second button
# this one runs the q67 and q76 graph function
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
# mainloop() keeps the program running until I close the window
window.mainloop()

# ------------------------End of Q66 and Q67 Analysis -------------------------#
