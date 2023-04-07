from Modules import *

opsi_jenis_jin = ["Pengumpul","Pembangun"]

def login(users,login_status,username):
    if login_status == False:
        username = input("Username: ")
        password = input("Password: ")
        is_username_true = False
        is_password_true = False
        username_index = 0
        for i in range(length(users)):
            if users[i][0] == username:
                is_username_true = True
                username_index = i
        for i in range(length(users)):
            if users[i][1] == password:
                is_password_true = True
        if is_username_true and is_password_true:
            login_status = True
            print(f"Selamat datang, {users[username_index][0]}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            return username,login_status
        elif is_username_true == False:
            print("Username tidak terdaftar")
            username = ""
            return username,login_status
        else:
            print("Password salah!")
            username = ""
            return username,login_status
    else:
        print("Anda sudah login, silakan logout terlebih dahulu")
        return username,login_status
    

def logout(login_status):
    if login_status == True:
        login_status = False
        print("Keluar dari akun")
        return login_status
    else:
        print("Maaf Anda belum login")
        return login_status

def summonjin(users,username):
    if username == "Bandung":
        print("""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi""")
        jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        opsi_jenis_jin_angka = ["1","2"]
        if is_part_of(jenis_jin,opsi_jenis_jin_angka) == False:
            print(f'Tidak ada jenis jin yang bernomor "{jenis_jin}"')
            new_username = ""
            new_password = ""
            role_jin = ""
            return new_username,new_password,role_jin
        else:
            print(f'Memilih jin "{opsi_jenis_jin[int(jenis_jin)-1]}"')
            role_jin = opsi_jenis_jin[int(jenis_jin)-1]
            loop = True
            while loop == True:
                new_username = input("Masukkan username jin: ")
                counter = 0
                for i in range(length(users)):
                    if new_username == users[i][0]:
                        print(f'Username "{new_username}" sudah diambil!')
                    elif counter == length(users)-1:
                        loop = False
                    else:
                        counter += 1

            loop = True
            while loop == True:
                new_password = input("Masukkan password jin: ")
                if length(new_password) < 5 or length(new_password) > 25:
                    print("Password panjangnya harus 5-25 karakter!")
                else:
                    loop = False
            return new_username,new_password,role_jin
        
    else:
        print("Maaf Anda tidak memiliki akses")
        new_username = ""
        new_password = ""
        role_jin = ""
        return new_username,new_password,role_jin

def hapusjin():
    pass

def ubahjin(users,username):
    if username == "Bandung":
        username = input("Masukkan username jin: ")
        counter = 0
        for i in range(length(users)):
            if username == users[i][0]:
                if users[i][2] == "Pengumpul":
                    opsi_ganti_jenis_jin = "Pembangun"
                else:
                    opsi_ganti_jenis_jin = "Pengumpul"
                print(f'Jin ini bertipe "{users[i][2]}". Yakin ingin mengubah ke tipe "{opsi_ganti_jenis_jin}" ')
                konfirmasi = input("(Y/N)? ")
            elif counter == length(users)-1:
                print("Tidak ada jin dengan username tersebut.")
            else:
                counter += 1

    else:
        print("Maaf Anda tidak memiliki akses")

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
    pass