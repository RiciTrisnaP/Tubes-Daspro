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

def perbaikan_numerasi(candi):
    list_kosong = [["","","","",""] for i in range(100)]
    for i in range(100):
        if candi[i][0] != "":
            id_candi = int(candi[i][0])
            list_kosong[id_candi-1] = candi[i]
    return list_kosong

def cari_index_kosong(list,panjang_list,item_kosong,tipe="terakhir"):
    index_kosong = panjang_list
    for i in range(panjang_list):
        if list[i] == item_kosong:
            index_kosong = i
            return index_kosong
    return index_kosong


# def cari_index_kosong(list,panjang_list,item_kosong,tipe="terakhir"):
#     index_kosong_terakhir = panjang_list
#     is_terakhir = False
#     for i in range(panjang_list):
#         if list[i] == item_kosong:
#             if not is_terakhir:
#                 index_kosong_terakhir = i
#                 is_terakhir = True
#                 if tipe == "terawal":
#                     return index_kosong_terakhir
#         else:
#             is_terakhir = False
#     return index_kosong_terakhir


def cek_full(list,panjang_list,item_kosong):
    index_kosong = cari_index_kosong(list,panjang_list,item_kosong,tipe="terawal")
    if index_kosong == panjang_list:
        return True
    else:
        return False

def username_tersedia(users,username):
    for i in range(102):
        if username == users[i][0]:
            print(f'\nUsername "{username}" sudah diambil!\n')
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
        print("\nPassword panjangnya harus 5-25 karakter!\n")
        return False
    else:
        return True

def hitung_jumlah(list,panjang_list,item_kosong,spesifikasi="",index_spesifikasi=""):
    jumlah = 0
    if spesifikasi == "" or index_spesifikasi == "":
        for i in range(panjang_list):
            if list[i] != item_kosong:
                jumlah += 1
        return jumlah
    else:
        for i in range(panjang_list):
            if list[i][index_spesifikasi] == spesifikasi:
                jumlah += 1
        return jumlah

def cek_kecukupan_bahan(bahan_bangunan,pasir,batu,air):
    if int(bahan_bangunan[0][2]) >= pasir and int(bahan_bangunan[1][2]) >= batu and int(bahan_bangunan[2][2]) >= air:
        return True
    else:
        return False

def sort_leksikografis(list,panjang_list,terurut_naik=True):
    for i in range(panjang_list):
         for j in range(i+1,panjang_list):
            if terurut_naik:
                if list[i][0] > list[j][0]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
            else:
                if list[i] < list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
    return list 

def cari_index_maxmin(list,panjang_list,tipe):
        nilai_min = list[0][1]
        nilai_max = list[0][1]
        index_min = 0
        index_max = 0
        if tipe == "max":
            for i in range(panjang_list):
                if list[i][1] > nilai_max and list[i][0] != "":
                    nilai_max = list[i][1]
                    index_max = i
            return index_max
        else:
            for i in range(panjang_list):
                if list[i][1] < nilai_min and list[i][0] != "":
                    nilai_min = list[i][1]
                    index_min = i
            return index_min


def cek_sudah_terhitung(list,panjang_list,index,item):
    for i in range(panjang_list):
        if list[i][index] == item:
            return True
    return False    

def generate_list_jumlah_candi_per_jin(candi):
    list_jumlah_candi_per_jin = [["",0] for i in range(100)]
    for i in range(100):
        if not cek_sudah_terhitung(list_jumlah_candi_per_jin,100,0,candi[i][1]):
            username = candi[i][1]
            jumlah_candi = hitung_jumlah(candi,100,["","","","",""],username,1)
            index_kosong = cari_index_kosong(list_jumlah_candi_per_jin,100,["",0],tipe="terawal")
            list_jumlah_candi_per_jin[index_kosong] = [username,jumlah_candi]
    return list_jumlah_candi_per_jin

def cari_jin(candi,tipe):
    jumlah_candi = hitung_jumlah(candi,100,["","","","",""])
    if jumlah_candi != 0:
        list_jumlah_candi_per_jin = generate_list_jumlah_candi_per_jin(candi)
        if tipe == "rajin":
            list_jumlah_candi_per_jin = sort_leksikografis(list_jumlah_candi_per_jin,100,terurut_naik=True)
            index_max = cari_index_maxmin(list_jumlah_candi_per_jin,100,"max")
            return list_jumlah_candi_per_jin[index_max][0]
        else:
            list_jumlah_candi_per_jin = sort_leksikografis(list_jumlah_candi_per_jin,100,terurut_naik=False)
            index_min = cari_index_maxmin(list_jumlah_candi_per_jin,100,"min")
            return list_jumlah_candi_per_jin[index_min][0]
    else:
        return "-"
    
def generate_list_harga_candi(candi,jumlah_candi):
    list_harga_candi = [["",0] for i in range(100)]
    if jumlah_candi != 0:
        for i in range(100):
            if candi[i] != ["","","","",""]:
                list_harga_candi[i][0] = int(candi[i][0])
                list_harga_candi[i][1] = int(candi[i][2]) * 10000 + int(candi[i][3]) * 15000 + int(candi[i][4]) * 7500
        return list_harga_candi 
    else:
        return ["",0]


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