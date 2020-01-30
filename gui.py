#!/usr/bin/env python

import tkinter
from tkinter import filedialog
import os
import datetime
import calendar
import expenses

gettime = datetime.datetime.now() #getting times-dates for filenames
month_now = calendar.month_abbr[gettime.month]
timestamp = str(str(gettime.day)+"-"+str(month_now)+"-"+str(gettime.year))
out_filename = str("Spendings "+timestamp+".csv")

guiform = tkinter.Tk()
guiform.geometry("425x195")
guiform.title("Spendings accounting")

dir = os.getcwd()


def browsefile(field):
    filename = filedialog.askopenfilename()
    field.delete(0, 'end')
    field.insert(0, filename)


def browsedir(field):
    dirname = filedialog.askdirectory()
    field.delete(0, 'end')
    field.insert(0, dirname)


chkbox1 = tkinter.IntVar()
chkbox3 = tkinter.IntVar()

alfainput = tkinter.Entry(guiform, width=40)
tinkinput = tkinter.Entry(guiform, width=40)

alfainput.insert(0, (dir+"\\alfa.csv"))
tinkinput.insert(0, (dir+"\\tinkoff.csv"))

alfainput.config(state='disable')
tinkinput.config(state='disable')


def enable_input(field, button, state):
    box_state = state.get()
    boxes_state = chkbox1.get()+chkbox3.get()

    if box_state:
        field.config(state='normal')
        button.config(state='normal')
    else:
        field.config(state='disable')
        button.config(state='disable')

    if boxes_state:
        processbutton.config(state='normal')
    else:
        processbutton.config(state='disable')


def enb_alfa(): enable_input(alfainput, alfabrowsebutton, chkbox1)
def enb_tink(): enable_input(tinkinput, tinkbrowsebutton, chkbox3)

mainlabel = tkinter.Label(guiform, text="Check the reports you need to process").grid(row=0, column=1)
outlabel_1 = tkinter.Label(guiform, text=" ").grid(row=6, column=1)
outlabel_2 = tkinter.Label(guiform, text=" ").grid(row=7, column=1)
outlabel_3 = tkinter.Label(guiform, text=" ").grid(row=8, column=1)
outlabel_4 = tkinter.Label(guiform, text=" ").grid(row=9, column=1)

tkinter.Checkbutton(guiform, text="Alfabank", variable=chkbox1, command=enb_alfa).grid(sticky="W", row=1)
tkinter.Checkbutton(guiform, text="Tinkoff", variable=chkbox3, command=enb_tink).grid(sticky="W", row=3)

def alfabrowse(): browsefile(alfainput)
def tinkbrowse(): browsefile(tinkinput)

def runmain():
    alfa = chkbox1.get()
    tink = chkbox3.get()

    alfapath = alfainput.get()
    tinkpath = tinkinput.get()

    fin_msg_1 = "The following reports were generated:"
    fin_msg_2 = (str(dir) + "\\" + str(out_filename))
    fin_msg_3 = (str(dir) + "\\unknown.csv")
    fin_msg_4 = "You may close this window now."

    if (alfa and tink):
        expenses.execute_both(alfapath,tinkpath)
        expenses.csvmerge()
        outlabel_1 = tkinter.Label(guiform, text=fin_msg_1).grid(sticky="W", row=6, column=1)
        outlabel_1 = tkinter.Label(guiform, text=fin_msg_2).grid(sticky="W", row=7, column=1)
        outlabel_1 = tkinter.Label(guiform, text=fin_msg_3).grid(sticky="W", row=8, column=1)
        outlabel_1 = tkinter.Label(guiform, text=fin_msg_4).grid(sticky="W", row=9, column=1)
    else:
        if alfa:
            expenses.execute_alfa(alfapath)
            expenses.csvmerge()
            outlabel_1 = tkinter.Label(guiform, text=fin_msg_1).grid(sticky="W", row=6, column=1)
            outlabel_1 = tkinter.Label(guiform, text=fin_msg_2).grid(sticky="W", row=7, column=1)
            outlabel_1 = tkinter.Label(guiform, text=fin_msg_3).grid(sticky="W", row=8, column=1)
            outlabel_1 = tkinter.Label(guiform, text=fin_msg_4).grid(sticky="W", row=9, column=1)
        else:
            if tink:
                expenses.execute_tinky(tinkpath)
                expenses.csvmerge()
                outlabel_1 = tkinter.Label(guiform, text=fin_msg_1).grid(sticky="W", row=6, column=1)
                outlabel_1 = tkinter.Label(guiform, text=fin_msg_2).grid(sticky="W", row=7, column=1)
                outlabel_1 = tkinter.Label(guiform, text=fin_msg_3).grid(sticky="W", row=8, column=1)
                outlabel_1 = tkinter.Label(guiform, text=fin_msg_4).grid(sticky="W", row=9, column=1)
            else:
                exit()


alfabrowsebutton = tkinter.Button(guiform, text='Browse', state='disable', command=alfabrowse)
tinkbrowsebutton = tkinter.Button(guiform, text='Browse', state='disable',command=tinkbrowse)
processbutton = tkinter.Button(guiform, text='Process...', state='disable', height=2, width=39, command=runmain)

alfabrowsebutton.grid(sticky="E", row=1, column=2)
tinkbrowsebutton.grid(sticky="E", row=3, column=2)
processbutton.grid(sticky="W", row=4, column=1)

alfainput.grid(sticky="W", row=1, column=1)
tinkinput.grid(sticky="W", row=3, column=1)

guiform.mainloop()
