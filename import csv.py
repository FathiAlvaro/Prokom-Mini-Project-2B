import csv

nama_file = 'cakupan-ktp-el-sumut-kab-kota-2025 (1).csv'

with open (nama_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)