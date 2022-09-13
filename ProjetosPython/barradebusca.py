from tkinter import *
import webbrowser

win = Tk()
win.title('Barra de Busca')

def search():
    url = Entry.get()
    webbrowser.open(url)
    
label1 = Label(win, text='Insira a URL aqui:', font=('arial', 10, 'bold'))
label1.grid(row=0, column=0)

entry = Entry(win, width=30)
entry.grid(row=0, column=1)

button = Button(win, text='Buscar', command=search)
button.grid(row=1, column=0, columnspan=2, pady=10)

win.mainloop()