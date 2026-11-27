# Prokom-Mini-Project-2B
# Analisis Prioritas Peningkatan Pelayanan Administrasi Kependudukan Berdasarkan Kesenjangan Kepemilikan KTP-el Menggunakan Metode Pareto

## Daftar Isi

- [Latar Belakang](#latar-belakang)
- [Tujuan](#tujuan)
- [Fitur Utama](#fitur-utama)
- [Metodologi](#metodologi)
- [Struktur Repositori](#struktur-repositori)
- [Syarat Minimal Software](#syarat-minimal-software)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Format Data](#format-data)
- [Keterbatasan](#keterbatasan)
- [Stakeholder Pengembang](#stakeholder-pengembang)

## Latar Belakang

KTP-el adalah identitas resmi penduduk yang menjadi dasar untuk memperoleh berbagai layanan publik, sehingga kepemilikannya perlu menjangkau seluruh penduduk di setiap wilayah. Cakupan kepemilikan KTP-el di Provinsi Sumatera Utara sudah tinggi, tetapi jumlah penduduk yang belum melakukan perekaman berbeda pada setiap kabupaten/kota. Pengurutan berdasarkan persentase cakupan saja belum cukup, karena wilayah dengan cakupan tinggi tetap dapat memiliki jumlah penduduk belum merekam yang besar bila penduduk wajib KTP-nya banyak. Karena itu program ini menghitung kesenjangan secara absolut, lalu memakai analisis Pareto (prinsip 80/20) untuk menentukan wilayah yang perlu diprioritaskan.

## Tujuan

1. Mengetahui gambaran jumlah penduduk wajib KTP, jumlah perekaman KTP-el, dan kesenjangan perekaman pada setiap kabupaten/kota di Sumatera Utara.
2. Membandingkan jumlah penduduk yang belum merekam antarkabupaten/kota.
3. Mengetahui variasi kesenjangan melalui rata-rata, median, dan simpangan baku.
4. Menentukan wilayah Prioritas I dan Prioritas II dengan analisis Pareto (ambang kumulatif 80% dan maksimal 10 wilayah pada Prioritas I).
5. Membandingkan cakupan perekaman tiap kabupaten/kota dengan cakupan tingkat provinsi.

## Fitur Utama

| Fitur | Keterangan |
|-------|-----------|
| Login akun | Pengguna harus memasukkan username dan password (class `Akun`) |
| Pembacaan dan validasi CSV | Memeriksa file kosong, kolom wajib, kelengkapan kolom tiap baris, dan format angka |
| Pencatatan error dan anomali | Baris bermasalah dicatat dalam log tanpa menghentikan program |
| Menu 1: Audit Data & Kesenjangan | Jumlah wilayah valid, total wajib KTP, total perekaman, total kesenjangan, rata-rata, median, log, dan tabel kesenjangan per wilayah |
| Menu 2: Statistik & Rasio Belum Rekam | Wilayah dengan kesenjangan tertinggi dan terendah, simpangan baku, dan rasio belum rekam per wilayah |
| Menu 3: Perhitungan Pareto | Persentase kontribusi, persentase kumulatif, dan label prioritas setiap wilayah |
| Menu 4: Prioritas I / II & Cakupan Provinsi | Daftar Prioritas I, Prioritas II, atau keduanya, serta perbandingan cakupan tiap wilayah dengan cakupan provinsi |
| Validasi input menu | Pilihan di luar menu ditolak dan pengguna diminta memasukkan ulang |
| Format angka Indonesia | Titik sebagai pemisah ribuan dan koma sebagai pemisah desimal |

## Metodologi

### Penentuan Nilai

| Nilai | Cara Penentuan |
|-------|---------------|
| Wilayah analisis | Baris dengan kode wilayah yang mengandung titik (kabupaten/kota) |
| Data pembanding | Baris dengan kode wilayah `12` (ringkasan Provinsi Sumatera Utara) |
| Data dikecualikan | Wilayah dengan jumlah penduduk wajib KTP bernilai 0 |
| Anomali | Perekaman lebih besar dari wajib KTP, kesenjangan dihitung 0 |
| Cakupan provinsi | Diambil dari baris provinsi, atau dihitung dari total perekaman dibagi total wajib KTP seluruh kabupaten/kota bila baris provinsi tidak ada |

### Perhitungan

```
Kesenjangan        = max(Wajib KTP - Perekaman, 0)
% Cakupan          = Perekaman / Wajib KTP x 100
% Kontribusi       = Kesenjangan wilayah / Total kesenjangan x 100
% Kumulatif        = Jumlah berjalan % kontribusi (urut kesenjangan terbesar)
Rasio Belum Rekam  = 100 - % Cakupan
```

### Penentuan Prioritas

Wilayah diurutkan dari kesenjangan terbesar ke terkecil. Sebuah wilayah masuk **Prioritas I** apabila persentase kumulatif wilayah sebelumnya masih di bawah 80% dan urutannya tidak lebih dari 10. Wilayah lainnya masuk **Prioritas II**.

### Statistik

Rata-rata dan median dihitung dengan `statistics.mean` dan `statistics.median`, sedangkan simpangan baku populasi dengan `statistics.pstdev`.

## Struktur Repositori

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

## Syarat Minimal Software

- Python 3.6 atau lebih baru
- Hanya memakai pustaka standar (`csv` dan `statistics`), sehingga tidak perlu instalasi paket tambahan
- Terminal atau command prompt

## Cara Menjalankan Program

1. Unduh atau clone repositori ini.
2. Pastikan file `cakupan-ktp-el-sumut-kab-kota-2025.csv` berada satu folder dengan `mini_project_2B.py`, dan namanya persis sama. Jika nama atau lokasinya berbeda, program akan meminta path file CSV saat dijalankan.
3. Buka terminal pada folder program, lalu jalankan:

   ```bash
   python mini_project_2B.py
   ```

4. Masukkan username dan password saat diminta (lihat [Panduan Penggunaan](#panduan-penggunaan)).
5. Jika file CSV tidak ditemukan atau isinya tidak valid, program menampilkan pesan error dan meminta path file CSV lain.

## Panduan Penggunaan

Saat program dijalankan, pengguna diminta login terlebih dahulu. Akun yang berlaku tersimpan pada konstanta `DAFTAR_AKUN` di dalam program. Jika username atau password salah, program meminta input ulang sampai login berhasil.

Setelah login berhasil dan data dimuat, program menampilkan menu utama:

```
=== MENU UTAMA ===
[1] Audit Data & Kesenjangan
[2] Statistik & Rasio Belum Rekam
[3] Perhitungan Pareto
[4] Prioritas I / II & Cakupan Provinsi
```

1. Ketik angka 1 sampai 4 lalu tekan Enter.
2. Pada menu 4, program menanyakan tampilan yang diinginkan: `1` untuk Prioritas I, `2` untuk Prioritas II, atau `3` untuk keduanya.
3. Jika memasukkan pilihan yang tidak valid, program menampilkan pesan input salah dan meminta pilihan ulang.
4. Setelah satu menu selesai, menu utama muncul kembali. Untuk keluar, hentikan program dengan `Ctrl + C`.

## Format Data

- Format file: CSV dengan pemisah kolom titik koma (`;`) dan encoding UTF-8
- Angka memakai titik sebagai pemisah ribuan dan koma sebagai pemisah desimal
- Dataset bersumber dari data Cakupan Kepemilikan KTP-el Kabupaten/Kota Provinsi Sumatera Utara Tahun 2025 yang dipublikasikan Dinas PMD Dukcapil Provinsi Sumatera Utara, lalu dikonversi dari PDF ke CSV
- Berisi enam kolom, 33 kabupaten/kota, dan satu baris ringkasan provinsi (kode `12`)

Header wajib yang digunakan program:

| Kolom | Keterangan |
|-------|-----------|
| `Kode Wilayah` | Kode administratif wilayah |
| `Kabupaten/Kota` | Nama wilayah |
| `Jumlah Penduduk Wajib KTP` | Jumlah penduduk yang wajib memiliki KTP |
| `Perekaman KTP-EL` | Jumlah penduduk yang sudah melakukan perekaman |

Dua kolom lain pada dataset, yaitu `Jumlah Penduduk Ber-KTP` dan `Cakupan Kepemilikan KTP-EL (%)`, tidak dipakai dalam perhitungan.

## Keterbatasan

1. Data hanya berasal dari satu file CSV, yaitu data kabupaten/kota Sumatera Utara tahun 2025.
2. Analisis dibatasi pada kesenjangan perekaman KTP-el, yaitu selisih jumlah penduduk wajib KTP dan jumlah penduduk yang telah merekam.
3. Program tidak menghitung jumlah penduduk yang belum memiliki KTP-el secara langsung, karena hanya memakai data perekaman, bukan data kepemilikan.
4. Hasil hanya ditampilkan di terminal dalam bentuk tabel dan ringkasan. Program tidak membuat diagram Pareto dan tidak menyimpan hasil ke file keluaran.
5. Program tidak menghitung FMEA, karena dataset tidak memuat penyebab kegagalan, dampak, maupun nilai risiko.
6. Prioritas I dibatasi maksimal 10 wilayah dengan ambang kumulatif 80%.
7. Login hanya berupa autentikasi sederhana dengan akun yang tertulis di dalam kode, sehingga tidak ditujukan sebagai pengamanan sungguhan.

## Stakeholder Pengembang

**Anggota Kelompok 2B**

| Nama | NIM |
|------|-----|
| Dea Permata Aldosi | 2610931034 |
| Fathi Alvaro Wiraja | 2610932029 |
| Andara Nurul Fatimah | 2610932045 |
| Melsa Sigianto Putri | 2610933019 |
