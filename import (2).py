def format_angka(angka, desimal=0):
    teks = f"{angka:,.{desimal}f}"
    return teks.replace(",", "X").replace(".", ",").replace("X", ".")

def baca_angka(teks):
    teks = teks.strip()
    bagian = teks.split(",")
    if len(bagian) > 2:
        return None
    bulat = bagian[0].replace(".", "")
    if not bulat.isdigit():
        return None
    if len(bagian) == 2 and bagian[1].strip("0") != "":
        return None
    return int(bulat)