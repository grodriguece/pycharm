import time
from tkinter import ttk
from tkinter import *


def progcntr(offst, d, root1, my_progress1, proglabel21):  # prog bar increase by 1 according to l offset in d/10 sec interval
    for k in range(1, 10):  # done 9 times
        my_progress1['value'] = offst + k
        proglabel21.config(text=my_progress1['value'])
        root1.update_idletasks()
        time.sleep(d/10)