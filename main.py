from data import *
from Modules import *

users = []
candi = []
bahan_bangunan = []

users,candi,bahan_bangunan = load()

role = ""
username = ""

def commands(masukan):
    # Deklarasi global variabel untuk memodifikasi nilai variabel global
    global users
    global candi
    global bahan_bangunan
    global role
    global username

    # Perintah untuk login
    if masukan == "login":
        if role == "":
            username,role = login(users=users,role=role)
        else:
            print("Login gagal!")
            print(f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    
    # Perintah untuk logout
    elif masukan == "logout":
        role = logout(role=role)

    # Perintah untuk men-summon jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "summonjin":
        if role == "Bandung_Bondowoso":
            if hitung_jin(users) > 100:
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            else:
                users = summonjin(users=users)
        else:
            print("Maaf Anda tidak memiliki akses")

    # Perintah untuk menghilangkan jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "hapusjin":
        if role == "Bandung_Bondowoso":
            users = hapusjin(users)
        else:
            print("Maaf Anda tidak memiliki akses")

    # Perintah untuk mengubah tipe jin
    # Akses hanya untuk Bandung Bondowoso
    elif masukan == "ubahjin":
        if role == "Bandung_Bondowoso":
            users = ubahjin(users=users)
        else:
            print("Maaf Anda tidak memiliki akses")
    
    #Perintah untuk menyimpan data saat ini
    elif masukan == 'save':
        folder = input('Masukan nama folder: ')
        save(users,folder,'user.csv')
        save(candi,folder,'candi.csv')
        save(bahan_bangunan,folder,'bahan_bangunan.csv')

    # Perintah untuk meminta bantuan
    elif masukan == "help":
        help(role)

    # Perintah untukl keluar program
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
