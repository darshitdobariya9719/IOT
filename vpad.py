import tkinter as tk
from tkinter import ttk
from tkinter import filedialog , font ,messagebox
import os

win=tk.Tk()
win.title('vpad')
photo=tk.PhotoImage(file='C:\pythonprogram\mylogo1.png')
win.iconphoto(False,photo)
win.geometry('1200x800')
toolbar=ttk.Label(win)
#toolbar.grid(row=1,column=0)
toolbar.pack(side=tk.TOP,fill=tk.X)

#toolbar.pack(side=tk.TOP,fill=tk.X)
fontfami=tk.font.families()
fontr=tk.StringVar()
#print(fontfami)
fontf=ttk.Combobox(toolbar,width=35,textvariable=fontr,state='readonly')
fontf['values']=fontfami
fontf.current(fontfami.index('Arial'))
fontf.grid(row=0,column=0)
#fontf.bind("<<ComboboxSelected>>",qwe)
fontsr=tk.IntVar()
fonts=ttk.Combobox(toolbar,textvariable=fontsr,state='readonly')
fonts['values']=tuple(range(8,200,2))
fonts.current(1)
fonts.grid(row=0,column=1)
#fonts.bind("<<ComboboxSelected>>",qwe)

texteditor=tk.Text(win)
texteditor.config(wrap='word',relief=tk.FLAT)
texteditor.pack(fill=tk.BOTH,expand=True)
curuntff='Arial'
curuntfs=12
def fof(event=None):
    global curuntff
    curuntff=fontr.get()
    texteditor.config(font=(curuntff,curuntfs))
def fos(event=None):
    global curuntfs
    curuntfs=fontsr.get()
    texteditor.config(font=(curuntff,curuntfs))    
fontf.bind("<<ComboboxSelected>>",fof)
fonts.bind("<<ComboboxSelected>>",fos)


url=''
def funknew(event=None):
    global url
    url=''
    texteditor.delete(1.0,tk.END)
    
def funkopen(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='select file',filetypes=(('text file','*.txt'),('all files','*.*')))
    with open(url,'r') as fo:

        texteditor.delete(1.0,tk.END)
        texteditor.insert(1.0,fo.read())
    
def funksave(event=None):
    global url
    if url:
        content=str(texteditor.get(1.0,tk.END))
        with open(url,'w') as fs:
            fs.write(content)
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text file','*.txt'),('All files','*.*')))       
        content2=str(texteditor.get(1.0,tk.END)) 
        url.write(content2)
        url.close()
def funksave_As(event=None):
    global url
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text file','*.txt'),('All files','*.*')))       
    content2=str(texteditor.get(1.0,tk.END)) 
    url.write(content2)
    url.close()
def funkExit(event=None):
    global url
    mbox=messagebox.askyesnocancel('Warning','do you want to save file?')
    if mbox is True:
        if url:
            content=str(texteditor.get(1.0,tk.END))
            with open(url,'w') as fs:
                fs.write(content)
                win.destroy()
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text file','*.txt'),('All files','*.*')))       
            content2=str(texteditor.get(1.0,tk.END)) 
            url.write(content2)
            url.close()
            win.destroy()

main_menu=tk.Menu(win)
file=tk.Menu(main_menu ,tearoff=False)
file.add_command(label='new',command=funknew,accelerator='Ctrl+N')
file.add_command(label='open',command=funkopen,accelerator='Ctrl+O')
file.add_command(label='Save',command=funksave,accelerator='Ctrl+S')
file.add_command(label='Save As',command=funksave_As,accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',command=funkExit,accelerator='Ctrl+Q')

text1=''
def copyfun(event=None):
    global text1
    text1=str(texteditor.event_generate("<Control c>"))
    text1=str(texteditor.get(1.0,tk.END))
def pastefun(event=None):
    global text1
    text1=str(texteditor.event_generate("<Control v>"))
    texteditor.insert(1.0,text1)    
def cutfun(event=None):
    global text1
    text1=str(texteditor.get(1.0,tk.END))   
    texteditor.delete(1.0,tk.END) 
def clearall(event=None):
        texteditor.delete(1.0,tk.END)

edit=tk.Menu(main_menu,tearoff=False)
edit.add_command(label='copy',command=copyfun,accelerator='Ctrl+C')
edit.add_command(label='Paste',command=pastefun,accelerator='Ctrl+V')
edit.add_command(label='Cut',command=cutfun,accelerator='Ctrl+X')
edit.add_command(label='Clear All',command=clearall,accelerator='Ctrl+Alt+X')
edit.add_command(label='Find',accelerator='Ctrl+F')
view=tk.Menu(main_menu,tearoff=False)

def ck1():
    ck=check.get()
    if ck:
        texteditor.pack_forget()
        toolbar.pack(side=tk.TOP,fill=tk.X)
        texteditor.pack(fill=tk.BOTH,expand=True)
    else:
        toolbar.pack_forget()
        

check=tk.BooleanVar()
view.add_checkbutton(label='Tool Bar',variable=check,command=ck1)
view.add_checkbutton(label='Status Bar')
color=tk.Menu(main_menu,tearoff=False)
them=tk.StringVar()
colordict={
    'Light Default':('#ffffff','#000000'),
    'blue':('#0000ff','#ffff00'),
    'Dark':('#000000','#ffffff'),
    'red':('#ff0000','#00ff00')
}
def change():
    var=them.get()
    cr=colordict[var]
    bg,fog=cr[0],cr[1]
    texteditor.config(background=bg,fg=fog)

count=0
for i in colordict:
    color.add_radiobutton(label=i,variable=them,command=change)
    count += 1
    

#texteditor.config(background=them(0),fg=them(1))
main_menu.add_cascade(label='file',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='color_theam',menu=color)
win.config(menu=main_menu)
win.mainloop() 