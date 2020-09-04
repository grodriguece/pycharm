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
