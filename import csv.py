# ANALISIS PRIORITAS KESENJANGAN KTP-EL SUMUT 2025 (METODE PARETO)
import os

NAMA_DEFAULT = "cakupan-ktp-el-sumut-kab-kota-2025(1).csv"
KOLOM_WAJIB = ["Kode Wilayah", "Kabupaten/Kota", "Jumlah Penduduk Wajib KTP",
               "Jumlah Penduduk Ber-KTP", "Perekaman KTP-EL",
               "Cakupan Kepemilikan KTP-EL (%)"]


def hitung_cakupan(b, w):
    if w == 0:
        return 0                                  # hindari pembagian dengan nol
    return b / w * 100


def angka(n):
    return "{:,}".format(n).replace(",", ".")     # 99297 -> 99.297


def persen(x):
    return "{:.2f}".format(x).replace(".", ",")   # 96.06 -> 96,06


class Wilayah:
    def __init__(self, nama, w, b, r):
        self.nama = nama
        self.w = w                                # penduduk wajib KTP
        self.b = b                                # penduduk ber-KTP
        self.r = r                                # perekaman
        self.k = w - b                            # kesenjangan
        self.belum_rekam = w - r
        self.rekam_belum = r - b
        self.cakupan = hitung_cakupan(b, w)
        self.persen = 0
        self.kumulatif = 0
        self.prioritas = ""
        self.di_bawah = False                     # cakupan < cakupan Sumut

    def cek_data(self):
        """Kembalikan alasan jika data tidak wajar, atau '' jika wajar."""
        if self.w <= 0:
            return "penduduk wajib KTP <= 0"
        if self.r > self.w:
            return "perekaman lebih besar dari penduduk wajib KTP"
        if self.b > self.r:
            return "penduduk ber-KTP lebih besar dari perekaman"
        return ""

    def tampil(self):
        print(self.nama)
        print("  Penduduk wajib KTP :", angka(self.w))
        print("  Perekaman          :", angka(self.r))
        print("  Penduduk ber-KTP   :", angka(self.b))
        print("  Kesenjangan        :", angka(self.k), "(belum merekam",
              angka(self.belum_rekam) + ", sudah rekam belum KTP",
              angka(self.rekam_belum) + ")")
        print("  Cakupan            :", persen(self.cakupan), "%")
        print("  Prioritas          :", self.prioritas)


def ambil_k(d):
    return d.k


def ambil_cakupan(d):
    return d.cakupan


def ambil_nama(d):
    return d.nama.lower()


def baca_file(nama_file):
    """Baca CSV, kembalikan (daftar Wilayah, daftar baris dilewati) atau None."""
    try:
        with open(nama_file, encoding="utf-8-sig") as file:
            baris = file.readlines()
    except OSError:
        print("KESALAHAN: file '" + nama_file + "' tidak ditemukan/tidak dapat dibuka.")
        return None
    if len(baris) == 0:
        print("KESALAHAN: file kosong.")
        return None

    kolom = []
    for k in baris[0].split(";"):
        kolom.append(k.strip())
    for k in KOLOM_WAJIB:
        if k not in kolom:
            print("KESALAHAN: kolom '" + k + "' tidak ditemukan.")
            return None

    data = []
    dilewati = []
    for i in range(1, len(baris)):
        bagian = baris[i].strip().split(";")
        if baris[i].replace(";", "").strip() == "":
            continue                              # baris kosong (;;;;;)
        if "." not in bagian[0]:
            continue                              # baris provinsi (kode "12")
        try:
            w = int(bagian[2].replace(".", ""))
            b = int(bagian[3].replace(".", ""))
            r = int(bagian[4].replace(".", ""))
            if w < 0 or b < 0 or r < 0:
                raise ValueError
        except (ValueError, IndexError):
            dilewati.append(i + 1)                # nomor baris tidak valid
            continue
        data.append(Wilayah(bagian[1].strip(), w, b, r))
    return data, dilewati


def hitung_pareto(data):
    """Urutkan, hitung persen, kumulatif, prioritas. Kembalikan (urut, total, cakupan)."""
    total_k = 0
    total_w = 0
    total_b = 0
    for d in data:
        total_k = total_k + d.k
        total_w = total_w + d.w
        total_b = total_b + d.b
    cakupan_sumut = hitung_cakupan(total_b, total_w)

    urut = sorted(data, key=ambil_k, reverse=True)
    kum = 0
    sudah80 = False
    for d in urut:
        d.persen = d.k / total_k * 100
        kum = kum + d.persen
        d.kumulatif = kum
        d.di_bawah = d.cakupan < cakupan_sumut
        if not sudah80:                           # I sampai kumulatif pertama >= 80%
            d.prioritas = "I"
            if kum >= 80:
                sudah80 = True
        else:
            d.prioritas = "II"
    return urut, total_k, cakupan_sumut


def tampil_tabel(daftar, urut):
    print("No".ljust(4), "Kabupaten/Kota".ljust(22), "Kesenjangan".rjust(11),
          "% Kontr.".rjust(8), "% Kum.".rjust(8), "Cakupan".rjust(8), "Prior".rjust(5))
    for d in daftar:
        tanda = ""
        if d.di_bawah:
            tanda = " *"                          # * = di bawah cakupan Sumut
        print(str(urut.index(d) + 1).ljust(4), d.nama[:22].ljust(22),
              angka(d.k).rjust(11), persen(d.persen).rjust(8),
              persen(d.kumulatif).rjust(8), persen(d.cakupan).rjust(8),
              d.prioritas.rjust(5) + tanda)
    print("* = cakupan di bawah cakupan Sumut")


def tampil_ringkasan(urut, total_k, cakupan_sumut):
    belum_rekam = 0
    rekam_belum = 0
    p1 = 0
    p1_bawah = 0
    for d in urut:
        belum_rekam = belum_rekam + d.belum_rekam
        rekam_belum = rekam_belum + d.rekam_belum
        if d.prioritas == "I":
            p1 = p1 + 1
            if d.di_bawah:
                p1_bawah = p1_bawah + 1
    print("Jumlah wilayah               :", len(urut))
    print("Total kesenjangan            :", angka(total_k), "orang")
    print("Cakupan Sumut                :", persen(cakupan_sumut), "%")
    print("Kesenjangan terbesar         :", urut[0].nama, "(" + angka(urut[0].k) + " orang)")
    print("Wilayah Prioritas I          :", p1, "(" + persen(p1 / len(urut) * 100) + " %)")
    print("Prioritas I di bawah Sumut   :", p1_bawah, "wilayah")
    print("Belum merekam                :", angka(belum_rekam))
    print("Sudah rekam, belum ber-KTP   :", angka(rekam_belum))
    if belum_rekam > rekam_belum:
        print("Kesimpulan: layanan PEREKAMAN perlu diperkuat lebih dulu.")
    else:
        print("Kesimpulan: layanan PENERBITAN KTP-el perlu diperkuat lebih dulu.")


def minta_angka(pesan, awal, akhir):
    while True:
        jawab = input(pesan).strip()
        if jawab.isdigit() and awal <= int(jawab) <= akhir:
            return int(jawab)
        print("  Masukkan angka", awal, "sampai", akhir)


def main():
    nama_file = input("Nama/lokasi file CSV [Enter = " + NAMA_DEFAULT + "]: ").strip('" ')
    if nama_file == "":
        nama_file = NAMA_DEFAULT
    folder = os.path.dirname(os.path.abspath(__file__))   # cari di folder program
    hasil = baca_file(os.path.join(folder, nama_file))
    if hasil is None:
        return
    data, dilewati = hasil
    if len(data) == 0:
        print("Dataset kosong: tidak ada data kabupaten/kota yang valid.")
        return

    for baris_ke in dilewati:
        print("Baris", baris_ke, "tidak valid, dilewati.")
    for d in data:
        if d.cek_data() != "":
            print("Perlu dicek:", d.nama, "-", d.cek_data())

    urut, total_k, cakupan_sumut = hitung_pareto(data)

    while True:
        print("\n=== MENU ===")
        print("1. Tabel Pareto")
        print("2. Ringkasan")
        print("3. Cari wilayah")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            print("Urutan: 1. Kesenjangan  2. Cakupan terendah  3. Nama A-Z")
            urutan = minta_angka("Pilih urutan (1-3): ", 1, 3)
            n = minta_angka("Tampilkan berapa wilayah (1-" + str(len(urut)) + "): ", 1, len(urut))
            if urutan == 1:
                daftar = urut
            elif urutan == 2:
                daftar = sorted(urut, key=ambil_cakupan)
            else:
                daftar = sorted(urut, key=ambil_nama)
            tampil_tabel(daftar[:n], urut)
        elif pilihan == "2":
            tampil_ringkasan(urut, total_k, cakupan_sumut)
        elif pilihan == "3":
            kata = input("Nama kabupaten/kota: ").strip().lower()
            ketemu = False
            for d in urut:
                if kata != "" and kata in d.nama.lower():
                    d.tampil()
                    ketemu = True
            if not ketemu:
                print("Wilayah tidak ditemukan.")
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


main()
