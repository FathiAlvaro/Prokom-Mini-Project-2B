def menu_1(data):
    daftar = data["daftar"]
    ks = [w["kesenjangan"] for w in daftar]
    print("\n--- [1] AUDIT DATA & KESENJANGAN ---")
    print(f"Jumlah kabupaten/kota valid : {len(daftar)}")
    print(f"Total Wajib KTP             : {format_angka(sum(w['wajib'] for w in daftar))}")
    print(f"Total Perekaman KTP-EL      : {format_angka(sum(w['rekam'] for w in daftar))}")
    print(f"Total Kesenjangan           : {format_angka(sum(ks))}")
    print(f"Rata-rata / Median          : {format_angka(statistics.mean(ks), 1)} / "
          f"{format_angka(statistics.median(ks), 1)}")

    for judul, log in (("Baris error/diabaikan", data["error"]),
                       ("Anomali data", data["anomali"])):
        if log:
            print(f"\n{judul} ({len(log)}):")
            for pesan in log:
                print(f"  - {pesan}")
        else:
            print(f"\n{judul}: tidak ada.")

    print(f"\n{'No':<3} {'Kabupaten/Kota':<24} {'Wajib':>12} {'Rekam':>12} {'Kesenjangan':>12}")
    print("-" * 67)
    for no, w in enumerate(sorted(daftar, key=ambil_kesenjangan, reverse=True), start=1):
        print(f"{no:<3} {w['nama']:<24} {format_angka(w['wajib']):>12} "
              f"{format_angka(w['rekam']):>12} {format_angka(w['kesenjangan']):>12}")