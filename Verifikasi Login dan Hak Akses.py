admin_user = "Phanes"
admin_pass = 454635
reg_user = "Pauline"
reg_pass = 306748

print("   ================================")
print("=== Verifikasi Login dan Hak Akses ===")
print("   ================================")
print("Selamat datang di sistem login")
print("Silakan masukkan username dan password Anda")
username = input("Masukkan username: ")
password = int(input("Masukkan password: "))

# Mengecek apakah username dan password sesuai dengan akun yang terdaftar
if username == admin_user and password == admin_pass or username == reg_user and password == reg_pass:
    print("Login Berhasil")

# Meminta pengguna untuk memasukkan level akses
    access_level = input("Masukkan level akses (admin/user): ")

# Mengecek apakah level akses sesuai dengan username yang digunakan
    if access_level == "admin" and username == admin_user:
        print(f"Selamat datang Admin ({admin_user})")

# Mengecek akses user biasa
    elif access_level == "user" and username == reg_user:
        print(f"Selamat datang User ({reg_user})")

# Menolak level akses yang tidak sesuai dengan username
    else:
        print("Hak akses tidak sesuai dengan username")

# Menolak login jika username dan password tidak sesuai
else:
    print("Login Gagal")

