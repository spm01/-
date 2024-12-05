#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 
import tkinter as tk
import pygame
import glob
from tkinter import ttk, messagebox

#read csv file
df1=pd.read_csv("https://www.cs.nccu.edu.tw/~sichiu/restaurant_nccu.csv")
r_type=df1["type"].drop_duplicates().tolist()

#set window size
win=tk.Tk()
win.geometry("600x400")
win.title("Restaurant Recs")

#declare variable for tk module
combo_var1=tk.StringVar()
entry_var = tk.StringVar()

#define functions
def myfun():
    try:
        #convert entry_var into float
        max_distance = float(entry_var.get())
        
        #select data points by condition
        #can also select by 2 conditions: df1[(condition_1) & (condition_2)]
        df_result=df1[(df1["type"]==combo_var1.get()) & (df1["distance_km"]<=max_distance)]
        r_list=df_result["restaurant"].tolist()
        
        #prep message
        message="Recommended Restaurants:\n"
        if len(r_list) == 0:
            messagebox.showinfo("Results", "No restaurants found")
        else:
            for restaurant in r_list:
                message += restaurant + "\n"
        messagebox.showinfo("Results", message)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid number for distance.")

#set widgets
#title label
label_1 = tk.Label(win,text="Restaurant Recs", fg="black", font=("Arial",18))
label_1.place(x=225,y=1)
#option label
label_3=tk.Label(win,text="Choices", fg="black",font=("Arial",14))
label_3.place(x=225, y=40)
#restaurant style
label_2=tk.Label(win,text="Restaurant Style", fg="black", font=("Arial", 14))
label_2.place(x=20,y=70)
#restaurant style combobox
combo_var1.set(r_type[0])
combo_1=ttk.Combobox(win,textvariable=combo_var1,value=r_type)
combo_1.place(x=180, y=70)

#desired distance widget
#desired distance label
label_4=tk.Label(win,text="Desired distance", fg="black", font=("Arial",14))
label_4.place(x=20, y=100)
#input box
entry_1=tk.Entry(win,textvariable=entry_var, width=10)
entry_1.place(x=180, y=100)

#confirm choices button
button_1=tk.Button(win,text="Confirm Choices", command=myfun)
button_1.place(x=225,y=250)

win.mainloop()

