from pathlib import Path
from rfpack.get_sheet_detailsc import get_sheet_details
from rfpack.csvfrmxlsxc import csvfmxlsx, xlsxfmcsv


def xlsxreord(file, sheet, tpos):
    sheetsdic = get_sheet_details(file)  # get sheet names and ids without opening xlsx file
    fpos = next((index for (index, d) in enumerate(sheetsdic) if d["name"] == sheet), None)
    csvfmxlsx(file, sheetsdic)
    lst = []    # list with new sheet order
    lpos = len(sheetsdic)
    if lpos >= fpos > tpos >= 0:  # move from a high to low position
        for index in range(len(sheetsdic)):
            if index == tpos:  # move to new position
                lst.append(sheetsdic[fpos].copy())
                lst[index]['id'] = str(index+1)
            elif tpos < index <= fpos:  # shift ids inside range
                lst.append(sheetsdic[index-1].copy())
                lst[index]['id'] = str(int(sheetsdic[index-1]['id'])+1)
            else:
                lst.append(sheetsdic[index].copy())  # copy sheet info out of range
    if lpos >= tpos > fpos >= 0:  # move from a low to high position
        for index in range(len(sheetsdic)):
            if index == tpos:  # move to new position
                lst.append(sheetsdic[fpos].copy())
                lst[index]['id'] = str(index + 1)
            elif fpos <= index < tpos:  # shift ids inside range
                lst.append(sheetsdic[index + 1].copy())
                lst[index]['id'] = str(int(sheetsdic[index + 1]['id']) - 1)
            else:
                lst.append(sheetsdic[index].copy())  # copy sheet info out of range
    xlsxfl = Path(str(file.with_suffix('')) + 'R.xlsx')
    xlsxfmcsv(xlsxfl, lst)
    return
