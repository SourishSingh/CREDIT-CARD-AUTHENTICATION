from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("H")
root.geometry("600x500")
root.configure(background="#A9FFC2")

lbl=Label(root,fg="red")
lbl.place(relx=0.5,rely=0.6,anchor=CENTER)

entr=Entry(root)
entr.place(relx=0.5,rely=0.5,anchor=CENTER)

def en():
    b=entr.get()
    try:
        print(b+0)
    except(TypeError):
        messagebox.showerror("Alert","There was a error in typing the code")
        lbl["text"]="Type it again"
    c=len(b)
    if(b!=4):
        messagebox.showinfo("Alert","Credit Card Pincode should be 4 lettered")
        lbl["text"]="Type it again"

btn=Button(root,text="add",command=en,background="#0A465D",fg="white")
btn.place(relx=0.6,rely=0.5,anchor=CENTER)

root.mainloop()
