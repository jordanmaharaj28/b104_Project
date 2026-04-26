# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project

# import libraries 
import pandas as pd             # used to load the data set
import seaborn as sns           # used to make the countplot graph
import matplotlib.pyplot as plt # used to show and customize the graph
import tkinter as tk            # used to make the GUI

# loads the YRBS data and tab seperates them and assigned to the variable "data"
data = pd.read_csv('XXhq.txt', sep = '\t')
 
# print the first few values of q66 and q67
print(data['q66'].head())
print(data['q67'].head())
# prints all the column names
print(data.columns)

#convert q66 into numbers so python can graph them
data["q66"] = pd.to_numeric(data["q66"], errors="coerce")
#convert q67 into numbers
data["q67"] = pd.to_numeric(data["q67"], errors="coerce")

# correlation between question 66 and question 67
data[["q66", "q67"]].corr()

# --- First Graph Attempt ---
#countplot made with bars and customized colors
<<<<<<< HEAD
# sns.countplot(x="q66", 
#               hue="q67", 
#               data=data, 
#               palette=['green', 'skyblue', 'darkblue', 'orange']
#               )
# # describes what each color in the small box means
# plt.legend(
#     title='Q67: Weight Goal', 
#     labels=['Lose Weight', 'Gain Weight', 'Stay The Same', 'Do Nothing']
#     )
=======
sns.countplot(x="q66", 
              hue="q67", 
              data=data, 
              palette=['green', 'skyblue', 'darkblue', 'orange']
              )

# replace the access labels 1.0 - 5.0 with text labels
plt.xticks(
    # position of the labels on teh x-axis
    ticks = [0, 1, 2, 3, 4,],
    # name of the labels
    labels = ['Very\n Underweight', 
               'Slightly\n Underweight',
               'About The\n Right Weight',
               'Slightly\n Overweight', 
               'Very\n Overweight']
    )

# describes what each color in the small box means
plt.legend(
    title='Q67: Weight Goal', 
    labels=['Lose Weight', 'Gain Weight', 'Stay The Same', 'Do Nothing']
    )
>>>>>>> f7ef5779bf1b70e2d8a1b8f12afdc4561949e6ab

# # added a title and labels on the each axis to better clarify it
# plt.title("Relationship Between Weight Perception (Q66) and Weight Goals (Q67)")
# plt.xlabel("Q66: Perception of Weight (1=Very Underweight to 5=Very Overweight)")
# plt.ylabel("Number of Students")
# # show the graph in the plots window
# plt.show()



# ------------------------ GUI Functions -------------------------------
# the Function that runs when anyone presses the "Show Graph" button in the GUI

def graph():
    #countplot made with bars and customized colors
    sns.countplot(x='q66', 
                  hue='q67', 
                  data=data, 
                  palette=['green', 'skyblue', 'darkblue', 'orange']
                  )
    # replace the access labels 1.0 - 5.0 with text labels
    plt.xticks(
        # position of the labels on teh x-axis
        ticks = [0, 1, 2, 3, 4,],
        # name of the labels
        labels = ['Very\n Underweight', 
                  'Slightly\n Underweight',
                  'About The\n Right Weight',
                  'Slightly\n Overweight', 
                  'Very\n Overweight']
        )
    
    # describes what each color in the small box means
    plt.legend(
        title='Q67: Weight Goal', 
        labels=['Lose Weight', 'Gain Weight', 'Stay The Same', 'Do Nothing']
        )

    # added a title and axis labels to better clarify it
    plt.title('Relationship Between Weight Perception (Q66) and Weight Goals (Q67)')
    plt.xlabel('Q66: Perception of Weight')
    plt.ylabel('Number of Students')
    # show the graph
    plt.show()
    
# the Function that runs when anyone pressed the "Show Graph 2" button in the GUI    

def graph_2():
    # chose a boxplot because Q76 is numberic (0-7 days) and makes it easier to read than a countplot
    sns.boxplot(x='q66', 
                  y='q76',
                  data = data, 
                  palette=['lightgreen', 'skyblue', 'pink', 'orange', 'red'])
    
    # replace the access labels 1.0 - 5.0 with text labels
    plt.xticks(
        # position of the labels on teh x-axis
        ticks = [0, 1, 2, 3, 4,],
        # name of the labels
        labels = ['Very\n Underweight', 
                  'Slightly\n Underweight',
                  'About The\n Right Weight',
                  'Slightly\n Overweight', 
                  'Very\n Overweight']
        )
    
    # Title and labels explaining what everything on the graph shows
    plt.title('Weight Perception (Q66) and Physical Activity (Q76)')
    plt.xlabel('Q66: Perception of Weight')
    plt.ylabel('Q76: Days Phyically Active Over The Past 7 Days')
    # show the graph
    plt.show()
    
    
    
    
# ------- GUI -------

# makes the GUI window
window = tk.Tk()

# Title of the window
window.title('GUI')

# makes a button called "Show Graph" and it runs the graph when clicked on
btn1 = tk.Button(window, text = 'Show Graph', command = graph)
btn1.pack() # puts the button in the window

# makes the second button called "Show Graph 2"
btn2 = tk.Button(window, text = 'Show Graph 2', command = graph_2)
btn2.pack()

# keeps the window open until someone closes it
window.mainloop()












