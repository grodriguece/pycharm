# case function for carrier selection. switcher is dictionary data type
def carrierl(carr):
    switcher = {
        0: 'all',
        1: 3075,
        2: 3225,
        3: 626,
        4: 651,
    }
    return switcher.get(carr, 'nothing')


# case function for carrier selection. switcher is dictionary data type
def carriers(carr):
    switcher = {
        0: 'all',
        1: 4387,
        2: 9712,
        3: 9685,
        4: 4364,
    }
    return switcher.get(carr, 'nothing')


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


def tabconv(tabsent):
    switcher = {
        'LNCEL': 'LNCEL_Full',
        'LNHOIF': 'LNHOIF_ref',
        'LNBTS': 'LNBTS_Full',
        'LNHOW': 'LNHOW_ref',
        'WCEL': 'WCEL_FULL1',
        'RNFC': 'RNFC_ref',
        'AMLEPR': 'AMLEPR_ref',
        'ANRPRL': 'ANRPRL_ref',
        'LNREL': 'LNREL_NO',
        'IRFIM': 'IRFIM_ref',
        'UFFIM_UTRFDDCARFRQL': 'UFFIM_UTRFDDCARFRQL_ref',
        'IAFIM_INTRFRNCLIST': 'IAFIM_INTRFRNCLIST_ref',
        'UFFIM': 'UFFIM_ref',
    }
    return switcher.get(tabsent, 'nothing')  # 'nothing' if not found


def zone(zon):
    switcher = {
        0: 'MED',
        1: 'PER',
        2: 'MAN',
        3: 'ARM',
        4: 'QUB',
        5: 'ANT',
        6: 'RIS',
        7: 'CAD',
        8: 'QUI',
        9: 'CHO',
    }
    return switcher.get(zon, 'nothing')


# groups zones for facet wrap plot purposes
def znfrmt(seq):
    switcher = {
        0: ['full', 'MED', 'ANT'],
        1: ['PER', 'MAN', 'ARM'],
        2: ['RIS', 'CAD', 'QUI'],
        3: ['QUB', 'CHO'],
    }
    return switcher.get(seq, 'nothing')


def tecnol(tech):
    switcher = {
        0: 'gsm',
        1: 'umts',
        2: 'lte',
    }
    return switcher.get(tech, 'nothing')
