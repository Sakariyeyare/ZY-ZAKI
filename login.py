from tkinter import*
from tkinter import messagebox
root = Tk()
root.title('Login')
root.geometry('300x300')

text_input = StringVar()
operator=''
def ok():
    username=e1.get()
    password=e2.get()

    if(username=="" and password==""):
        messagebox.showwarning('Digniin',"Blank Not Allowed")
    elif(username=="Admin" and password=="1234"):
        messagebox.showinfo('Success',"Login successfull")
        root.destroy()

    else:
        messagebox.showerror('Error',"Incorrect username and password")

def reset():

    username = e1.get()
    password = e2.get()


global e1
global e2
Label(root, text="Username").place(x=10,y=10)
Label(root, text="Password").place(x=10,y=40)
e1 = Entry(root)
e1.place(x=140,y=10)

e2 = Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")

Button(root,text="Login", command=ok, height=3,width=13).place(x=10,y=100)
Button(root,text="Reset", command=reset(), height=3,width=13).place(x=150,y=100)


root.resizable(0,0)
root.mainloop()