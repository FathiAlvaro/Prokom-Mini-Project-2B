import csv
import statistics

NAMA_FILE = "cakupan-ktp-el-sumut-kab-kota-2025.csv"
KODE_PROVINSI = "12"
BATAS_PRIORITAS_1 = 10
AMBANG_PARETO = 80.0
KOLOM_WAJIB = ["Kode Wilayah","Kabupaten/Kota","Jumlah Penduduk Wajib KTP","Perekaman KTP-EL"]