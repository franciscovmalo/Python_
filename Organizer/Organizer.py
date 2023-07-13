import os
import shutil
from tkinter import *

path = 'D:\Test'
list = os.listdir(path)

def Org():
    for file in list:
        fname, ext = os.path.splitext(file)
        print(fname)
        ext = ext[1:]
        ext = ext
        
        if ext == '':
            continue
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file, path +'/'+ext+'/'+file)
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file, path +'/'+ext+'/'+file)

screen = Tk()

screen.title('Organizer')
text = Label(screen, text='Directory path')
text.grid(column=0, row=3)
#Label(screen, textvariable='', anchor='e', bg='black', fg='red', font=('Digital-7',47)).grid(row=1, columnspan=4, sticky='ew', padx=4, pady=2)

bt = Button(screen, text='Organizar', command=Org)


bt.grid(column=3, row=5)

screen.mainloop()