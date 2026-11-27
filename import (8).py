class Akun:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def cocok(self, username, password):
        return self.username == username and self.password == password

DAFTAR_AKUN = [Akun("miniproject2B", "prokom2026")]

def login():
    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        for akun in DAFTAR_AKUN:
            if akun.cocok(username, password):
                print(f"Login berhasil. Selamat datang, {akun.username}.")
                return
        print("[LOGIN GAGAL] Username atau password salah.")
