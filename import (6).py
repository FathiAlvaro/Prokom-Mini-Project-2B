def menu_2(data):
    daftar = data["daftar"]
    ks = [w["kesenjangan"] for w in daftar]
    tertinggi = max(daftar, key=ambil_kesenjangan)
    terendah = min(daftar, key=ambil_kesenjangan)
    print("\n--- [2] STATISTIK & RASIO BELUM REKAM ---")
    print(f"Total belum merekam : {format_angka(sum(ks))}")
    print(f"Tertinggi           : {tertinggi['nama']} ({format_angka(tertinggi['kesenjangan'])})")
    print(f"Terendah            : {terendah['nama']} ({format_angka(terendah['kesenjangan'])})")
    print(f"Simpangan baku      : {format_angka(statistics.pstdev(ks), 1)}")

    print(f"\n{'No':<3} {'Kabupaten/Kota':<24} {'Belum Rekam':>12} {'Rasio':>9}")
    print("-" * 51)
    for no, w in enumerate(sorted(daftar, key=ambil_kesenjangan, reverse=True), start=1):
        print(f"{no:<3} {w['nama']:<24} {format_angka(w['kesenjangan']):>12} "
              f"{format_angka(max(100 - w['cakupan'], 0), 2):>8}%")

def cetak_pareto(terurut):
    print(f"\n{'No':<3} {'Kabupaten/Kota':<24} {'Kesenjangan':>12} {'%Kontribusi':>12} {'%Kumulatif':>12}  Prioritas")
    print("-" * 81)
    for no, w in enumerate(terurut, start=1):
        print(f"{no:<3} {w['nama']:<24} {format_angka(w['kesenjangan']):>11} "
              f"{format_angka(w['kontribusi'], 2):>11}% {format_angka(w['kumulatif'], 2):>12}%  {w['prioritas']}")
