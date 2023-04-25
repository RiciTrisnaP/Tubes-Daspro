import time

def csv_toarray(list,csv,separator):
    file = open(csv,"r")
    index = -1
    for line in file:
        if index == -1:
            index += 1
        else:
            sub_index = 0
            container = ""
            for i in range(len(line)):
                if line[i] == separator or line[i] == "\n":
                    list[index][sub_index] = container
                    sub_index += 1
                    container = ""
                else:
                    container += line[i]
            if container != "":
                list[index][sub_index] = container
            index += 1
    return list

def cari_index_kosong_terakhir(list,panjang_list,item_kosong):
    index_kosong_terakhir = panjang_list
    is_terakhir = False
    for i in range(panjang_list):
        if list[i] == item_kosong:
            if not is_terakhir:
                index_kosong_terakhir = i
                is_terakhir = True
        else:
            is_terakhir = False
    return index_kosong_terakhir


def cek_full(list,panjang_list,item_kosong):
    index_kosong_terakhir = cari_index_kosong_terakhir(list,panjang_list,item_kosong)
    if index_kosong_terakhir == panjang_list:
        return True
    else:
        return False

def username_tersedia(users,username):
    for i in range(102):
        if username == users[i][0]:
            print(f'Username "{username}" sudah diambil!')
            return False
    return True

def validasi_username(users,username):
    for i in range(102):
        if username == users[i][0]:
            index = i
            return True,index
    return False,""

def validasi_password(password):
    if len(password) < 5 or len(password) > 25:
        print("Password panjangnya harus 5-25 karakter!")
        return False
    else:
        return True

def hitung_jumlah(list,panjang_list,item_kosong):
    jumlah = 0
    for i in range(panjang_list):
        if list[i] != item_kosong:
            jumlah += 1
    return jumlah

def cek_kecukupan_bahan(bahan_bangunan,pasir,batu,air):
    if int(bahan_bangunan[0][2]) >= pasir and int(bahan_bangunan[1][2]) >= batu and int(bahan_bangunan[2][2]) >= air:
        return True
    else:
        return False

# Bonus
def random_number_generator(first_number,last_number,seed):
    a = 75
    c = 74
    m = 65537
    number = (a*seed+c) % m
    number_on_range = number % (last_number - first_number + 1) + first_number
    return number_on_range,number

def random_bahan(seed,repeat=False):
    seed_1 = seed
    pasir,seed_2 = random_number_generator(1,5,seed_1)
    batu,seed_3= random_number_generator(1,5,seed_2)
    air,seed_4 = random_number_generator(1,5,seed_3)
    if repeat:
        return pasir,batu,air,seed_4
    else:
        return pasir,batu,air
