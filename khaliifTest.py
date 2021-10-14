from tkinter import*
from  tkinter import  messagebox
root=Tk()
root.title('Register form')
root.configure(bg='light grey')
root.geometry("600x385")
root.state('zoomed')
root.resizable(0,0)

zak=Label( text="JAMHUURIYA UNIVERSITY",fg='blue' , bg='lightgrey', font=('Times New Roman', 60, 'underline','bold')).place(x=10,y=0)
title = Label( text="REGISTER HERE", font=("times new roman", 28, "bold"), bg='lightgrey',
              fg='black').place(x=10, y=107)
Name = Label( text=" Name*", font=("times new roman", 24, "bold"), bg='lightgrey',
                   fg='black').place(x=0, y=170)
txt_firstname = Entry( font=("times new roman", 15,),bd=3, bg="white").place(x=10, y=210, width=400)

Name = Label( text=" First", font=("times new roman", 15, ), bg='lightgrey',
                   fg='black').place(x=0, y=240)

txt_lasttname = Entry( font=("times new roman", 15,),bd=3, bg="white").place(x=700, y=210, width=400)
last_name = Label( text="Last ", font=("times new roman", 15, ), bg='lightgrey',
                  fg='black').place(x=700, y=240)
username= Label( text=" Username*", font=("times new roman", 24, "bold"), bg='lightgrey',
                   fg='black').place(x=0, y=280)
txt_username = Entry( font=("times new roman", 15,),bd=3, bg="white").place(x=10, y=325, width=1300)
email= Label( text=" Email*", font=("times new roman", 24, "bold"), bg='lightgrey',
                   fg='black').place(x=0, y=380)
txt_email = Entry( font=("times new roman", 15,),bd=3, bg="white").place(x=10, y=425, width=1300)
password= Label( text=" Password*", font=("times new roman", 24, "bold"), bg='lightgrey',
                   fg='black').place(x=0, y=480)
txt_password = Entry( font=("times new roman", 15,),bd=3, bg="white").place(x=10, y=525, width=1300)
confirmpassword= Label( text="Confirm password*", font=("times new roman", 24, "bold"), bg='lightgrey',
                   fg='black').place(x=0, y=580)

txt_confirmpassword = Entry( font=("times new roman", 15,),bd=3, bg="white").place(x=10, y=625, width=1300)

check=Checkbutton( text="Forget Password",onvalue=1,offvalue=0,bg='lightgrey',
                          fg='black').place(x=10, y=660)

Button(root,text="Submit",bg='red',fg='white',  height=3,width=13).place(x=150,y=675)
Button(root,text="Login",bg='blue',fg='white',  height=3,width=13).place(x=850,y=675)

root.mainloop()