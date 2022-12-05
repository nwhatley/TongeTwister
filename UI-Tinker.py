import tkinter as tk
from tkinter import ttk
from Parser_test import *


# root window
root = tk.Tk()
root.geometry('1000x500')
root.title('TongueTwister')
style = ttk.Style(root)

sentence_var = tk.StringVar()
result_var = tk.StringVar()

def submit():
    """test for now"""
    sentence = sentence_var.get()
    #print(sentence)
    test = parser(sentence, 'fr')

    word = info_reader(test)
    #print(word)
    output = print_nice(word)

    #print(output)
    result_var.set(output)
    print(result_generator(word))
    result(result_generator(word))
    textWindow.insert(tk.INSERT, result_var.get())

def result(resultlist):
    """Does a thing"""

    x = 0
    for item in resultlist:

        word = tk.Label(resultFrame, text=item[0])
        if len(item) == 2:

            if item[1] == "":
                word.configure(foreground='purple')
            else:
                word.configure(foreground=item[1])
        else:
            word.configure(foreground='purple')

        word.grid(column=x, row= 0, padx=10, pady= 10)
        x = x+1


menubar = tk.Menu(root)
# create a notebook
notebook = ttk.Notebook(root)
style.theme_use('classic')
notebook.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# Menu Bar

menubar = tk.Menu(root)

# Adding File Menu and commands
file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='Import', command=None)
file.add_command(label='...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

# Adding Edit Menu and commands
edit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)


language = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Change Language', menu=language)
language.add_command(label='English to French', command=None)
language.add_command(label='English to Spanish', command=None)
language.add_command(label='...', command=None)
language.add_command(label='...', command=None)
language.add_separator()
language.add_command(label='Default Language', command=None)
language.add_command(label='...', command=None)


# Adding Help Menu
help_ = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

# create frames
frame1 = ttk.Frame(notebook, width=1000, height=580)
frame2 = ttk.Frame(notebook, width=1000, height=580)
frame3 = ttk.Frame(notebook, width=1000, height=580)
frame4 = ttk.Frame(notebook, width=1000, height=580)


frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


# Test Window Right Side

# Testing stuff with Frames
entryFrame = ttk.LabelFrame(frame1, text="Sentence Entry")
entryFrame.place(x= 10, y = 20)

resultFrame = ttk.LabelFrame(frame1, text="Result")
resultFrame.place(x= 10, y = 250)

rawFrame = ttk.LabelFrame(frame1, text="Annotations")
rawFrame.place(x= 550, y = 20)

moreFrame = ttk.LabelFrame(frame1, text ="More Options")
moreFrame.place(x= 650, y = 400)

#resultLabel = tk.Label(resultFrame, text="~~~~~~Placeholder~~~~~~")
#resultLabel.grid(column=0, row= 0, padx=50, pady= 20)

textWindow = tk.Text(rawFrame, height = 10, width = 53)
textWindow.grid(column=0, row=0, padx=8, pady=8)

textWindow.insert(tk.INSERT, result_var.get())

frameEntry = tk.Entry(entryFrame, textvariable = sentence_var, width=65)
frameEntry.grid(column=0, row=0, padx=20, pady= 18)

goButton = tk.Button(entryFrame, text="Go", command= submit,  width=8)
goButton.grid(column=3, row=0, padx= 10, pady = 10)

translateButton = tk.Button(moreFrame, text="Translate This", width=10)
translateButton.grid(column=1, row=0, padx= 10, pady = 10)

saveButton = tk.Button(moreFrame, text="Save This", width=8)
saveButton.grid(column=2, row=0, padx= 10, pady = 10)
# Label Creation
# Header
lbl = tk.Label(frame1, text="Parsing Page")
lbl.pack()


# add frames to notebook

notebook.add(frame1, text='Sentence Parsing')
notebook.add(frame2, text='Translating')
notebook.add(frame3, text='Vocab')

notebook.add(frame4, text='Settings')



root.config(menu = menubar)
root.mainloop()