# Prokom-Mini-Project-2B
# Alur Program

## 1. Titik Masuk: main()

Program berjalan dari blok if __name__ == "__main__" yang memanggil main(). Fungsi ini mencetak judul program, memanggil minta_data() untuk mendapatkan data, lalu memanggil hitung_pareto() sekali saja dan menyimpan hasilnya di variabel terurut. Setelah itu program masuk ke perulangan while True yang menampilkan menu utama, meminta pilihan lewat input_pilihan(), dan memanggil menu_1 sampai menu_4 sesuai pilihan. Perulangan ini tidak punya perintah keluar, sehingga menu muncul kembali setiap kali satu menu selesai ditampilkan.

## 2. Pemuatan Data: minta_data()

Fungsi ini memakai path bawaan dari konstanta NAMA_FILE dan memanggil muat_csv(path) di dalam perulangan. Jika muat_csv() mengembalikan data, fungsi langsung mengembalikannya ke main(). Jika yang dikembalikan adalah pesan error, pesan itu dicetak dan pengguna diminta mengetik path file CSV lain, lalu pemuatan diulang sampai berhasil.

## 3. Pembacaan dan Validasi: muat_csv(path)

File dibuka dengan encoding utf-8-sig dan dibaca memakai csv.reader dengan pemisah titik koma. Jika tidak ada baris sama sekali, fungsi mengembalikan error "File kosong". Baris pertama dianggap header, lalu setiap nama di KOLOM_WAJIB diperiksa keberadaannya. Posisi keempat kolom wajib disimpan sebagai indeks, dan indeks terbesar (terjauh) dipakai untuk memeriksa apakah sebuah baris punya cukup kolom.

Baris data dibaca satu per satu mulai dari nomor baris 2. Baris yang kolomnya kurang dicatat ke error_log bila tidak kosong seluruhnya. Baris yang kode dan namanya sama-sama kosong dilewati. Angka wajib dan rekam dikonversi dengan baca_angka(); bila hasilnya None, baris dicatat ke error_log dan dilewati. Baris yang lolos dimasukkan ke dictionary w berisi kode, nama, wajib, rekam, kesenjangan, cakupan, kontribusi, kumulatif, dan prioritas.

Setelah dictionary dibuat, wilayah dengan wajib sama dengan 0 dicatat ke anomali_log lalu dikecualikan. Jika rekam lebih besar dari wajib, kejadian itu dicatat sebagai anomali. Kesenjangan dihitung dengan max(wajib - rekam, 0) dan cakupan dengan rekam dibagi wajib dikali 100. Kemudian kode wilayah diperiksa: jika sama dengan KODE_PROVINSI, dictionary disimpan sebagai provinsi; jika mengandung titik, ditambahkan ke daftar kabupaten/kota; selain itu dicatat sebagai error format kode.

Setelah semua baris diproses, fungsi mengembalikan error bila daftar kabupaten/kota kosong. Cakupan provinsi diambil dari baris provinsi jika ada, atau dihitung dari jumlah rekam dibagi jumlah wajib seluruh kabupaten/kota. Hasil akhirnya berupa dictionary dengan kunci daftar, provinsi, cakupan_prov, error, dan anomali.

## 4. Fungsi Pembantu

baca_angka() membersihkan teks angka: teks dipisah pada koma, ditolak (None) bila lebih dari dua bagian, titik ribuan dibuang, dan sisanya harus berupa digit. Bagian desimal hanya diterima jika semuanya nol, lalu hasilnya dikembalikan sebagai integer.

format_angka() mengubah angka menjadi teks berformat Indonesia. Angka diformat dengan pemisah ribuan koma dan desimal titik, kemudian kedua tanda itu ditukar menjadi titik untuk ribuan dan koma untuk desimal.

input_pilihan() mencetak pesan, membaca input, dan mengulang tanpa henti sampai jawaban ada di daftar pilihan yang valid.

ambil_kesenjangan() dan ambil_cakupan() hanyalah fungsi kecil yang mengembalikan nilai kunci tertentu, dipakai sebagai key pada sorted(), max(), dan min().

## 5. Perhitungan Pareto: hitung_pareto(daftar)

Daftar diurutkan dari kesenjangan terbesar dan total kesenjangan dijumlahkan. Pada setiap wilayah, program menyimpan nilai kumulatif sebelumnya, menghitung kontribusi (kesenjangan dibagi total dikali 100), lalu menambahkannya ke kumulatif. Wilayah mendapat label "Prioritas I" bila kumulatif sebelumnya masih di bawah AMBANG_PARETO dan nomor urutnya tidak melebihi BATAS_PRIORITAS_1; selain itu mendapat "Prioritas II". Karena isi daftar berupa dictionary yang sama dengan data["daftar"], nilai kontribusi, kumulatif, dan prioritas otomatis ikut tersimpan di data utama.

## 6. Menu 1: Audit Data

menu_1() mencetak jumlah wilayah valid, total wajib, total rekam, total kesenjangan, serta rata-rata dan median kesenjangan memakai modul statistics. Setelah itu log error dan log anomali dicetak, atau diberi keterangan "tidak ada" bila kosong. Bagian terakhir adalah tabel wilayah yang diurutkan dari kesenjangan terbesar.

## 7. Menu 2: Statistik

menu_2() mencari wilayah dengan kesenjangan tertinggi memakai max() dan terendah memakai min(), menghitung simpangan baku dengan statistics.pstdev(), lalu mencetak tabel belum rekam per wilayah beserta rasionya, yaitu 100 dikurangi cakupan.

## 8. Menu 3: Pareto

menu_3() menerima daftar terurut dari main(), menghitung jumlah wilayah Prioritas I dan Prioritas II, lalu memanggil cetak_pareto() untuk menampilkan tabel kesenjangan, persen kontribusi, persen kumulatif, dan prioritas.

## 9. Menu 4: Prioritas dan Cakupan Provinsi

menu_4() meminta pengguna memilih Prioritas I, Prioritas II, atau keduanya, lalu memanggil cetak_pareto() pada daftar yang sudah difilter. Setelah itu program menampilkan tabel cakupan setiap wilayah yang diurutkan dari cakupan terkecil, lengkap dengan status "Di bawah rata-rata" atau "Di atas/sama" dibandingkan cakupan provinsi.
