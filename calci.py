import tkinter as tk

def click(event):
    current_text=entry.get()
    button_text=event.widget.cget("text")

    if button_text=="=":
        try:
            result=str(eval(current_text))
            entry.delete(0,tk.END)
            entry.insert(0,result)
        except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(0,"Error")
    elif button_text=="C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,button_text)




root=tk.Tk()
root.title("My Calculator")

entry=tk.Entry(root,font="Helvetica 16",borderwidth=5,relief=tk.RIDGE)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky="nsew")


buttons=[
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
]

for i,row in enumerate(buttons):
    for j,text in enumerate(row):
        button=tk.Button(root,text=text,font="Helvetica 16",borderwidth=5,relief=tk.RIDGE)
        button.grid(row=i+1,column=j,padx=5,pady=5,sticky="nsew")
        button.bind("<Button-1>",click)
for i in range(4):
    root.grid_columnconfigure(i,weight=1)
for i in range(5):
    root.grid_rowconfigure(i,weight=1)
    
root.mainloop()