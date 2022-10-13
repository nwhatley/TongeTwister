from tkinter import *

def display():
    if(x.get()==1):
        print("Huh")
    else:
        print("okay")

window = Tk()
window.geometry("1000x500")
window.title("TongueTwister")

roni = PhotoImage(file='roni.png')
window.iconphoto(True,roni)
window.config(background="grey")

x = IntVar()
grammar_button = Checkbutton(window,
                             text="Grammar",
                             variable=x,
                             onvalue=1,
                             offvalue=0,
                             command=display,
                             font=('Comic Sans', 20),
                             fg='black',
                             bg='grey',
                             activebackground='grey',
                             padx=5000,
                             pady=10000)


grammar_button.pack()
window.mainloop()

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


