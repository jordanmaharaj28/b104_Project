# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project Copy

# Libraries
# pandas helps read the data file
import pandas as pd
# seaborn helps make the graphs
import seaborn as sns
# matplotlib shows the graphs
import matplotlib.pyplot as plt
# tkinter is used to make the GUI window
import tkinter as tk

# this reads the data file
# "XXhq.txt" is the file name
# sep="\t" means the file is separated by tabs
data = pd.read_csv("XXhq.txt", sep="\t")

# this shows the first 5 values from q67
# .head() is just a quick way to check the column
print(data["q67"].head())

# this shows the first 5 values from q76
print(data["q76"].head())

# this prints all the column names
# I used this to make sure q67 and q76 were really in the file
print(data.columns)

# this changes q67 into numbers
# pd.to_numeric() converts values into numbers
# errors="coerce" means bad values turn into NaN
# NaN means the value is missing or not a real number
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# this changes q76 into numbers too
data["q76"] = pd.to_numeric(data["q76"], errors="coerce")

# this prints the correlation between q67 and q76
# .corr() checks if the two columns are related
print(data[["q67", "q76"]].corr())

# this function makes the q67 graph
# def means I am defining a function
# a function is just code that runs later when I call it
def show_q67_graph():

    # this starts a new graph window
    # figsize=(12, 6) means 12 inches wide and 6 inches tall
    # I picked that size so the graph has enough room for labels
    plt.figure(figsize=(12, 6))

    # this makes the bar graph for q67
    # x="q67" puts q67 on the x-axis
    # color="skyblue" makes the bars blue
    sns.countplot(x="q67", data=data, color="skyblue")

    # this changes the graph background color
    # plt.gca() means get current axes
    # the axes is the actual graph area where the bars are
    plt.gca().set_facecolor("lightgray")

    # this adds the title
    plt.title("Q67 Responses")

    # this labels the x-axis
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    plt.ylabel("Number of People")

    # this changes the q67 code numbers into words
    # ticks are the original values in the data
    # labels are the words I want to show instead
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this fixes spacing so labels do not get cut off
    plt.tight_layout()

    # this shows the graph
    plt.show()

# this function makes the q67 and q76 graph together
# def means define
# this function runs the code for the graph that compares q67 and q76
def show_q67_q76_graph():

    # this starts a new graph
    plt.figure(figsize=(12, 6))

    # this makes a countplot using q67 and q76
    # q67 goes on the x-axis
    # hue="q76" means q76 is shown with different colors
    # palette="Blues" uses shades of blue
    sns.countplot(x="q67", hue="q76", data=data, palette="Blues")

    # this changes the graph background color
    plt.gca().set_facecolor("lightgray")

    # this adds the title
    plt.title("Relationship Between Q67 and Q76")

    # this labels the x-axis
    plt.xlabel("Q67: What People Are Trying To Do About Their Weight")

    # this labels the y-axis
    plt.ylabel("Number of People")

    # this changes the q67 numbers into words
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Lose Weight", "Gain Weight", "Stay the Same", "Do Nothing"]
    )

    # this gets the legend pieces from the graph
    # handles means the little color boxes in the legend
    # labels means the words attached to those color boxes
    handles, labels = plt.gca().get_legend_handles_labels()

    # this list gives better names for q76
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

    # this adds the legend
    # plt.legend() makes the legend box
    # handles gives it the color boxes
    # new_labels[:len(labels)] makes sure the graph only uses as many labels as it needs
    # len(labels) means count how many legend labels there are
    # bbox_to_anchor=(1.05, 1) moves the legend a little to the right of the graph
    # 1.05 moves it a bit past the graph edge
    # 1 keeps it lined up near the top
    # loc="upper left" means the upper-left corner of the legend is placed there
    plt.legend(
        handles,
        new_labels[:len(labels)],
        title="Q76: Days Physically Active In The Past 7 Days",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    # this fixes spacing so the legend fits
    plt.tight_layout()

    # this shows the graph
    plt.show()

# this creates the main GUI window
# tk.Tk() starts the actual window
window = tk.Tk()

# this gives the window a title
# this is the name shown at the top of the window
window.title("YRBS Graph Viewer")

# this sets the size of the window
# "500x250" means 500 pixels wide and 250 pixels tall
# I picked this because it gives enough room for the title and buttons
# without making the window too huge
window.geometry("500x250")

# this changes the whole window background color
# I picked a very light gray so it looks cleaner than plain white
window.configure(bg="#f2f2f2")

# this makes the top message
# tk.Label() creates text inside the GUI window
# text= is what the label says
# font=("Arial", 14, "bold") means:
# Arial is the font style
# 14 is the font size
# bold makes the words thick
# bg= labels background color so it matches the window
label = tk.Label(
    window,
    text="Click a button to display a graph",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)

# this places the label in the window
# .pack() is a simple way to place things in tkinter
# pady=20 means add 20 pixels of space above and below the label
# I picked 20 so the top text is not too close to the edge
label.pack(pady=20)

# this makes the first button
# text= is what shows on the button
# command= tells the button what function to run when clicked
# width=25 makes the button wider so the text fits nicely
# bg= makes the button background light blue
button1 = tk.Button(
    window,
    text="Show Q67 Graph",
    command=show_q67_graph,
    width=25,
    bg="lightblue"
)

# this places the first button in the window
# pady=10 means 10 pixels of space above and below the button
# I picked 10 because it gives some space but not too much
button1.pack(pady=10)

# this makes the second button
# this button runs the second graph function
button2 = tk.Button(
    window,
    text="Show Q67 and Q76 Graph",
    command=show_q67_q76_graph,
    width=25,
    bg="lightblue"
)

# this places the second button in the window
# I used the same pady=10 so both buttons have equal spacing
button2.pack(pady=10)

# this keeps the GUI window open
# .mainloop() keeps the program running until the user closes the window
window.mainloop()
    
#------------------------End of Q66 and Q67 Analysis -------------------------#




















