from tkinter import *
root=Tk()
def c():
    print("haii")
b1=Button(root,text="submit",command=c)
b1.pack()
b2=Button(root,text="quit",command=quit)
b2.pack
root.mainloop()