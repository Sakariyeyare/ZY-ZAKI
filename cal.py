from tkinter import *
root=Tk()
root.title("Calculator")
#functions
text_input = StringVar()
operator=''
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
#buttons
text_display = Entry(font=("arial", 20, "bold"), textvariable=text_input, bg='powder blue', bd=30, insertwidth=4,
                      justify='right')
text_display.grid(columnspan=4)
button7 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='7', \
                                                         command=lambda :button_click(7)).grid(row=2, column=0)
button8 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='8', \
                                                         command=lambda :button_click(8)).grid(row=2, column=1)
button9 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='9', \
                                                         command=lambda :button_click(9)).grid(row=2, column=2)
button_add = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='+', \
                                                         command=lambda :button_click('+')).grid(row=2, column=3)
button4 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='4', \
                                                         command=lambda :button_click(4)).grid(row=3, column=0)
button5 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='5', \
                                                         command=lambda :button_click(5)).grid(row=3, column=1)
button6 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='6', \
                                                         command=lambda :button_click(6)).grid(row=3, column=2)
button_subtraction= Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='-', \
                                                         command=lambda :button_click('-')).grid(row=3, column=3)
button1 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='1', \
                                                         command=lambda :button_click(1)).grid(row=4, column=0)
button2 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='2', \
                                                         command=lambda :button_click(2)).grid(row=4, column=1)
button3 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='3', \
                                                         command=lambda :button_click(3)).grid(row=4, column=2)
button_multiply = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='*', \
                                                         command=lambda :button_click('*')).grid(row=4, column=3)
button0 = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='0', \
                                                         command=lambda :button_click(0)).grid(row=5, column=0)
button_clear = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='C', \
                                                         command =button_clearDisplay).grid(row=5, column=1)
button_equal = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='=', \
                                                         command=button_equalInput).grid(row=5, column=2)

button_divide = Button( padx=16, pady=16, bd=8, bg='powder blue', fg='black', font=('arial',20,'bold'), text='/', \
                                                         command=lambda :button_click('/')).grid(row=5, column=3)
root.mainloop()