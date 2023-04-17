from data import *
from Modules import *

users = []
candi = []
bahan_bangunan = []

users = csv_toarray('Struktur_data_eksternal\\user.csv',separator=';')
candi = csv_toarray('Struktur_data_eksternal\\candi.csv',separator=';')
bahan_bangunan = csv_toarray('Struktur_data_eksternal\\bahan_bangunan.csv',separator=';')

role = ""
username = ""

def commands(masukan):
    # Deklarasi global variabel untuk memodifikasi nilai variabel global
    global users
    global candi
    global bahan_bangunan
    global role
    global username

    # Perintah login
    if masukan == "login":
        if role == "":
            username,role = login(users=users,role=role)
        else:
            print("Login gagal!")
            print(f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    
    # Perintah logout
    elif masukan == "logout":
        role = logout(role=role)

    # Perintah summon jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "summonjin":
        if role == "Bandung_Bondowoso":
            if hitung_jin(users) > 100:
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            else:
                users = summonjin(users=users)
        else:
            print("Maaf Anda tidak memiliki akses")

    # Perintah ubah tipe jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "ubahjin":
        if role == "Bandung_Bondowoso":
            users = ubahjin(users=users)
        else:
            print("Maaf Anda tidak memiliki akses")
            
    # Perintah keluar program
    elif masukan == "exit":
        exit()

    elif masukan == "users":
        print(users)
    elif masukan == "role":
        print(role)
    else:
        print("Maaf perintah tidak dikenal")


while True:
    masukan = input(">>> ")
    commands(masukan)
