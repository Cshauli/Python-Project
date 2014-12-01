from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="blue")




































print 'Hello, please enter your name!'
userInput = raw_input()
print 'Welcome to Geek Battle' + userInput
class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        drawpad.pack(side=RIGHT)
app = myApp(root)
root.mainloop()