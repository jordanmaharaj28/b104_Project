# Developer:  Maharaj, Jordan  Lopez, Luis
# Course:     B104
# Assignment: Final Project

# import libraries 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk

# loads the YRBS data
df = pd.read_csv('XXhq.txt', sep = '\t')
 
print(df['q66'].head())
print(df['q67'].head())
print(df.columns)

#convert q66 into numbers
df["q66"] = pd.to_numeric(df["q66"], errors="coerce")
#convert q67 into numbers
df["q67"] = pd.to_numeric(df["q67"], errors="coerce")

# correlation between question 66 and question 67
df[["q66", "q67"]].corr()

#countplot made with bars and customized colors
sns.countplot(x="q66", 
              hue="q67", 
              data=df, 
              palette=['green', 'skyblue', 'darkblue', 'orange']
              )
# describes what each color in the small box means
plt.legend(
    title='Q67: Weight Goal', 
    labels=['Lose Weight', 'Gain Weight', 'Stay The Same', 'Do Nothing']
    )

# added a title and axis labels to better clarify it
plt.title("Relationship Between Weight Perception (Q66) and Weight Goals (Q67)")
plt.xlabel("Q66: Perception of Weight (1=Very Underweight to 5=Very Overweight)")
plt.ylabel("Number of Students")
# show the graph
plt.show()

# the function that runs when anyone presses the "Show Graph" button in the GUI
def graph():
    #countplot made with bars and customized colors
    sns.countplot(x="q66", 
                  hue="q67", 
                  data=df, 
                  palette=['green', 'skyblue', 'darkblue', 'orange']
                  )
    # describes what each color in the small box means
    plt.legend(
        title='Q67: Weight Goal', 
        labels=['Lose Weight', 'Gain Weight', 'Stay The Same', 'Do Nothing']
        )

    # added a title and axis labels to better clarify it
    plt.title("Relationship Between Weight Perception (Q66) and Weight Goals (Q67)")
    plt.xlabel("Q66: Perception of Weight (1=Very Underweight to 5=Very Overweight)")
    plt.ylabel("Number of Students")
    # show the graph
    plt.show()
    
# ----- GUI -----
# makes the GUI window
window = tk.TK()
# Title of the window
window.title('GUI')
# makes a button called "Show Graph" and it runs the graph when clicked on
btn1 = tk.Button(window, text = 'Show Graph', command = graph)
btn1.pack()

# keeps the window open until someone closes it
window.mainloop()












