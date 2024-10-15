import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    text['text'] += ' ' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('391x175')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', width=55, height=5, background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=5, background='silver',
                               foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5)
main_menu = tkinter.Menu()
main_menu.add_cascade(label="File")
window.config(menu=main_menu)
window.mainloop()
