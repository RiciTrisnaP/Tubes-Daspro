from data import *
from Modules import *

users = []
candi = []
bahan_bangunan = []

users = csv_toarray('Struktur_data_eksternal\\user.csv',separator=';')
candi = csv_toarray('Struktur_data_eksternal\\candi.csv',separator=';')
bahan_bangunan = csv_toarray('Struktur_data_eksternal\\bahan_bangunan.csv',separator=';')

login_status = False
username = ""

while True:
    masukan = input(">>> ")
    if masukan == "login":
        username,login_status = login(users=users,login_status=login_status,username=username)
    elif masukan == "logout":
        login_status = logout(login_status=login_status)
        username = ""
    elif masukan == "summonjin":
        username_jin, password_jin,role_jin = summonjin(users=users,username=username)
        if username_jin != "" and password_jin != "" and role_jin != "":
            users = add(users,[username_jin,password_jin,role_jin])
    elif masukan == "ubahjin":
        username_jin,opsi_ganti_jenis_jin = ubahjin(users=users,username=username)
        if username_jin != "" and opsi_ganti_jenis_jin != "":
            for i in range(length(users)):
                if username_jin == users[i][0]:
                    index_jin = i
            users[index_jin][2] = opsi_ganti_jenis_jin
            (print("Jin telah berhasil diubah."))
    elif masukan == "users":
        print(users)
    else:
        print("Maaf perintah tidak dikenal")