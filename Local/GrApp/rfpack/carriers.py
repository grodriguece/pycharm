# case function for carrier selection. switcher is dictionary data type
def carriers(carr):
    switcher = {
        0: 'Uall',
        1: 4387,
        2: 9712,
        3: 9685,
        4: 4364,
    }
    return switcher.get(carr, 'nothing')
