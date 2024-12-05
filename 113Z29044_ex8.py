#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#set window size
win=tk.Tk()
win.geometry("600x400")

#bring window to foreground
win.lift()
win.attributes("-topmost", True)
win.after(1, lambda: win.attributes("-topmost", False))

#define variables for tkinter function
q1=tk.IntVar()
q2=tk.IntVar()
q3=tk.StringVar()
q4=tk.IntVar()

#define function
def myfun():
    total_score=q1.get() + q2.get() + q4.get()
    sleep_hours = int(q3.get())
    if total_score >=3 and q3.get()>=7:
        message="You have a healthy lifestyle!"
    else:
        message="You need to improve your lifestyle."
    messagebox.showinfo("Survey Results", message)

#questionaire title
label_1_title=tk.Label(win,text="Health Questionaire", fg="black")
label_1_title.place(x=200,y=1)

#question1
label_q1 = tk.Label(win, text="1. Do you smoke?", fg="black")
label_q1.place(x=50,y=50)
q1_r1=tk.Radiobutton(win,text="yes",variable=q1,value=1)
q1_r1.place(x=180,y=50)
q1_r2=tk.Radiobutton(win,text="no",variable=q1,value=0)
q1_r2.place(x=230,y=50)

#question2
label_q2 = tk.Label(win,text="2. Do you drink?", fg="black")
label_q2.place(x=50,y=100)
q2_r1=tk.Radiobutton(win,text="yes",variable=q2,value=1)
q2_r1.place(x=180,y=100)
q2_r2=tk.Radiobutton(win,text="no",variable=q2,value=0)
q2_r2.place(x=230,y=100)

#question3
label_q3=tk.Label(win,text="3. How much do you sleep per night?", fg="black")
label_q3.place(x=50, y=150)
sleep=[i for i in range(1,25)]
q3.set(sleep[0])
c1=ttk.Combobox(win,value=sleep,textvariable=q3)
c1.place(x=300, y=150)

#question4
label_q4=tk.Label(win,text="4. Do you have a balanced diet?", fg="black")
label_q4.place(x=50, y=200)
q4_r1=tk.Radiobutton(win,text="yes",variable=q4,value=0)
q4_r1.place(x=270,y=200)
q4_r2=tk.Radiobutton(win,text="no",variable=q4,value=1)
q4_r2.place(x=330,y=200)

#submit button
button_1=tk.Button(win,text="Submit Form", command=myfun)
button_1.place(x=250,y=300)

win.mainloop()


# In[ ]:





# In[ ]:




