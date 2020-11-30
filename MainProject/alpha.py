from tkinter import *
root = Tk()
root.title("the mashup")
root.geometry("350x550")
work_frm = Frame(root, bg="silver")
work_frm.place(relx=0, rely=0, relwidth=1, relheight=1)
def new():
    global work_frm
    work_frm.destroy()
    work_frm = Frame(root, bg="silver")
    work_frm.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
