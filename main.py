from tkinter import *
import os
from tkinter import filedialog, colorchooser, font 
from tkinter.messagebox import *
from tkinter.filedialog import *
import textwrap

#function to change font color
def change_color():
     color = colorchooser.askcolor(title="Choose a Color")
     textArea.config(fg=color[1])

#function to change font
def change_font(*args):
     textArea.config(font=(font_name.get(), font_size_change.get()))

#function to create a new file
def new_file():
     #default 
     win.title("Untitled")
     #deletes all the content
     textArea.delete(1.0,END)

#function to open a file
def open_file():
     #opening a file name
     file = askopenfilename(defaultextension=".txt", file=[("All Files","*.*"), 
                                                           ("Text Documents","*.txt")])
     try:
          #fetching the data of the file into the text editor
          win.title(os.path.basename(file))
          textArea.delete(1.0,END)
          file = open(file, "r")
          textArea.insert(1.0,file.read())
     except Exception:
          print("Could not read the file: " + file)
     finally:
          file.close()

#function to save a file to
def save_file():
     file = win.title()
     if(file=="untitled.txt"):
          save_as_file()
     else:
          try:
               #write the contents of the text editor into the file
               win.title(os.path.basename(file))
               file = open(file,"w")
               file.write(textArea.get(1.0,END))
          except Exception:
               print("Couldn't save file")
          finally:
               file.close()
               
#function to save as a file
def save_as_file():
     file = filedialog.asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", 
                                         filetypes=[("All Files","*.*"),
                                                    ("Text Documents","*.txt")])
     if file is None:
          return
     else:
          try:
               #write the contents of the text editor into the file
               win.title(os.path.basename(file))
               file = open(file,"w")
               file.write(textArea.get(1.0,END))
          except Exception:
               print("The file couldn't be saved")
          finally:
               file.close()     

#function to cut using Ctrl+X
def cut():
     textArea.event_generate("<<Cut>>")

#function to copy using Ctrl+C
def copy():
     textArea.event_generate("<<Copy>>")

#function to paste using Ctrl+V
def paste():
     textArea.event_generate("<<Paste>>")

#About page 
def about():
     showinfo("This is created by Praveen Rao V P. Check out my GitHub Page @PraveenRaoVP for some code of my projects")

#function to quit the app
def quit():
     win.destroy()



#Creating a window
win = Tk()
win.title("Roy Text Editor")

#initially before saving the file 
file = None 

#dimensions of the window
winWidth = 500
winHeight = 500

#The width of the native device of the screen
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()

#x and y for the calculation of the window size
x = int((screenWidth/2) - (winWidth/2))
y = int((screenHeight/2) - (winHeight/2))

#Setting the geometry of the window through the above calculated values
win.geometry(f"{winWidth}x{winHeight}+{x}+{y}")

#Default font and size
font_name = StringVar(win)
font_name.set("Arial")

font_size = StringVar(win)
font_size.set("20")

#Creating area to type text
textArea = Text(win, font=(font_name.get(), font_size.get()))

#scroll bar for the editor
scrollBar = Scrollbar(textArea)
scrollBar.pack(side=RIGHT, fill=Y)
textArea.config(yscrollcommand=scrollBar.set)

win.grid_rowconfigure(0,weight=1)
win.grid_columnconfigure(0,weight=1)
textArea.grid(sticky=N+E+S+W)

#Creating a Frame
frame = Frame(win)
frame.grid()

#changing the font color
colorButton = Button(frame, text="Change Font Color", command = change_color)
colorButton.grid(row=0,column=0)

#font change
fontChangeButton = OptionMenu(frame, font_name,*font.families(), command= change_font)
fontChangeButton.grid(row=0,column=1)

#font size change
font_size_change = Spinbox(frame, from_=1, to=52, textvariable=font_size, command=change_font)
font_size_change.grid(row=0,column=2)

#menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)
#file menu dropdown cascade, New, open, save, save as, exit
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

#edit menu dropdown cascade, cut, copy, paste
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

#help menu about
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", command=help_menu)
help_menu.add_command(label="About", command=about)

#mainloop
win.mainloop()










