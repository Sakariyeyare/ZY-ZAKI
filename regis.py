from  tkinter import  *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk

class Register:

    def __init__(self,root):
        self.root = root
        self.root.title("Form Registration")
        self.root.geometry("1350x700+0+0")

        self.root.config(bg="white")
        text_input = StringVar()
        operator = ''

        def ok():
            password = e1.get()

            confirm_password = e2.get()

            if (password == "" and confirm_password == ""):
                messagebox.showwarning('Digniin', "Blank Not Allowed")
            elif (password == "1234" and confirm_password == "1234"):
                messagebox.showinfo('Success', "Login successfull")
                root.destroy()

            else:
                messagebox.showerror('Error', "Incorrect username and password")

        self.bg = ImageTk.PhotoImage(Image.open("img6.jpg"))
        bg = Label(self.root, image=self.bg).place(x=250, y=0,relwidth=1,relheight=1)
        self.left = ImageTk.PhotoImage(Image.open("img7.jpg"))
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        fram1=Frame(self.root,bg="white").place(x=480,y=100,width=700,height=500)
        zak=Label(fram1, text="JAMHUURIYA UNIVERSITY",bd=0, font=('Times New Roman', 60, 'bold')).place(x=10,y=0)

        title =Label(fram1, text="REGISTER HERE",font=("times new roman",20,"bold"),bg='white',
                     fg='green').place(x=490,y=107)
        first_name = Label(fram1, text="First Name", font=("times new roman", 20, "bold"), bg='white',
                      fg='gray').place(x=490, y=170)
        txt_firstname = Entry(fram1,font=("times new roman",15, ),bg="lightgray").place(x=490, y=210,width=250)
        last_name = Label(fram1, text="Last Name", font=("times new roman", 20, "bold"), bg='white',
                           fg='gray').place(x=900, y=175)
        txt_lasttname = Entry(fram1, font=("times new roman", 15,), bg="lightgray").place(x=900, y=210, width=250)

        contact_no = Label(fram1, text="Contact No.", font=("times new roman", 20, "bold"), bg='white',
                           fg='gray').place(x=490, y=240)
        txt_contact = Entry(fram1, font=("times new roman", 15,), bg="lightgray").place(x=900, y=290, width=250)
        email = Label(fram1, text="Email", font=("times new roman", 20, "bold"), bg='white',
                          fg='gray').place(x=900, y=250)
        txt_email = Entry(fram1, font=("times new roman", 15,), bg="lightgray").place(x=490, y=280, width=250)

        quation = Label(fram1, text="Security Quation ", font=("times new roman", 20, "bold"), bg='white',
                           fg='gray').place(x=490, y=330)
        txt_quation = ttk.Combobox(fram1, font=("times new roman", 13), state="readonly", justify=CENTER)
        txt_quation["values"]=("select","Your first pet name ","Your birth place","Your best friend name")
        txt_quation.place(x=490, y=370, width=250)
        txt_quation.current(0)
        answers= Label(fram1, text="Answer", font=("times new roman", 20, "bold"), bg='white',
                          fg='gray').place(x=900, y=330)
        txt_answer = Entry(fram1, font=("times new roman", 15,), bg="lightgray").place(x=900, y=370, width=250)

        password = Label(fram1, text="Password", font=("times new roman", 20, "bold"), bg='white',
                           fg='gray').place(x=490, y=430)


        confirm_password = Label(fram1, text="Confirm Password", font=("times new roman", 20, "bold"), bg='white',
                      fg='gray').place(x=900, y=430)
        e1 = Entry(root, bg='white', fg='black', bd=2, width=20, font=('arial', 15, 'bold'))
        e1.place(x=490, y=480)
        e1.config(show='*')
        e2 = Entry(root, bg='white', fg='black', bd=2, width=20, font=('arial', 15, 'bold'))
        e2.place(x=900, y=480)
        e2.config(show='*')



        check=Checkbutton(fram1, text="I Agree The Terms & Conditions",onvalue=1,offvalue=0,bg='white',
                          fg='black').place(x=490, y=520)


        self.btn_img=ImageTk.PhotoImage(Image.open("img3.png"))
        btn=Button(fram1,image=self.btn_img,bd=0,cursor='hand2',bg="white").place(x=700,y=530)

        self.btn_signin = ImageTk.PhotoImage(Image.open("img10.jpg"))
        btn_signin = Button(fram1, image=self.btn_signin, bd=0, cursor='hand2', bg="white",command=ok).place(x=130, y=330)
root = Tk()
obj= Register(root)
root.mainloop()















