from Modules import *
import sys

def login(users,role):
    username = input("Username: ")
    password = input("Password: ")
    for i in range(1,length(users)):
        if users[i][0] == username:
            if users[i][1] == password:
                role = users[i][2]
                print(f"Selamat datang, {users[i][0]}!")
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                return username,role
            else:
                print("Password salah!")
                return "",""
    print("Username tidak terdaftar!")
    return "",""

def logout(role):
    if role != "":
        role = ""
        print("Keluar dari akun")
        return role
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return role

def summonjin(users):
    print("""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi""")
    jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
    opsi_jenis_jin_angka = ["1","2"]
    opsi_jenis_jin = ["Pengumpul","Pembangun"]
    if is_part_of(jenis_jin,opsi_jenis_jin_angka) == False:
        print(f'Tidak ada jenis jin yang bernomor "{jenis_jin}"')
        return users
    else:
        print(f'Memilih jin "{opsi_jenis_jin[int(jenis_jin)-1]}"')
        role_jin = opsi_jenis_jin[int(jenis_jin)-1]

        username_jin = input("Masukkan username jin: ")
        while validasi_username_1(users,username_jin) != True:
            username_jin = input("Masukkan username jin: ")

        password_jin = input("Masukkan password jin: ")
        while validasi_password(password_jin) != True:
            password_jin = input("Masukkan password jin: ")

    users = add(users,[username_jin,password_jin,role_jin])
    return users
        
def hapusjin():
    pass

def ubahjin(users):
    username_jin = input("Masukkan username jin: ")
    is_valid,index_username_jin = validasi_username_2(users,username_jin)
    if is_valid:
        if users[index_username_jin][2] == "Pengumpul":
            opsi_ganti_jenis_jin = "Pembangun"
        else:
            opsi_ganti_jenis_jin = "Pengumpul"
        print(f'Jin ini bertipe "{users[index_username_jin][2]}". Yakin ingin mengubah ke tipe "{opsi_ganti_jenis_jin}" ')
        konfirmasi = input("(Y/N)? ")
        if konfirmasi == "Y":
            users[index_username_jin][2] = opsi_ganti_jenis_jin
            print("Jin telah berhasil diubah.")
            return users
        elif konfirmasi == "N":
            print("Perubahan jin dibatalkan")
            return users
        else:
            print("Perintah tidak dikenali, perubahan jin dibatalkan")
            return users
    else:
        print("Tidak ada jin dengan username tersebut.")
        return users

def bangun():
    pass

def kumpul():
    pass

def batchkumpul():
    pass

def laporanjin():
    pass

def laporancandi():
    pass

def hancurkancandi():
    pass

def ayamberkokok():
    pass

def load():
    pass

def save():
    pass

def help():
    pass

def exit():
    sys.exit(1)