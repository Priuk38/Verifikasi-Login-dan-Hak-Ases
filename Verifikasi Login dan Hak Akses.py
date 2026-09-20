admin_user = "Phanes"
admin_pass = 454635
reg_user = "Pauline"
reg_pass = 306748

username = input("Masukkan username: ")
password = int(input("Masukkan password: "))
if username == admin_user and password == admin_pass or username == reg_user and password == reg_pass:
    print("Login Berhasil")
    access_level = input("Masukkan level akses (admin/user): ")
    if access_level == "admin" and username == admin_user:
        print("Selamat datang Admin")
    elif access_level == "user" and username == reg_user:
        print("Selamat datang User")
    else:
        print("Hak akses tidak sesuai dengan username")
else:
    print("Login Gagal")

