# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

# Libraries
# pandas helps me read the data file and work with it like a table
import pandas as pd
# seaborn helps me make graphs
import seaborn as sns
# matplotlib helps me show the graphs and add titles and labels
import matplotlib.pyplot as plt
# tkinter helps me make the GUI window and buttons
import tkinter as tk

# this reads the data file and stores it in a variable called data
# pd.read_csv() opens the file and reads it into Python
# "XXhq.txt" is the file name
# sep="\t" means the values in the file are separated by tabs
data = pd.read_csv("XXhq.txt", sep="\t")

# this shows the first 5 values from q67
# .head() only shows the first few rows
# I used this to make sure the data loaded right
print(data["q67"].head())

# this shows the first 5 values from q76
# I checked this one too for the same reason
print(data["q76"].head())

# this prints all the column names in the file
# .columns gives the names of every column
# I used this to make sure q67 and q76 were really there
print(data.columns)

# this changes q67 into numbers
# pd.to_numeric() tries to turn values into numbers
# errors="coerce" means if something cannot turn into a number,
# Python changes it to NaN instead of crashing
# NaN means the value is missing or invalid
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# this changes q76 into numbers too
# I did this because numbers are easier to graph and compare
data["q76"] = pd.to_numeric(data["q76"], errors="coerce")

# this prints the correlation between q67 and q76
# data[["q67", "q76"]] picks only those two columns
# .corr() checks if the two columns are related
print(data[["q67", "q76"]].corr())

# def means define
# this is how I create a function in Python
# a function is just a block of code I can run later
# I made this function so the q67 graph only shows when I click the button
def show_q67_graph():

    # this starts the graph window
    # plt.figure() creates a new graph
    # figsize means figure size
    # 12 is the width and 6 is the height
    # I picked 12 by 6 so the graph has enough room for the labels and legend
    plt.figure(figsize=(12, 6))

    # this makes a countplot for q67
    # sns.countplot() counts how many times each q67 value appears
    # x="q67" puts q67 on the x-axis
    # hue="q67" gives each q67 response its own color
    # data=data tells seaborn to use the table called data
    # palette picks the colors in order
    sns.countplot(
        x="q67",
        hue="q67",
        data=data,
        palette=["lightblue", "skyblue", "cornflowerblue", "steelblue"]
    )

    # this changes the graph background to white
    # plt.gca() means get current axes
    # the axes is the graph area where the bars are drawn
    # .set_facecolor() changes the background color of that graph area
    plt.gca().set_facecolor("white")

    # this adds the title at the top of the graph
    # plt.title() is used to name the graph
    plt.title("Q67 Responses")

    # this labels the x-axis
    # plt.xlabel() adds a label under the graph
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    # plt.ylabel() adds a label to the side of the graph
    plt.ylabel("Number of People")

    # this changes the q67 numbers into words
    # plt.xticks() changes the labels on the x-axis
    # ticks are the real code numbers in the data
    # labels are the words I want to show instead
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this gets the legend parts from the graph
    # handles are the little color boxes
    # labels are the default words next to those boxes
    handles, labels = plt.gca().get_legend_handles_labels()

    # this makes better legend labels for q67
    # I wrote out what each number means so the graph is easier to understand
    new_labels = [
        "0 = Lose Weight",
        "1 = Gain Weight",
        "2 = Stay the Same",
        "3 = Do Nothing"
    ]

    # this adds the legend to the graph
    # plt.legend() makes the legend box
    # handles gives the color boxes
    # new_labels[:len(handles)] only uses the labels I need
    # len(handles) counts how many color groups are in the graph
    # title= adds a title above the legend
    # bbox_to_anchor moves the legend outside the graph
    # 1.05 moves it a little to the right
    # 1 keeps it near the top
    # loc="upper left" means the upper-left corner of the legend goes there
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
    # plt.show() tells Python to display the graph
    plt.show()

# def means define again
# this function makes the comparison graph for q67 and q76
# I made this function so it can run when I click the second button
def show_q67_q76_graph():

    # this starts a new graph
    # I used the same size so both graphs look similar
    plt.figure(figsize=(12, 6))

    # this makes a countplot for q67 and q76
    # q67 goes on the x-axis
    # hue="q76" means q76 is shown by different colors
    # palette gives different shades of blue
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

    # this changes the graph background to white
    # I used white so the colors show better
    plt.gca().set_facecolor("white")

    # this adds the title at the top
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
    # labels are the default words for them
    handles, labels = plt.gca().get_legend_handles_labels()

    # this gives better labels for q76
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
    # I moved it outside so it does not cover the bars
    plt.legend(
        handles,
        new_labels[:len(labels)],
        title="Q76: Days Physically Active In The Past 7 Days",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    # this fixes the spacing so the legend and labels fit better
    plt.tight_layout()

    # this shows the graph
    plt.show()

# this creates the GUI window
# tk.Tk() starts the actual window
window = tk.Tk()

# this gives the window a title
# this is the name shown at the top of the GUI
window.title("YRBS Graph Viewer")

# this sets the size of the GUI window
# 500 is the width and 250 is the height
# I picked this size so the title and buttons would fit nicely
window.geometry("500x250")

# this changes the background color of the whole window
# I used a light gray so the window looks a little nicer
window.configure(bg="#f2f2f2")

# this makes the message at the top of the window
# tk.Label() creates text inside the GUI
# text= is what the label says
# font=("Arial", 14, "bold") means font style, size, and bold
# bg= makes the label background match the window
label = tk.Label(
    window,
    text="Click a button to display a graph",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)

# this places the label on the window
# .pack() is a simple way to place things in tkinter
# pady=20 means add 20 pixels of space above and below the label
# I used 20 so the top text would not be too close to the edge
label.pack(pady=20)

# this makes the first button
# tk.Button() creates a button
# text= is what the button says
# command= tells the button what function to run when clicked
# width=25 makes the button wider so the text fits better
# bg changes the button color
button1 = tk.Button(
    window,
    text="Show Q67 Graph",
    command=show_q67_graph,
    width=25,
    bg="lightblue"
)

# this places the first button on the window
# pady=10 adds space above and below the button
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

# this places the second button on the window
button2.pack(pady=10)

# this keeps the GUI window open
# without this, the window would close right away
window.mainloop()
    
#------------------------End of Q66 and Q67 Analysis -------------------------#




















