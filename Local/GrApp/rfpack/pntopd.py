def pntopd(file, figs, x, y, wi, he):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4, letter, landscape, portrait
    w, h = letter
    c = canvas.Canvas(str(file), pagesize=portrait(letter))
    for png in figs:
        c.drawImage(png, x, h - y, width=wi, height=he)
        c.showPage()
    c.save()