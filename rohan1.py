from tkinter import *
window = Tk()
def s1():
    print(listbox.get(listbox.curselection()))

listbox = Listbox(window)
listbox.pack()
button = Button(window,text="submit",command=s1)
button.pack()

listbox.insert(1,"rohan")
listbox.insert(2,"rohan1")
listbox.insert(3,"rohan2")
listbox.insert(4,"rohan3")

window.mainloop()