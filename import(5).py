def ambil_kesenjangan(w):
    return w["kesenjangan"]

def ambil_cakupan(w):
    return w["cakupan"]

def hitung_pareto(daftar):
    terurut = sorted(daftar, key=ambil_kesenjangan, reverse=True)
    total = sum(w["kesenjangan"] for w in terurut)

    kumulatif = 0.0
    for no, w in enumerate(terurut, start=1):
        sebelum = kumulatif
        w["kontribusi"] = w["kesenjangan"] / total * 100 if total > 0 else 0.0
        kumulatif += w["kontribusi"]
        w["kumulatif"] = kumulatif
        masuk_80 = sebelum < AMBANG_PARETO and total > 0
        w["prioritas"] = "Prioritas I" if (masuk_80 and no <= BATAS_PRIORITAS_1) else "Prioritas II"
    return terurut
