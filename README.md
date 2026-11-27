# Prokom-Mini-Project-2B
# Prioritas Pelayanan Adminduk Berdasarkan Kesenjangan Perekaman KTP-el (Metode Pareto)

Mini Project Pemrograman Komputer, Kelompok 2B
Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas, 2026

## Daftar Isi

- [Latar Belakang](#latar-belakang)
- [Tujuan](#tujuan)
- [Fitur Program](#fitur-program)
- [Cara Kerja Perhitungan](#cara-kerja-perhitungan)
- [Struktur Folder](#struktur-folder)
- [Kebutuhan Software](#kebutuhan-software)
- [Cara Menjalankan](#cara-menjalankan)
- [Cara Pakai](#cara-pakai)
- [Format Data](#format-data)
- [Keterbatasan](#keterbatasan)
- [Tim Pengembang](#tim-pengembang)

## Latar Belakang

KTP-el adalah identitas resmi yang dipakai penduduk untuk mengakses banyak layanan publik, jadi idealnya semua penduduk di setiap wilayah sudah memilikinya. Di Sumatera Utara, cakupan kepemilikan KTP-el sebenarnya sudah tinggi. Tetapi jumlah penduduk yang belum merekam tiap kabupaten/kota ternyata tidak sama.

Kalau wilayah hanya diurutkan dari persentase cakupan, hasilnya bisa menyesatkan. Wilayah dengan cakupan tinggi tetap bisa punya banyak penduduk yang belum merekam, asalkan penduduk wajib KTP-nya besar. Karena itu program ini menghitung kesenjangan dalam jumlah orang (angka absolut), lalu memakai analisis Pareto (prinsip 80/20) untuk menentukan wilayah mana yang perlu didahulukan.

## Tujuan

1. Melihat gambaran jumlah penduduk wajib KTP, perekaman KTP-el, dan kesenjangan perekaman di tiap kabupaten/kota di Sumatera Utara.
2. Membandingkan jumlah penduduk yang belum merekam antarkabupaten/kota.
3. Melihat variasi kesenjangan lewat rata-rata, median, dan simpangan baku.
4. Menentukan wilayah Prioritas I dan Prioritas II dengan analisis Pareto (ambang kumulatif 80% dan maksimal 10 wilayah di Prioritas I).
5. Membandingkan cakupan perekaman tiap kabupaten/kota dengan cakupan tingkat provinsi.

## Fitur Program

| Fitur | Keterangan |
|-------|-----------|
| Login akun | Pengguna mengisi username dan password (class `Akun`) |
| Baca dan validasi CSV | Mengecek file kosong, kolom wajib, kelengkapan kolom tiap baris, dan format angka |
| Pencatatan error dan anomali | Baris bermasalah masuk ke log, program tetap jalan |
| Menu 1: Audit Data & Kesenjangan | Jumlah wilayah valid, total wajib KTP, total perekaman, total kesenjangan, rata-rata, median, log, dan tabel kesenjangan per wilayah |
| Menu 2: Statistik & Rasio Belum Rekam | Wilayah dengan kesenjangan tertinggi dan terendah, simpangan baku, serta rasio belum rekam per wilayah |
| Menu 3: Perhitungan Pareto | Persentase kontribusi, persentase kumulatif, dan label prioritas tiap wilayah |
| Menu 4: Prioritas I / II & Cakupan Provinsi | Daftar Prioritas I, Prioritas II, atau keduanya, plus perbandingan cakupan wilayah dengan cakupan provinsi |
| Validasi input menu | Pilihan di luar menu ditolak, pengguna diminta mengisi ulang |
| Format angka Indonesia | Titik untuk ribuan, koma untuk desimal |

## Cara Kerja Perhitungan

### Penentuan nilai

| Nilai | Cara menentukan |
|-------|----------------|
| Wilayah analisis | Baris yang kode wilayahnya mengandung titik (kabupaten/kota) |
| Data pembanding | Baris dengan kode wilayah `12` (ringkasan Provinsi Sumatera Utara) |
| Data dikecualikan | Wilayah dengan jumlah penduduk wajib KTP bernilai 0 |
| Anomali | Perekaman lebih besar dari wajib KTP, kesenjangan dihitung 0 |
| Cakupan provinsi | Diambil dari baris provinsi. Kalau baris provinsi tidak ada, dihitung dari total perekaman dibagi total wajib KTP seluruh kabupaten/kota |

### Rumus

```
Kesenjangan        = max(Wajib KTP - Perekaman, 0)
% Cakupan          = Perekaman / Wajib KTP x 100
% Kontribusi       = Kesenjangan wilayah / Total kesenjangan x 100
% Kumulatif        = Jumlah berjalan % kontribusi (urut dari kesenjangan terbesar)
Rasio Belum Rekam  = 100 - % Cakupan
```

### Penentuan prioritas

Wilayah diurutkan dari kesenjangan terbesar ke terkecil. Satu wilayah masuk **Prioritas I** kalau persentase kumulatif wilayah sebelumnya masih di bawah 80% dan urutannya tidak lebih dari 10. Sisanya masuk **Prioritas II**.

### Statistik

Rata-rata dan median dihitung dengan `statistics.mean` dan `statistics.median`. Simpangan baku populasi dihitung dengan `statistics.pstdev`.

## Struktur Folder

```
.
├── data/
│   └── cakupan-ktp-el-sumut-kab-kota-2025.csv
├── dokumentasi/
│   └── MINI_PROJECT.docx
├── program/
│   └── mini_project_2B.py
└── README.md
```

| Folder / File | Isi |
|---------------|-----|
| `data/` | Dataset CSV cakupan KTP-el kabupaten/kota Sumatera Utara 2025 |
| `dokumentasi/` | Laporan mini project |
| `program/` | Kode program Python |
| `README.md` | Dokumen ini |

## Kebutuhan Software

- Python 3.6 atau lebih baru
- Hanya memakai pustaka standar (`csv` dan `statistics`), jadi tidak perlu install paket tambahan
- Terminal atau command prompt

## Cara Menjalankan

1. Unduh atau clone repositori ini.
2. Pastikan file `cakupan-ktp-el-sumut-kab-kota-2025.csv` satu folder dengan `mini_project_2B.py` dan namanya persis sama. Kalau nama atau lokasinya beda, program akan meminta path file CSV saat dijalankan.
3. Buka terminal di folder program, lalu jalankan:

   ```bash
   python mini_project_2B.py
   ```

4. Masukkan username dan password saat diminta (lihat [Cara Pakai](#cara-pakai)).
5. Kalau file CSV tidak ditemukan atau isinya tidak valid, program menampilkan pesan error dan meminta path file CSV lain.

## Cara Pakai

Begitu program jalan, pengguna harus login dulu. Akun yang berlaku disimpan di konstanta `DAFTAR_AKUN` di dalam program. Kalau username atau password salah, program meminta input ulang sampai berhasil.

Setelah login dan data berhasil dimuat, menu utama muncul:

```
=== MENU UTAMA ===
[1] Audit Data & Kesenjangan
[2] Statistik & Rasio Belum Rekam
[3] Perhitungan Pareto
[4] Prioritas I / II & Cakupan Provinsi
```

1. Ketik angka 1 sampai 4, lalu tekan Enter.
2. Di menu 4, program menanyakan tampilan yang diinginkan: `1` untuk Prioritas I, `2` untuk Prioritas II, atau `3` untuk keduanya.
3. Kalau pilihan tidak valid, program menampilkan pesan input salah dan meminta pilihan ulang.
4. Setelah satu menu selesai, menu utama muncul lagi. Untuk keluar, hentikan program dengan `Ctrl + C`.

## Format Data

- File CSV dengan pemisah kolom titik koma (`;`) dan encoding UTF-8
- Angka memakai titik sebagai pemisah ribuan dan koma sebagai pemisah desimal
- Sumber data: Cakupan Kepemilikan KTP-el Kabupaten/Kota Provinsi Sumatera Utara Tahun 2025 dari Dinas PMD Dukcapil Provinsi Sumatera Utara, dikonversi dari PDF ke CSV
- Isinya enam kolom, 33 kabupaten/kota, dan satu baris ringkasan provinsi (kode `12`)

Header wajib yang dipakai program:

| Kolom | Keterangan |
|-------|-----------|
| `Kode Wilayah` | Kode administratif wilayah |
| `Kabupaten/Kota` | Nama wilayah |
| `Jumlah Penduduk Wajib KTP` | Jumlah penduduk yang wajib punya KTP |
| `Perekaman KTP-EL` | Jumlah penduduk yang sudah merekam |

Dua kolom lain di dataset, yaitu `Jumlah Penduduk Ber-KTP` dan `Cakupan Kepemilikan KTP-EL (%)`, tidak dipakai dalam perhitungan.

## Keterbatasan

1. Data hanya dari satu file CSV, yaitu data kabupaten/kota Sumatera Utara tahun 2025.
2. Analisis hanya mencakup kesenjangan perekaman KTP-el, yaitu selisih penduduk wajib KTP dan penduduk yang sudah merekam.
3. Program tidak menghitung penduduk yang belum punya KTP-el secara langsung, karena datanya perekaman, bukan kepemilikan.
4. Hasil hanya tampil di terminal (tabel dan ringkasan). Tidak ada diagram Pareto dan hasil tidak disimpan ke file.
5. FMEA tidak dihitung, karena dataset tidak memuat penyebab kegagalan, dampak, maupun nilai risiko.
6. Prioritas I dibatasi maksimal 10 wilayah dengan ambang kumulatif 80%.
7. Login hanya autentikasi sederhana dengan akun yang tertulis di kode, jadi bukan pengamanan sungguhan.

## Tim Pengembang

**Anggota Kelompok 2B**

| Nama | NIM |
|------|-----|
| Dea Permata Aldosi | 2610931034 |
| Fathi Alvaro Wiraja | 2610932029 |
| Andara Nurul Fatimah | 2610932045 |
| Melsa Sigianto Putri | 2610933019 |
