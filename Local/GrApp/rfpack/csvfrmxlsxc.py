import pandas as pd
from pathlib import Path
from xlsx2csv import Xlsx2csv
from pyexcelerate import Workbook
from rfpack.pyexcelerate_toexcel import pyexecelerate_to_excel


def csvfrmxlsx(xlsxfl, df):  # create csv files in csv folder on parent directory
    (xlsxfl.parent / 'csv').mkdir(parents=True, exist_ok=True)
    for index, row in df.iterrows():  # table row iteration by audit2 column type
        shnum = row['id']
        shnph = xlsxfl.parent / 'csv' / Path(row['name'] + '.csv')  # path for converted csv file
        Xlsx2csv(str(xlsxfl), outputencoding="utf-8").convert(str(shnph), sheetid=int(shnum))  # id from openxlsx
    return


def csvfmxlsx(xlsxfl, lst):  # create csv files in csv folder on parent directory from list
    (xlsxfl.parent / 'csv').mkdir(parents=True, exist_ok=True)
    for index in range(len(lst)):  # table row iteration by audit2 column type
        shnum = lst[index]['id']
        shnph = xlsxfl.parent / 'csv' / Path(lst[index]['name'] + '.csv')  # path for converted csv file
        Xlsx2csv(str(xlsxfl), outputencoding="utf-8").convert(str(shnph), sheetid=int(shnum))  # id from openxlsx
    return


def xlsxfmcsv(xlsxfl, lst, iterini, root1, my_progress1, proglabel21):
    wb = Workbook()  # pyexcelerate Workbook
    for index in range(len(lst)):
        my_progress1['value'] = iterini + round(index / len(lst) * 15)  # prog bar up to iterini + 15
        proglabel21.config(text=my_progress1['value'])  # prog bar updt
        root1.update_idletasks()
        df1 = pd.read_csv(xlsxfl.parent / 'csv' / Path(lst[index]['name'] + '.csv'))
        pyexecelerate_to_excel(wb, df1, sheet_name=lst[index]['name'], index=False)
    wb.save(xlsxfl)
    my_progress1['value'] = iterini + 25  # prog bar up to iterini + 25
    proglabel21.config(text=my_progress1['value'])  # prog bar updt
    root1.update_idletasks()
    return

