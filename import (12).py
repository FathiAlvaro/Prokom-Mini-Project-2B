def minta_data():
    path = NAMA_FILE
    while True:
        data, error = muat_csv(path)
        if data is not None:
            return data
        print(f"[ERROR] {error}")
        masukan = input("Masukkan path file CSV lain: ").strip()
        if masukan:
            path = masukan
