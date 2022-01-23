import tkinter
from tkinter import *
import os

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self)

        #creating some more basic options such as:
        self.master = master 
        self.master.resizable(width=True, height=True) 
        self.master.geometry('{}x{}'.format(700, 400) )
        self.master.title('Input Text')
        self.master.config(bg="white")
        
        self.txtInput = StringVar()
    
        self.txtInput = Label(self.master,text='Input Text', font=("Helvetica", 16), fg="black", bg="lightgray")
        self.txtInput.grid(row=0, column=0, padx=(30, 0), pady=(30,0) )

        self.txtInput= Entry(self.master, text=self.txtInput, font= ("Helvetica", 16), fg="black", bg="lightblue")
        self.txtInput.grid(row=0, column=1, padx=(30, 0), pady=(30,0) )

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(30, 0), pady=(30,0) , sticky=NE)

    def submit(self): 
        txt = self.txtInput.get()
        print(txt)
        f = open("htmlPy.html", "w")
        f.write("""
                <html>
                    <body>
                        <h1>
                        {}
                        </h1>
                    </body>
                </html>
        """.format(txt))
        f.close()

        os.system(r"start C:\Users\Diego\Documents\GitHub\Python_Projects\challenges\htmlPy.html")

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
            
    
    
    



