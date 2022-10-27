import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('1000x500')
root.title('TongueTwister')
style = ttk.Style(root)

# create a notebook
notebook = ttk.Notebook(root)
style.theme_use('classic')
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=1000, height=580)
frame2 = ttk.Frame(notebook, width=1000, height=580)
frame3 = ttk.Frame(notebook, width=1000, height=580)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

inputtxt = tk.Text(frame1,
                   height=2,
                   width=50)

inputtxt.place(x=10,y=20)

# Button Creation
printButton = tk.Button(frame1, text="Parse")
printButton.place(x= 420, y = 22)

# Label Creation
lbl = tk.Label(frame1, text="Parsing Page")
lbl.pack()
# add frames to notebook

notebook.add(frame1, text='Sentence Parsing')
notebook.add(frame2, text='Translating')
notebook.add(frame3, text='Settings')




root.mainloop()