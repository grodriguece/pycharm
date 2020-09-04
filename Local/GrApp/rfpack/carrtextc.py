# case function for carrier selection. switcher is dictionary data type
def carrtext(carr):
    switcher = {
        0: 'Total',
        1: 'Carrier I: 4387',
        2: 'Carrier II: 9712',
        3: 'Carrier III: 9685',
        4: 'Carrier IV: 4364',
    }
    return switcher.get(carr, 'nothing')  # 'nothing' if not found
