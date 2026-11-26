def input_pilihan(pesan, pilihan_valid):
    while True:
        jawaban = input(pesan).strip()
        if jawaban in pilihan_valid:
            return jawaban
        print(f"[INPUT SALAH] Pilih salah satu dari: {', '.join(pilihan_valid)}")