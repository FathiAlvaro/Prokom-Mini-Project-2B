def muat_csv(path):
    with open(path, "r", encoding="utf-8-sig", errors="replace", newline="") as file:
        baris = list(csv.reader(file, delimiter=";"))

    if not baris:
        return None, "File kosong."

    header = [kol.strip() for kol in baris[0]]
    for kolom in KOLOM_WAJIB:
        if kolom not in header:
            return None, f"Kolom wajib '{kolom}' tidak ditemukan."

    posisi_kolom = {}
    for nomor, kolom in enumerate(header):
        posisi_kolom[kolom] = nomor

    i_kode = posisi_kolom["Kode Wilayah"]
    i_nama = posisi_kolom["Kabupaten/Kota"]
    i_wajib = posisi_kolom["Jumlah Penduduk Wajib KTP"]
    i_rekam = posisi_kolom["Perekaman KTP-EL"]
    terjauh = max(i_kode, i_nama, i_wajib, i_rekam)

    provinsi = None
    daftar = []
    error_log = []
    anomali_log = []

    for no, row in enumerate(baris[1:], start=2):
        if len(row) <= terjauh:
            if any(sel.strip() for sel in row):
                error_log.append(f"Baris {no}: jumlah kolom kurang.")
            continue

        kode = row[i_kode].strip()
        nama = row[i_nama].strip()
        if not kode and not nama:
            continue

        wajib = baca_angka(row[i_wajib])
        rekam = baca_angka(row[i_rekam])
        if wajib is None or rekam is None:
            error_log.append(f"Baris {no} ({nama or kode}): angka tidak valid / kosong.")
            continue

        w = {
            "kode": kode,
            "nama": nama,
            "wajib": wajib,
            "rekam": rekam,
            "kesenjangan": 0,
            "cakupan": 0.0,
            "kontribusi": 0.0,
            "kumulatif": 0.0,
            "prioritas": ""
        }

        if wajib == 0:
            anomali_log.append(f"{nama} ({kode}): Wajib KTP = 0, dikecualikan.")
            continue
        if rekam > wajib:
            anomali_log.append(
                f"{nama} ({kode}): Rekam ({format_angka(rekam)}) > Wajib "
                f"({format_angka(wajib)}), kesenjangan dihitung 0."
            )

        w["kesenjangan"] = max(wajib - rekam, 0)
        w["cakupan"] = rekam / wajib * 100

        if kode == KODE_PROVINSI:
            provinsi = w
        elif "." in kode:
            daftar.append(w)
        else:
            error_log.append(f"Baris {no} ({nama or kode}): format kode tidak sesuai.")

    if not daftar:
        return None, "Tidak ada data kabupaten/kota yang valid."

    if provinsi is not None:
        cakupan_prov = provinsi["cakupan"]
    else:
        cakupan_prov = sum(w["rekam"] for w in daftar) / sum(w["wajib"] for w in daftar) * 100

    hasil = {"daftar": daftar, "provinsi": provinsi, "cakupan_prov": cakupan_prov, "error": error_log, "anomali": anomali_log}
    return hasil, None
