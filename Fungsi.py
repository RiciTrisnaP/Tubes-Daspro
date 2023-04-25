from Modules import *
import sys
import os
import argparse

def login(users,role):
    username = input("Username: ")
    password = input("Password: ")
    for i in range(102):
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
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return role

def summonjin(users):
    print("""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi""")
    jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")

    if jenis_jin == "1":
        print(f'Memilih jin "Pengumpul"')
        role_jin = "Jin Pengumpul"
    elif jenis_jin == "2":
        print(f'Memilih jin "Pembangun"')
        role_jin = "Jin Pembangun"

    username_jin = input("Masukkan username jin: ")
    while username_tersedia(users,username_jin) != True:
        username_jin = input("Masukkan username jin: ")

    password_jin = input("Masukkan password jin: ")
    while validasi_password(password_jin) != True:
        password_jin = input("Masukkan password jin: ")

    is_full = cek_full(users,102,["","",""])
    if not is_full:
        index_kosong_terakhir = cari_index_kosong_terakhir(users,102,["","",""])
        users[index_kosong_terakhir] = [username_jin,password_jin,role_jin]
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username_jin} berhasil dipanggil!")
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    return users
        
def hapusjin(users,candi):
    username_jin = input("Masukkan username jin: ")
    is_valid,index_username_jin = validasi_username(users,username_jin)
    if is_valid:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)?")
        if konfirmasi == "Y":
            users[index_username_jin] = ["","",""]
            for i in range(100):
                if candi[i][1] == username_jin:
                    candi[i][1] == ["","","","",""]
            print("Jin telah berhasil dihapus dari alam gaib.")
        elif konfirmasi == "N":
            print("Penghapusan jin dibatalkan.")
        else:
            print("Perintah tidak dikenali, penghapusan jin dibatalkan.")
    else:
        print("Tidak ada jin dengan username tersebut.")
    return users,candi
    
def ubahjin(users):
    username_jin = input("Masukkan username jin: ")
    is_valid,index_username_jin = validasi_username(users,username_jin)
    if is_valid:
        if users[index_username_jin][2] == "Jin Pengumpul":
            opsi_ganti_jenis_jin = "Jin Pembangun"
        else:
            opsi_ganti_jenis_jin = "Jin Pengumpul"
        print(f'Jin ini bertipe "{users[index_username_jin][2]}". Yakin ingin mengubah ke tipe "{opsi_ganti_jenis_jin}" ')
        konfirmasi = input("(Y/N)? ")
        if konfirmasi == "Y":
            users[index_username_jin][2] = opsi_ganti_jenis_jin
            print("Jin telah berhasil diubah.")
        elif konfirmasi == "N":
            print("Perubahan jin dibatalkan")
        else:
            print("Perintah tidak dikenali, perubahan jin dibatalkan")
    else:
        print("Tidak ada jin dengan username tersebut.")
    return users

def bangun(candi,bahan_bangunan,username,seed=time.time_ns(),repeat=False):
    pasir,batu,air,seed  = random_bahan(seed,True)
    is_bahan_cukup = cek_kecukupan_bahan(bahan_bangunan,pasir,batu,air)
    list_pembangunan = ["","","","",""]
    if is_bahan_cukup:
        is_full = cek_full(candi,100,["","","","",""])
        if not is_full:
            list_pembangunan = ["",username,pasir,batu,air]
        if not repeat:
            index_kosong_terakhir = cari_index_kosong_terakhir(candi,100,["","","","",""])
            candi[index_kosong_terakhir] = list_pembangunan
            bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - pasir
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - batu
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - air
            print("Candi berhasil dibangun.")
            jumlah_candi = hitung_jumlah(candi,100,["","","","",""])
            print(f"Sisa candi yang perlu dibangun: {100-jumlah_candi}")
            return candi,bahan_bangunan
    else:
        if not repeat:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
            return candi,bahan_bangunan
    return seed,list_pembangunan

def kumpul(bahan_bangunan,seed=time.time_ns(),repeat=False):
    pasir,batu,air,seed = random_bahan(seed,repeat=True)
    bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) + pasir
    bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) + batu
    bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) + air
    if not repeat:
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
        return bahan_bangunan
    else:
        return bahan_bangunan,pasir,batu,air,seed

def batchbangun(users,candi,bahan_bangunan):
    seed = time.time_ns()
    jumlah_jin_pembangun = 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    list_pembangunan = ["","","","",""]
    matriks_pembangunan = [["","","","",""] for i in range(100)]
    for i in range(102):
        if users[i][2] == "Jin Pembangun":
            seed,list_pembangunan = bangun(candi,bahan_bangunan,users[i][0],seed,repeat=True)
            index_kosong_terakhir = cari_index_kosong_terakhir(matriks_pembangunan,100,["","","","",""])
            matriks_pembangunan[index_kosong_terakhir] = list_pembangunan
            jumlah_jin_pembangun += 1
    if jumlah_jin_pembangun != 0:
        for i in range(jumlah_jin_pembangun):
            total_pasir += matriks_pembangunan[i][2]
            total_batu += matriks_pembangunan[i][3]
            total_air += matriks_pembangunan[i][4]
        print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, {total_air} air.")
        is_bahan_cukup = cek_kecukupan_bahan(bahan_bangunan,total_pasir,total_batu,total_air)
        if is_bahan_cukup:
            bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - total_pasir
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - total_batu
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - total_air
            for i in range(cari_index_kosong_terakhir(matriks_pembangunan,100,["","","","",""])):
                index_kosong_terakhir = cari_index_kosong_terakhir(candi,100,["","","","",""])
                matriks_pembangunan[i][0] = index_kosong_terakhir+1 
                candi[index_kosong_terakhir] = matriks_pembangunan[i]
            print(f"Jin berhasil membangun total {jumlah_jin_pembangun} candi.")
        else:
            string_pasir = f'{ total_pasir - int(bahan_bangunan[0][2])} pasir' if int(bahan_bangunan[0][2]) < total_pasir else ""
            string_batu = f'{total_batu - int(bahan_bangunan[1][2])} batu' if int(bahan_bangunan[1][2]) < total_batu else ""
            string_air = f'{total_air - int(bahan_bangunan[2][2])} air' if int(bahan_bangunan[2][2]) < total_air else ""
            if string_pasir != "":
                if string_batu != "":
                    if string_air != "":
                        string_akhir = f'Kurang {string_pasir}, {string_batu}, dan {string_air}.'
                    else:
                        string_akhir = f'Kurang {string_pasir}, dan {string_batu}.'
                else:
                    if string_air != "":
                        string_akhir = f'Kurang {string_pasir} dan {string_air}.'
                    else:
                        string_akhir = f'Kurang {string_pasir}.'
            else:
                if string_batu != "":
                    if string_air != "":
                        string_akhir = f'Kurang {string_batu} dan {string_air}.'
                    else:
                        string_akhir = f'Kurang {string_batu}.'
                else:
                    if string_air != "":
                        string_akhir = f'Kurang {string_air}.'
            print(string_akhir)
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    return candi,bahan_bangunan

def batchkumpul(users,bahan_bangunan):
    seed = time.time_ns()
    total_pasir = 0
    total_batu = 0
    total_air = 0
    jumlah_jin_pengumpul = 0
    for i in range(102):
        if users[i][2] == "Jin Pengumpul":
            bahan_bangunan,pasir,batu,air,seed = kumpul(bahan_bangunan,seed,repeat=True)
            total_pasir += pasir
            total_batu += batu
            total_air += air
            jumlah_jin_pengumpul += 1
    if jumlah_jin_pengumpul != 0:
        print(f"Mengerahkan {jumlah_jin_pengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
    return bahan_bangunan

def laporanjin():
    pass

def laporancandi():
    pass

def hancurkancandi():
    pass

def ayamberkokok():
    pass

def load(users,candi,bahan_bangunan):
    parser = argparse.ArgumentParser(usage="python main.py <nama_folder>") 
    parser.add_argument("path")
    if len(sys.argv)==1:
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args=parser.parse_args()

    if os.path.exists(args.path):  
        print("Loading...")
        users=csv_toarray(users,f"{args.path}\\user.csv",separator=';')
        candi=csv_toarray(candi,f"{args.path}\\candi.csv",separator=';')
        bahan_bangunan=csv_toarray(bahan_bangunan,f"{args.path}/bahan_bangunan.csv",separator=';')
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda") 
        return users,candi,bahan_bangunan
    else:
        print(f"Folder “{args.path}” tidak ditemukan.")
        sys.exit(1)


def save(file,panjang_file,panjang_sub_item,folder,filename):
    if 'save' not in os.listdir():
        os.mkdir('save')
    if folder not in os.listdir('save\\'):
        os.mkdir(f'save\\{folder}')
    f = open(f'save\\{folder}\\{filename}', 'w')
    if panjang_file == 102:
        f.write("username;password;role\n")
    elif panjang_file == 100:
        f.write("id;pembuat;pasir;batu;air\n")
    elif panjang_file == 3:
        f.write("nama;deskripsi;jumlah\n")
    for i in range(panjang_file):
        kosong = False
        for j in range(panjang_sub_item):
            if file[i] == ["" for i in range(panjang_sub_item)]:
                kosong = True
                break
            elif j != panjang_sub_item-1:
                f.write(f'{file[i][j]};')
            else:
                f.write(f'{file[i][j]}')
        if i != panjang_file-1 and not kosong:
            f.write('\n')    
    f.close()

def help(role):
    print('=========== HELP ===========')
    if role == 'Bandung_Bondowoso':
        print('1.  logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print('2.  summonjin\n    Untuk memanggil jin')
    elif role == 'Roro_Jonggrang':
        print('1.  logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print('2.  hancurkancandi\n    Untuk menghancurkan candi yang tersedia')
    elif role == 'Jin Pengumpul':
        print('1.  logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print('2.  kumpul\n    Untuk mengumpulkan resource candi')
    elif role == 'Jin Pembangun':
        print('1.  logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print('2.  bangun\n    Untuk membangun candi')
    else:
        print('1.   login\n     Untuk masuk menggunakan akun')
        print('2.   exit\n     Untuk keluar dari akun')

def exit():
    sys.exit(1)

# BONUS

def undo(stack_list):
    pass
