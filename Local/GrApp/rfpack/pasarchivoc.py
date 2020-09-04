import tkinter as tk
import sqlite3
import pandas as pd
import timeit
from pyexcelerate import Workbook
from datetime import date
from tkinter import messagebox
from tkinter import Label


def pasarchivo(datb, tablas, tipo, iterini, root1, my_progress1, proglabel21):
    """copy to csv files tables from query results"""
    top = tk.Toplevel()
    top.title("Process Progress")
    top.geometry("300x600+750+120")
    top.iconbitmap('IT.ico')
    dat_dir = datb.parent
    start_time = timeit.default_timer()
    conn = sqlite3.connect(datb)                # database connection
    c = conn.cursor()
    today = date.today()
    df1 = pd.read_csv(tablas)
    xls_file = tipo + today.strftime("%y%m%d") + ".xlsx"
    xls_path = dat_dir / xls_file                   # xls file path-name
    csv_path = dat_dir / "csv"                      # csv path to store big data
    wb = Workbook()                                 # excelerator file init
    i = 0
    for index, row in df1.iterrows():               # panda row iteration tablas file by tipo column
        my_progress1['value'] = iterini + round(index / len(df1) * 95)  # prog bar up to iterini + 95
        proglabel21.config(text=my_progress1['value'])  # prog bar updt
        root1.update_idletasks()
        line = row[tipo]
        if not pd.isna(row[tipo]):                  # nan null values validation
            try:
                df = pd.read_sql_query("select * from " + line + ";", conn)  # pandas dataframe from sqlite
                if len(df) > 1000000:                   # excel not supported, big file
                    csv_loc = line + today.strftime("%y%m%d") + '.csv.gz'   # compressed csv file name
                    print('Table {} saved in {}'.format(line, csv_loc))
                    feedbk = tk.Label(top, text='Table {} saved in {}'.format(line, csv_loc))
                    feedbk.pack()
                    top.update_idletasks()
                    df.to_csv(csv_path / csv_loc, compression='gzip')       # pandas dataframe saved to csv
                else:
                    data = [df.columns.tolist()] + df.values.tolist()
                    data = [[index] + row for index, row in zip(df.index, data)]
                    wb.new_sheet(line, data=data)
                    print('Table {} stored in xlsx sheet'.format(line))
                    feedbk = tk.Label(top, text='Table {} stored in xlsx sheet'.format(line))
                    feedbk.pack()
                    top.update_idletasks()
                    i += 1
            except sqlite3.Error as error:  # sqlite error handling
                print('SQLite error: %s' % (' '.join(error.args)))
                feedbk = tk.Label(top, text='SQLite error: %s' % (' '.join(error.args)))
                feedbk.pack()
    end_time = timeit.default_timer()
    delta = round(end_time - start_time, 2)
    print("Data proc took " + str(delta) + " secs")
    feedbk = tk.Label(top, text="Data proc took " + str(delta) + " secs")
    feedbk.pack()
    top.update_idletasks()
    deltas = 0
    if i == 0:
        print('No tables to excel')
        feedbk = tk.Label(top, text='No tables to excel')
        feedbk.pack()
    else:
        print("Saving tables in {} workbook".format(xls_path))
        feedbk = tk.Label(top, text="Saving tables in {} workbook".format(xls_path))
        feedbk.pack()
        top.update_idletasks()
        start_time = timeit.default_timer()
        wb.save(xls_path)
        end_time = timeit.default_timer()
        deltas = round(end_time - start_time, 2)
        print("xlsx save took " + str(deltas) + " secs")
        feedbk = tk.Label(top, text="xlsx save took " + str(deltas) + " secs")
        feedbk.pack()
        top.update_idletasks()
    print("Total time " + str(delta+deltas) + " secs")
    feedbk = tk.Label(top, text="Total time " + str(delta+deltas) + " secs")
    feedbk.pack()
    top.update_idletasks()
    c.close()
    conn.close()
    my_progress1['value'] = 100  # prog bar increase a cording to i steps in loop
    proglabel21.config(text=my_progress1['value'])
    response = messagebox.showinfo("Tablas", "Process Finished")
    proglabel3 = Label(root1, text=response)
    # proglabel3 = Label(root, text="")
    # proglabel3.grid(row=3, column=1, pady=10)
    my_progress1['value'] = 0  # prog bar increase a cording to i steps in loop
    proglabel21.config(text="   ")
    root1.update_idletasks()
