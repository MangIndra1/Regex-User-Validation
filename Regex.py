import re

# Validasi Email
def validasi_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})*$'
    return re.match(email_pattern, email) is not None

# Validasi Nomor Telepon
def validasi_telepon(telepon):
    telepon_pattern = r'^(\+62|08)[0-9]{8,12}$'
    return re.match(telepon_pattern, telepon) is not None

# Validasi Kata Sandi
def validasi_password(password):
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(password_pattern, password) is not None

print("\nPROGRAM IMPLEMENTASI REGEX")
print("==========================")
# Meminta input dari pengguna
def minta_email():
    while True:
        email = input("Masukkan email Anda\t\t: ")
        if validasi_email(email):
            print("Email valid")
            return email
        else:
            print("Email tidak valid, silakan coba lagi.")

def minta_telepon():
    while True:
        telepon = input("Masukkan nomor telepon Anda\t: ")
        if validasi_telepon(telepon):
            print("Nomor telepon valid")
            return telepon
        else:
            print("Nomor telepon tidak valid, silakan coba lagi.")

def minta_password():
    while True:
        password = input("Masukkan kata sandi Anda\t: ")
        if validasi_password(password):
            print("Kata sandi valid")
            return password
        else:
            print("Kata sandi tidak valid, silakan coba lagi. \n1. Pastikan minimal 8 karakter\n2. Mengandung huruf besar, kecil, angka, dan simbol.")

# Meminta input dari pengguna dengan validasi
email = minta_email()
telepon = minta_telepon()
password = minta_password()

print("\nSemua data berhasil divalidasi!")
