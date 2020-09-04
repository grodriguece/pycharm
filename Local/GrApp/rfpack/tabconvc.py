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
