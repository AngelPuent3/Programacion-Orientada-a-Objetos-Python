from tkinter import *
#import le modulo parser de python





root = Tk()
root.title

display= Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

i=0

def getNumbers(n):
    global i
    display.insert(i,n)
    i+=1


def getOperation(operator):
    global i
    len(operator)
    operatorlen=len(operator)
    display.insert(i,operator)
    i+=operatorlen

def getClear():
    display.delete(0,END)

def undo():
    displayState = display.get()
    if len(displayState):
        displayNewState = displayState[:-1]
        getClear()
        display.insert(0,displayNewState)
    else:
        getClear()
        display.insert(0,"Error")


def calculate():
    displayState = display.get()
    try:
        mathResult = compile(displayState,"app.py","eval")
        result = eval(mathResult)
        getClear()
        display.insert(0,result)
    except Exception:
        getClear()
        display.insert(0,"Error")

Button(root, text=1, command=lambda:getNumbers(1)).grid(row=2,column=0,sticky=W+E)
Button(root, text=2,command=lambda:getNumbers(2)).grid(row=2,column=1,sticky=W+E)
Button(root, text=3,command=lambda:getNumbers(3)).grid(row=2,column=2,sticky=W+E)
Button(root, text=4,command=lambda:getNumbers(4)).grid(row=3,column=0,sticky=W+E)
Button(root, text=5,command=lambda:getNumbers(5)).grid(row=3,column=1,sticky=W+E)
Button(root, text=6,command=lambda:getNumbers(6)).grid(row=3,column=2,sticky=W+E)
Button(root, text=7,command=lambda:getNumbers(7)).grid(row=4,column=0,sticky=W+E)
Button(root, text=8,command=lambda:getNumbers(8)).grid(row=4,column=1,sticky=W+E)
Button(root, text=9,command=lambda:getNumbers(9)).grid(row=4,column=2,sticky=W+E)

Button(root, text="AC",command=lambda:getClear()).grid(row=5,column=0,sticky=W+E)
Button(root, text="0",command=lambda:getNumbers(0)).grid(row=5,column=1,sticky=W+E)
Button(root, text="%",command=lambda:getOperation("%")).grid(row=5,column=2,sticky=W+E)

Button(root, text="+",command=lambda:getOperation("+")).grid(row=2,column=3,sticky=W+E)
Button(root, text="-",command=lambda:getOperation("-")).grid(row=3,column=3,sticky=W+E)
Button(root, text="*",command=lambda:getOperation("*")).grid(row=4,column=3,sticky=W+E)
Button(root, text="/",command=lambda:getOperation("/")).grid(row=5,column=3,sticky=W+E)

Button(root, text="⇦",command=lambda:undo()).grid(row=2,column=4,sticky=W+E,columnspan=2)
Button(root, text="exp",command=lambda:getOperation("**")).grid(row=3,column=4,sticky=W+E)
Button(root, text="*2",command=lambda:getOperation("**2")).grid(row=3,column=5,sticky=W+E)
Button(root, text="(",command=lambda:getOperation("(")).grid(row=4,column=4,sticky=W+E)
Button(root, text=")",command=lambda:getOperation(")")).grid(row=4,column=5,sticky=W+E)
Button(root, text="=",command=lambda:calculate()).grid(row=5,column=4,sticky=W+E,columnspan=2)




root.mainloop()