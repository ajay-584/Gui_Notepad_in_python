from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFiile():
    global file
    root.title("Untitle-Notepad")
    file = None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file== None:
        file = asksaveasfilename(initialfile="Untitle.text",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #save as a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            # print("files save")
    else:
        # save as the file
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Note_Pad","Notepas By Ajay Kumar")


if __name__=='__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x788")
    root.wm_iconbitmap((""))

    # Add TextArea
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH,expand=True)

    # Creating Menu
    MenuBar = Menu(root)
    # File menu start
    FileMenu = Menu(MenuBar,tearoff=0)
    # To open new file
    FileMenu.add_command(label="New",command=newFiile)

    #To open already exiting file
    FileMenu.add_command(label="Open",command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #File menu ends

    #Edit menu start
    EditMenu = Menu(MenuBar,tearoff=0)
    # to give a feature of cut,copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu = EditMenu)
    # Edit menu ends

    # Help menu start
    HelpMenu = Menu(MenuBar,tearoff = 0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    # Help mneu ends
    root.config(menu=MenuBar)

    # Adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()