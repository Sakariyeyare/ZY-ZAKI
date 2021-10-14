from tkinter import *
import random
import  time
root = Tk()
root.title('Beder Restaurent')
root.state('zoomed')
root.resizable(0,0)
text_input = StringVar()
operator=''
#frams
tops = Frame(root, width=1600, height=70, bg='powder blue', relief=SUNKEN)
tops.pack(side=TOP)
f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)
f2 = Frame(root, width=300, height=700,  relief=SUNKEN)
f2.pack(side=RIGHT)
#TIME
localtime = time.asctime(time.localtime(time.time()))
#Information
Information = Label(tops, font=('arial', 50, 'bold'), text="Beder Restaurent",   fg='steel blue', bd=10, anchor='w')
Information.grid(row=0, column=0)
Information = Label(tops, font=('arial', 20, 'bold'), text=localtime,  fg='steel blue', bd=10, anchor='w')
Information.grid(row=1, column=0)
#calculation functions
def clock():
    hours=time.strftime("%I")
    MINUTES=time.strftime("%M")
    SEC=time.strftime("%S")
    Information.config(text=hours+":"+ MINUTES+":"+SEC)
    Information.after(1000,clock)
clock()
def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
def button_clearDisplay():

    global operator
    operator =''
    text_input.set('')
def button_equalInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator =''
def Ref():
    # x=random.randint(12908, 50876)
    # randomRef=str(x)
    # rand.set(randomRef)
    coF=float(Fries.get())
    coD = float(Drinks.get())
    coFilet = float(Filet.get())
    coBurger = float(Burger.get())
    coChicken= float(Chicken.get())
    coCheese = float(Cheese.get())
    costoffries=coF * 0.99
    costofdrinks=coD * 1.00
    costoffilet=coFilet * 2.99
    costofburger=coBurger * 2.87
    costofchicken= coChicken * 2.89
    costofCheese= coCheese * 2.69
    costofmeal="$", str("%.2f" % (costoffries + costofdrinks + costoffilet + costofburger + costofCheese
                                   + costofchicken))
    payTax =((costoffries + costofdrinks + costoffilet + costofburger + costofCheese
                                   + costofchicken) * 0.2)
    Totalcost=((costoffries + costofdrinks + costoffilet + costofburger + costofCheese
                                + costofchicken))
    Ser_Charger = ((costoffries + costofdrinks + costoffilet + costofburger + costofCheese
                                   + costofchicken) / 99)
    Service='$',str("%.2f" % Ser_Charger)
    overallcost='$',str("%.2f" % (payTax + Totalcost + Ser_Charger))
    paidTax='$',str("%.2f" % payTax)
    Service_Charger.set(Service)
    Cost.set(costofmeal)
    Tax.set(paidTax)
    SubTotal.set(costofmeal)
    Total.set(overallcost)
def Exit():
    root.destroy()
def Reset():
    rand.set('')
    Fries.set('')
    Burger.set('')
    Filet.set('')
    SubTotal.set('')
    Total.set('')
    Service_Charger.set('')
    Chicken.set('')
    Cheese.set('')
    Tax.set('')
    Cost.set('')
    Drinks.set('')

text_display = Entry(f2, font=("arial", 20, "bold"), textvariable=text_input, bg='#fff', bd=30, insertwidth=4,
                      justify='right')
text_display.grid(columnspan=4)
button7 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='7', \
                                                         command=lambda :button_click(7)).grid(row=2, column=0)
button8 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='8', \
                                                         command=lambda :button_click(8)).grid(row=2, column=1)
button9 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='9', \
                                                         command=lambda :button_click(9)).grid(row=2, column=2)
button_add = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='+', \
                                                         command=lambda :button_click('+')).grid(row=2, column=3)
button4 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='4', \
                                                         command=lambda :button_click(4)).grid(row=3, column=0)
button5 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='5', \
                                                         command=lambda :button_click(5)).grid(row=3, column=1)
button6 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='6', \
                                                         command=lambda :button_click(6)).grid(row=3, column=2)
button_subtraction= Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='-', \
                                                         command=lambda :button_click('-')).grid(row=3, column=3)
button1 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='1', \
                                                         command=lambda :button_click(1)).grid(row=4, column=0)
button2 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='2', \
                                                         command=lambda :button_click(2)).grid(row=4, column=1)
button3 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='3', \
                                                         command=lambda :button_click(3)).grid(row=4, column=2)
button_multiply = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='*', \
                                                         command=lambda :button_click('*')).grid(row=4, column=3)
button0 = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='0', \
                                                         command=lambda :button_click(0)).grid(row=5, column=0)
button_clear = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='C', \
                                                         command =button_clearDisplay).grid(row=5, column=1)
button_equal = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='=', \
                                                         command=button_equalInput).grid(row=5, column=2)
button_divide = Button(f2, padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='/', \
                                                         command=lambda :button_click('/')).grid(row=5, column=3)
#variables restaurente information
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charger = StringVar()
Chicken = StringVar()
Cheese = StringVar()
Tax = StringVar()
Cost = StringVar()
Drinks = StringVar()
lblReverance = Label(f1,font=('arial', 16 ,'bold'), text='Reverance', bd=16, anchor='w')
lblReverance.grid(row=0, column=0)
txtReverance=Entry(f1,font=('arial', 16 ,'bold'), textvariable=rand, bd=10, insertwidth=4,
                    bg='powder blue', justify='right')
txtReverance.grid(row=0, column=1)
lblFries = Label(f1,font=('arial', 16 ,'bold'), text='Large Fries', bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries=Entry(f1,font=('arial', 16 ,'bold'), textvariable=Fries, bd=10, insertwidth=4,
                    bg='powder blue', justify='right')
txtFries.grid(row=1, column=1)
lblBurger = Label(f1,font=('arial', 16 ,'bold'), text='Burger Meal', bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger=Entry(f1,font=('arial', 16 ,'bold'), textvariable=Burger, bd=10, insertwidth=4,
                    bg='powder blue', justify='right')
txtBurger.grid(row=2, column=1)

lblFilet = Label(f1,font=('arial', 16 ,'bold'), text='Filet_o_Meal', bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet=Entry(f1,font=('arial', 16 ,'bold'), textvariable=Filet, bd=10, insertwidth=4,
                    bg='powder blue', justify='right')
txtFilet.grid(row=3, column=1)
lblChicken = Label(f1,font=('arial', 16 ,'bold'), text='Chicken Meal', bd=16, anchor='w')
lblChicken .grid(row=4, column=0)
txtChicken=Entry(f1,font=('arial', 16 ,'bold'), textvariable=Chicken, bd=10, insertwidth=4,
                    bg='powder blue', justify='right')
txtChicken.grid(row=4, column=1)
lblCheese = Label(f1,font=('arial', 16 ,'bold'), text='Cheese Meal', bd=16, anchor='w')
lblCheese .grid(row=5, column=0)
txtCheese=Entry(f1,font=('arial', 16 ,'bold'), textvariable=Cheese, bd=10, insertwidth=4,
                    bg='powder blue', justify='right')
txtCheese.grid(row=5, column=1)
#another line informatin
lblDrinks = Label(f1,font=('arial', 16 ,'bold'), text='Drinks', bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks =Entry(f1,font=('arial', 16 ,'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                    bg='#fff', justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1,font=('arial', 16 ,'bold'), text='Cost Of Meal', bd=16, anchor='w')
lblCost  .grid(row=1, column=2)
txtCost  =Entry(f1,font=('arial', 16 ,'bold'), textvariable=Cost, bd=10, insertwidth=4,
                    bg='#fff', justify='right')
txtCost .grid(row=1, column=3)

lblService_charger = Label(f1,font=('arial', 16 ,'bold'), text='Service_charger', bd=16, anchor='w')
lblService_charger  .grid(row=2, column=2)
txtService_charger  =Entry(f1,font=('arial', 16 ,'bold'), textvariable=Service_Charger, bd=10, insertwidth=4,
                    bg='#FFF', justify='right')
txtService_charger .grid(row=2, column=3)

lblTax = Label(f1,font=('arial', 16 ,'bold'), text='State Tax', bd=16, anchor='w')
lblTax  .grid(row=3, column=2)
txtTax  =Entry(f1,font=('arial', 16 ,'bold'), textvariable=Tax, bd=10, insertwidth=4,
                    bg='#fff', justify='right')
txtTax .grid(row=3, column=3)

lblSubTotal = Label(f1,font=('arial', 16 ,'bold'), text='Sub Total', bd=16, anchor='w')
lblSubTotal  .grid(row=4, column=2)
txtSubTotal  =Entry(f1,font=('arial', 16 ,'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                    bg='#fff', justify='right')
txtSubTotal .grid(row=4, column=3)

lblTotal = Label(f1,font=('arial', 16 ,'bold'), text='Total Cost', bd=16, anchor='w')
lblTotal  .grid(row=5, column=2)
txtTotal =Entry(f1,font=('arial', 16 ,'bold'), textvariable=Total, bd=10, insertwidth=4,
                    bg='#fff', justify='right')
txtTotal.grid(row=5, column=3)

#Buttons
buttonTotal= Button(f1, padx=16, pady=8, bd=16, fg='black',font=('arial', 16 ,'bold'),width=10,
                    text='Total', bg='powder blue', command=Ref).grid(row=7, column=1)

buttonReset= Button(f1, padx=16, pady=8, bd=16, fg='black',font=('arial', 16 ,'bold'),width=10,
                    text='Reset', bg='powder blue', command=Reset).grid(row=7, column=2)

buttonQuit= Button(f1, padx=16, pady=8, bd=16, fg='black',font=('arial', 16 ,'bold'),width=10,
                    text='Exit', bg='powder blue', command=Exit).grid(row=7, column=3)

root.mainloop()