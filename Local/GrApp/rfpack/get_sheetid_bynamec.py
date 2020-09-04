import pandas as pd


def get_sheetid_bynamef(tablas, tipo, dict):
    df2 = pd.DataFrame.from_dict(dict)
    df1 = pd.read_csv(tablas)
    df1 = df1.loc[:, df1.columns == tipo].dropna()  # only column tipo is selected without NaN
    df1.rename(columns={tipo: "name"}, inplace=True)
    df1 = pd.merge(df1, df2, on='name')
    return df1


def get_sheetid_bynamei(item, dict):
    df2 = pd.DataFrame.from_dict(dict)
    df1 = df2[(df2['name'] == item)].reset_index()
    return df1


