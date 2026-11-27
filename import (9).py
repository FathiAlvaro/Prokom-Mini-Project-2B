def menu_3(terurut):
    p1 = [w for w in terurut if w['prioritas'] == "Prioritas I"]
    print("\n--- [3] PERHITUNGAN PARETO ---")
    print(f"Total kesenjangan : {format_angka(sum(w['kesenjangan'] for w in terurut))}")
    print(f"Prioritas I       : {len(p1)} wilayah (ambang {AMBANG_PARETO:.0f}%, maks. {BATAS_PRIORITAS_1})")
    print(f"Prioritas II      : {len(terurut) - len(p1)} wilayah")
    cetak_pareto(terurut)
