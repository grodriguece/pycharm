import time
from pathlib import Path
from rfpack.progcntrc import progcntr
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox


# def progcntr(offst, d):  # prog bar increase by 1 according to l offset in d/10 sec interval
#     for k in range(1, 10):  # done 9 times
#         my_progress['value'] = offst + k
#         proglabel2.config(text=my_progress['value'])
#         root.update_idletasks()
#         time.sleep(d/10)


def tables():
    proglabel2.config(text="")  # label init
    dly = 2  # delay in tenth seconds
    for i in range(0, 100, 10): # from 0 to 99 step 10
        my_progress['value'] = i  # prog bar increase according to i steps in loop
        proglabel2.config(text=my_progress['value'])  # prog value
        root.update_idletasks()
        time.sleep(dly/10)  # delay
        progcntr(i, dly, root, my_progress, proglabel2) # terst to check subrouting execution
    my_progress['value'] = 100  # prog bar finished value
    proglabel2.config(text=my_progress['value'])
    root.update_idletasks()


def audit():
    pass


def missing():
    pass


def undefined():
    pass


def gralaud():
    pass


def specaud():
    pass


iconf = Path('C:/SQLite/IT.ico')
root = Tk()
root.title('NorOcc Table - Audit Process')
root.iconbitmap(iconf)
root.geometry("400x400+350+200")        # WxH+Right+Down
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')  # progress bar
my_progress.grid(row=0, column=0, columnspan=2,pady=10, padx=10, ipadx=10)
proglabel2 = Label(root, text="")  # progress label
proglabel2.grid(row=0, column=2, pady=10)
tables_btn = Button(root, text="Tables", command=tables)  # operation buttons
tables_btn.grid(row=1, column=0, columnspan=1, pady=10, padx=10, ipadx=39)
audit_btn = Button(root, text="Reuse Audits", command=audit)
audit_btn.grid(row=1, column=1, columnspan=1, pady=10, padx=10, ipadx=23)
miss_btn = Button(root, text="Missing UMTS", command=missing)
miss_btn.grid(row=2, column=0, columnspan=1, pady=10, padx=10, ipadx=18)
undef_btn = Button(root, text="Undefined GSM", command=undefined)
undef_btn.grid(row=2, column=1, columnspan=1, pady=10, padx=10, ipadx=17)
miss_btn = Button(root, text="General Audit", command=gralaud)
miss_btn.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx=18)
undef_btn = Button(root, text="Specific Audit", command=specaud)
undef_btn.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx=17)
q_btn = Button(root, text="Exit", command=root.destroy)  # exit button
q_btn.grid(row=4, column=0, columnspan=1, pady=10, padx=10, ipadx=45)
root.mainloop()
