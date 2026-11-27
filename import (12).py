def main():
    print("=" * 135)
    print("ANALISIS PRIORITAS PENINGKATAN PELAYANAN ADMINISTRASI KEPENDUDUKAN BERDASARKAN KESENJANGAN KEPEMILIKAN KTP-EL MENGGUNAKAN METODE PARETO")
    print("                                Kelompok 2B | Dataset: cakupan-ktp-el-sumut-kab-kota-2025.csv")
    print("=" * 135)

    login()

    data = minta_data()
    terurut = hitung_pareto(data["daftar"])

    while True:
        print("\n=== MENU UTAMA ===")
        print("[1] Audit Data & Kesenjangan")
        print("[2] Statistik & Rasio Belum Rekam")
        print("[3] Perhitungan Pareto")
        print("[4] Prioritas I / II & Cakupan Provinsi")

        pilihan = input_pilihan("Pilih menu [1-4]: ", ["1", "2", "3", "4"])
        if pilihan == "1":
            menu_1(data)
        elif pilihan == "2":
            menu_2(data)
        elif pilihan == "3":
            menu_3(terurut)
        else:
            menu_4(data, terurut)

if __name__ == "__main__":
    main()
