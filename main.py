# Mengimport Fungsi.py dan Modules.py
from Fungsi import *
from Modules import *
import time

# Menginisiasi array of array users,candi, dan bahan_bangunan
users = [["","",""] for i in range(102)]
candi = [["","","","",""] for i in range(100)]
bahan_bangunan = [["","",""] for i in range(3)]

# Mengambil nilai seed untuk Random Number Generator
seed = time.time_ns()

# Mengambil data dari CSV pada folder yang telah disediakan pengguna
users,candi,bahan_bangunan = load(users,candi,bahan_bangunan)

# Menginisiasi variabel string role dan username dengan nilai ""
# "" pada role dan username menandakan users belum login
role = ""
username = ""

# Mendefinisikan fungsi commands
def commands(masukan):
    # Deklarasi global variabel agar nilai variabel dapat dimodifikasi di scope manapun
    global users
    global candi
    global bahan_bangunan
    global role
    global username
    global seed

    # Perintah untuk login
    if masukan == "login":
        if role == "":
            username,role = login(users=users,role=role)
        else:
            print("Login gagal!")
            print(f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.\n")
    
    # Perintah untuk logout
    elif masukan == "logout":
        role = logout(role=role)

    # Perintah untuk men-summon jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "summonjin":
        if role == "Bandung_Bondowoso":
            users = summonjin(users=users)
        else:
            print("Maaf Anda tidak memiliki akses\n")

    # Perintah untuk menghilangkan jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "hapusjin":
        if role == "Bandung_Bondowoso":
            users,candi = hapusjin(users,candi)
        else:
            print("Maaf Anda tidak memiliki akses\n")

    # Perintah untuk mengubah tipe jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "ubahjin":
        if role == "Bandung_Bondowoso":
            users = ubahjin(users=users)
        else:
            print("Maaf Anda tidak memiliki akses\n")
    
    # Perintah untuk melakukan pembangunan bagi jin pembangun
    elif masukan == "bangun":
        if role == "Jin Pembangun":
            seed,candi,bahan_bangunan = bangun(candi,bahan_bangunan,username,seed)
        else:
            print("Maaf Anda tidak memiliki akses\n")

    # Perintah untuk mencari bahan bangunan bagi jin pengumpul
    elif masukan == "kumpul":
        if role == "Jin Pengumpul":
            seed,bahan_bangunan = kumpul(bahan_bangunan,seed)
        else:
            print("Maaf Anda tidak memiliki akses\n")

    # Perintah mengerahkan semua jin pembangun untuk melakukan bangun
    elif masukan == "batchbangun":
        if role == "Bandung_Bondowoso":
            seed,candi,bahan_bangunan = batchbangun(users,candi,bahan_bangunan,seed)
        else:
            print("Maaf Anda tidak memiliki akses\n")

    # Perintah mengerahkan semua jin pengumpul untuk mengumpulkan bahan pembuatan candi
    elif masukan == "batchkumpul":
        if role == "Bandung_Bondowoso":
            seed,bahan_bangunan = batchkumpul(users,bahan_bangunan,seed)
        else:
            print("Maaf Anda tidak memiliki akses\n")

    # Perintah untuk menampilkan laporan jin
    elif masukan == "laporanjin":
        if role == "Bandung_Bondowoso":
            laporanjin(users,candi,bahan_bangunan)
        else:
            print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")

    # Perintah untuk menampilkan laporan candi
    elif masukan == "laporancandi":
        if role == "Bandung_Bondowoso":
            laporancandi(candi)
        else:
            print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.\n")
    
    # Perintah untuk menghancurkan candi
    # Akses : Roro Jonggrang
    elif masukan == "hancurkancandi":
        if role == "Roro_Jonggrang":
            candi = hancurkancandi(candi)
        else:
            print("Penghancuran candi hanya dapat dilakukan oleh Roro Jonggrang")
    
    # Perintah untuk mengakhiri pembangunan candi
    elif masukan == "ayamberkokok":
        if role == "Roro_Jonggrang":
            ayamberkokok(candi)
        else:
            print("Ayam hanya bisa berkokok apabila diperintah Roro Jonggrang!")

    # Perintah untuk menyimpan data saat ini
    elif masukan == 'save':
        folder = input('Masukan nama folder: ')
        print("Saving...")
        save(users,102,3,folder,'user.csv')
        save(candi,100,5,folder,'candi.csv')
        save(bahan_bangunan,3,3,folder,'bahan_bangunan.csv')
        print(f"Berhasil menyimpan data di folder save/{folder}!\n") 

    # Perintah untuk meminta bantuan
    elif masukan == "help":
        help(role)

    # Perintah untuk keluar program
    elif masukan == "exit":
        exit(users,candi,bahan_bangunan)
    
    elif masukan == "users":
        print(users)
    elif masukan == "candi":
        print(candi)
    elif masukan == "bahan_bangunan":
        print(bahan_bangunan)
    elif masukan == "role":
        print(role)
    else:
        print("Maaf perintah tidak dikenal\n")


while True:
    masukan = input(">>> ")
    commands(masukan)
