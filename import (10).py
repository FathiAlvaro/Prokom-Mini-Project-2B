def menu_4(data, terurut):
    print("\n--- [4] PRIORITAS I / II & CAKUPAN PROVINSI ---")
    print("[1] Prioritas I\n[2] Prioritas II\n[3] Keduanya")
    pilihan = input_pilihan("Pilih [1-3]: ", ["1", "2", "3"])

    if pilihan in ("1", "3"):
        print("\n=== PRIORITAS I ===")
        cetak_pareto([w for w in terurut if w['prioritas'] == "Prioritas I"])
    if pilihan in ("2", "3"):
        print("\n=== PRIORITAS II ===")
        cetak_pareto([w for w in terurut if w['prioritas'] == "Prioritas II"])

    rata = data["cakupan_prov"]
    print(f"\n--- CAKUPAN VS RATA-RATA PROVINSI ({format_angka(rata, 2)}%) ---")
    print(f"{'No':<3} {'Kabupaten/Kota':<24} {'Cakupan':>9} {'Kesenjangan':>12}  Status")
    print("-" * 71)
    for no, w in enumerate(sorted(data["daftar"], key=ambil_cakupan), start=1):
        status = "Di bawah rata-rata" if w['cakupan'] < rata else "Di atas/sama"
        print(f"{no:<3} {w['nama']:<24} {format_angka(w['cakupan'], 2):>8}% "
              f"{format_angka(w['kesenjangan']):>12}  {status}")
