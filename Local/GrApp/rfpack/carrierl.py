# case function for carrier selection. switcher is dictionary data type
def carrierl(carr):
    switcher = {
        0: 'Lall',
        1: 3075,
        2: 3225,
        3: 626,
        4: 651,
    }
    return switcher.get(carr, 'nothing')
