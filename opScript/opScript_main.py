import tkinter
from tkinter import *
import opScript_functions as ops

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self)

        self.master = master 
        self.master.resizable(width=True, height=True) 
        self.master.geometry('{}x{}'.format(700, 400) )
        self.master.title('AB')
        self.master.config(bg="darkgray")
        
        self.sourcePath = StringVar()
        self.destPath = StringVar()

        #entry 1 that displays source path and it's label
        self.sourcePathlbl = Label(self.master,text='Source Path', font=("Helvetica", 16), fg="black", bg="lightgray")
        self.sourcePathlbl.grid(row=0, column=0, padx=(30, 0), pady=(30,0) )

        self.sourcePath = Entry(self.master, text=self.sourcePath,width=30, font= ("Helvetica", 16), fg="black", bg="white")
        self.sourcePath.grid(row=0, column=1, padx=(30, 0), pady=(30,0) )

        #entry 2 that displays dest path and it's label
        self.destPath = Entry(self.master, text=self.destPath, width=30, font= ("Helvetica", 16), fg="black", bg="white")
        self.destPath.grid(row=1, column=1, padx=(30, 0), pady=(30,0) )

        self.destPathlbl = Label(self.master,text='Destination Path', font=("Helvetica", 16), fg="black", bg="lightgray")
        self.destPathlbl.grid(row=1, column=0, padx=(30, 0), pady=(30,0) )

        #buttons
        self.btnSelect = Button(self.master, text="Select Source...", width=15, height=2, command=lambda:ops.chooseSource(self))
        self.btnSelect.grid(row=2, column=1,padx=(0,165), pady=(30,0), sticky=NE, )

        self.btnSelectD = Button(self.master, text="Select Destination...", width=15, height=2, command=lambda: ops.chooseDest(self))
        self.btnSelectD.grid(row=2, column=1, padx=(0,30), pady=(30, 0), sticky=NE)

        self.btnhold= Button(self.master, text="Transfer", width=15, height=3, command=lambda: ops.MoveFiles(self))
        self.btnhold.grid(row=3, column=1, padx=(0,30), pady=(30, 0))
       


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
