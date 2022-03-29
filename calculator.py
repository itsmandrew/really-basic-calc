from tkinter import *
import tkinter.font as font


def init():
    root = Tk()
    root.geometry('312x324')
    root.resizable(0, 0) #prevents resizing
    root.title('Calculator')
    
    myFont = font.Font(family='Times New Roman', font=10, weight='bold')

    canvas = Canvas(root, bg = 'white')
    canvas.pack()
    #frame for the string???
    frame = Frame(canvas, width = 312, height = 65, bg = 'dark grey', highlightbackground="black", highlightthickness=5)
    frame.pack(side=TOP)

    #frame for the buttons
    button_frame = Frame(canvas, width = 312, height = 274, bg = 'black', highlightbackground="black", highlightthickness=3)
    button_frame.pack()

    #row 0
    clear_button = Button(button_frame, text='AC', bg= 'darkblue', fg='white', pady=5, padx = 25)
    clear_button.grid(row = 0, column =0, padx = 2.5, pady=(3, 10))

    negate = Button(button_frame, text = '+/-', bg= 'darkblue', fg = 'white', pady=5, padx=25)
    negate.grid(row = 0, column= 1, padx=2.5, pady=(3, 10))

    percentage = Button(button_frame, text='%', bg = 'darkblue', fg= 'white', pady=5, padx = 25)
    percentage.grid(row=0, column= 2, padx=2.5, pady=(3, 10))

    divide = Button(button_frame, text = '/', bg = 'orange', fg= 'white', pady=5, padx = 25)
    divide.grid(row=0, column=3, padx=2, pady=(3, 10))
    
    #end of row0

    #row 1
    number_7 = Button(button_frame, text='7', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_7.grid(row=1, column=0, padx=0, pady=(3, 10))

    number_8 = Button(button_frame, text='8', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_8.grid(row=1, column=1, padx=0, pady=(3, 10))

    number_9 = Button(button_frame, text='9', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_9.grid(row=1, column=2, padx=0, pady=(3, 10))

    multiply = Button(button_frame, text='X', bg = 'orange', fg= 'white', pady=5, padx = 20)
    multiply.grid(row=1, column=3, padx=(2, 0), pady=(3, 10))
    #end of row 1

    #row 2
    number_4 = Button(button_frame, text='4', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_4.grid(row=2, column=0, padx=0, pady=(3, 10))

    number_5 = Button(button_frame, text='5', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_5.grid(row=2, column=1, padx=0, pady=(3, 10))

    number_6 = Button(button_frame, text='6', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_6.grid(row=2, column=2, padx=0, pady=(3, 10))

    subtract = Button(button_frame, text='-', bg = 'orange', fg= 'white', pady=5, padx = 22)
    subtract.grid(row=2, column=3, padx=(2, 0), pady=(2, 10))
    #end of row 2

    #row 2
    number_1 = Button(button_frame, text='1', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_1.grid(row=3, column=0, padx=0, pady=(3, 10))

    number_2 = Button(button_frame, text='2', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_2.grid(row=3, column=1, padx=0, pady=(3, 10))

    number_3 = Button(button_frame, text='3', bg = 'darkgrey', fg= 'white', pady=5, padx = 28, font=('bold'))
    number_3.grid(row=3, column=2, padx=0, pady=(3, 10))

    add = Button(button_frame, text='+', bg = 'orange', fg= 'white', pady=5, padx = 22)
    add.grid(row=3, column=3, padx=(2, 0), pady=(2, 10))
    #end of row 2


    root.mainloop()
if __name__ == '__main__':
    expression = ''
    init()
