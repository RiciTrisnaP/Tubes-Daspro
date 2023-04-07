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
        new_username, new_password,role_jin = summonjin(users=users,username=username)
        if new_username != "" and new_password != "" and role_jin != "":
            users = add(users,[new_username,new_password,role_jin])
    elif masukan == "ubahjin":
        ubahjin(users=users,username=username)
    elif masukan == "users":
        print(users)
    else:
        print("Maaf perintah tidak dikenal")