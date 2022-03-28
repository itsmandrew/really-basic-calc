from tkinter import *



def init():
    root = Tk()
    root.geometry('312x324')
    root.resizable(0, 0) #prevents resizing
    root.title('Calculator')

    frame = Frame(root, width = 312, height = 50, bg = 'dark grey', highlightbackground="white", highlightthickness=3)
    frame.pack(side=TOP)

    button_frame = Frame(width = 312, height = 274, bg = 'black', highlightbackground="white", highlightthickness=3)
    button_frame.pack()


    root.mainloop()
if __name__ == '__main__':
    expression = ''
    init()