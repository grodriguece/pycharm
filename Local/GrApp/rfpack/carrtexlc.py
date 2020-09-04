# case function for carrier selection. switcher is dictionary data type
def carrtexl(carr):
    switcher = {
        0: 'Total',
        1: 'Carrier 2600 I: 3075',
        2: 'Carrier 2600 II: 3225',
        3: 'Carrier 1900 HL: 626',
        4: 'Carrier 1900: 651',
    }
    return switcher.get(carr, 'nothing')  # 'nothing' if not found


