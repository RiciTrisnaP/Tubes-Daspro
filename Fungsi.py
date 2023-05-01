from Modules import *
import sys
import os
import argparse

# F01  
def login(users,role):
    username = input("Username: ")
    password = input("Password: ")
    for i in range(102): # Mengecek setiap instance dalam users
        if users[i][0] == username: # Mengecek apakah username yang dimasukan terdaftar pada database users
            if users[i][1] == password: # Mengecek apakah password benar dan sesuai dengan username
                role = users[i][2]
                print(f"\nSelamat datang, {users[i][0]}!")
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.\n')
                return username,role
    # Jika tidak maka role dan username tetep ""
            else: 
                print("\nPassword salah!\n")
                return "",""
    print("\nUsername tidak terdaftar!\n")
    return "",""

# F02 
def logout(role):
    if role != "": # Apabila sudah login maka role diubah menjadi ""
        role = ""
        print("") 
        # Keluar dari akun
    else: # Apabila belum login maka role tidak berubah
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout\n")
    return role

# F03
def summonjin(users):
    print("""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membangun candi""")
    jenis_jin = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")

    if jenis_jin == "1": # Apabila memilih 1 maka role jin adalah jin pengumpul
        print(f'\nMemilih jin "Pengumpul"')
        role_jin = "Jin Pengumpul"
    elif jenis_jin == "2": # Apabila memilih 2 maka role jin adalah jin pembangun
        print(f'\nMemilih jin "Pembangun"')
        role_jin = "Jin Pembangun"
    else: # Apabila memilih selain 1 dan 2 maka fungsi akan berhenti dan return users seperti keadaan awal
        print(f"\nTidak ada jenis jin bernomor {jenis_jin}\n")
        return users

    username_jin = input("\nMasukkan username jin: ")
    while username_tersedia(users,username_jin) != True: # Mengecek ketersediaan username
        username_jin = input("Masukkan username jin: ")

    password_jin = input("Masukkan password jin: ")
    while validasi_password(password_jin) != True: # Mengecek kevalidan password
        password_jin = input("Masukkan password jin: ")

    is_full = cek_full(users,102,["","",""]) 
    if not is_full: # Apabila users belum full maka tambahkan jin ke dalam users
        index_kosong = cari_index_kosong(users,102,["","",""])
        users[index_kosong] = [username_jin,password_jin,role_jin]
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username_jin} berhasil dipanggil!\n")
    else: # Apabila jin sudah berjumlah 100 (sudah full) maka return users seperti keadaan awal
        print("\nJumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu\n")
    return users

# F04
def hapusjin(users,candi):
    username_jin = input("Masukkan username jin: ")
    is_valid,index_username_jin = validasi_username(users,username_jin) # Mengecek kevalidan username jin sekaligus mencari index username jin pada matriks users
    if is_valid: # Apabila username valid
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)?")
        if konfirmasi == "Y": # Apabila dikonfirmasi
            users[index_username_jin] = ["","",""] # Menghapus entry jin yang dihapus pada users
            for i in range(100):
                if candi[i][1] == username_jin: # Menghapus semua entry candi oleh jin yang dihapus
                    candi[i] = ["","","","",""]
            print("\nJin telah berhasil dihapus dari alam gaib.\n")
        elif konfirmasi == "N": # Apabila dibatalkan
            print("\nPenghapusan jin dibatalkan.\n")
        else: # Apabila konfirmasi bukan Y atau N
            print("\nPerintah tidak dikenali, penghapusan jin dibatalkan.\n")
    else: # Apabila username tidak valid
        print("\nTidak ada jin dengan username tersebut.\n")
    return users,candi

# F05
def ubahjin(users):
    username_jin = input("Masukkan username jin: ")
    is_valid,index_username_jin = validasi_username(users,username_jin)  # Mengecek kevalidan username jin sekaligus mencari index username jin pada matriks users
    if is_valid: # Apabila username valid
        if users[index_username_jin][2] == "Jin Pengumpul": # Apabila jin pengumpul ganti ke jin pembangun dan sebaliknya
            opsi_ganti_jenis_jin = "Jin Pembangun" 
        else:
            opsi_ganti_jenis_jin = "Jin Pengumpul"
        print(f'Jin ini bertipe "{users[index_username_jin][2]}". Yakin ingin mengubah ke tipe "{opsi_ganti_jenis_jin}?" ')
        konfirmasi = input("(Y/N)? ")
        if konfirmasi == "Y": # Apabila dikonfirmasi maka ganti jenis jin
            users[index_username_jin][2] = opsi_ganti_jenis_jin
            print("\nJin telah berhasil diubah.\n")
        elif konfirmasi == "N": # Apabila dibatalkan maka tidak diganti
            print("\nPerubahan jin dibatalkan\n")
        else: # Apabila tidak dikenali maka dibatalkan
            print("\nPerintah tidak dikenali, perubahan jin dibatalkan\n")
    else: # Apabila username tidak valid maka tidak bisa diganti
        print("\nTidak ada jin dengan username tersebut.\n")
    return users

# F06
def bangun(candi,bahan_bangunan,username,seed,repeat=False):
    pasir,batu,air,seed  = random_bahan(seed,True) # Mengenerate jumlah pasir batu dan air secara random
    is_bahan_cukup = cek_kecukupan_bahan(bahan_bangunan,pasir,batu,air) # Mengecek kecukupan bahan pembangunan
    list_pembangunan = ["","","","",""]
    if is_bahan_cukup or repeat: # Apabila bahan cukup atau merupakan prosedur batch bangun 
        is_full = cek_full(candi,100,["","","","",""])
        if not is_full: # Apabila candi belum 100
            list_pembangunan = ["",username,pasir,batu,air]
        if not repeat: # Apabila bukan prosedur batch bangun
            # Apabila list_pembangunan tidak kosong maka masukkan ke entry candi
            if list_pembangunan != ["","","","",""]:
                # Menambahkan candi yang dibangun ke dalam matriks candi
                index_kosong = cari_index_kosong(candi,100,["","","","",""])
                list_pembangunan[0] = index_kosong+1
                candi[index_kosong] = list_pembangunan
                # Mengurangi bahan sesuai bahan yang diperlukan
                bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - pasir
                bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - batu
                bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - air
            print("Candi berhasil dibangun.")
            jumlah_candi = hitung_jumlah(candi,100,["","","","",""])
            print(f"Sisa candi yang perlu dibangun: {100-jumlah_candi}\n")
            return seed,candi,bahan_bangunan
    else: # Apabila bahan tidak cukup dan bukan repeat
        if not repeat:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!\n")
            return seed,candi,bahan_bangunan
    return seed,list_pembangunan

#F07
def kumpul(bahan_bangunan,seed,repeat=False):
    pasir,batu,air,seed = random_bahan(seed,repeat=True) # Mengenerate jumlah pasir batu dan air secara random
    # Menambah bahan sesuai bahan yang didapat
    bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) + pasir
    bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) + batu
    bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) + air
    if not repeat: # Jika bukan prosedur batch kumpul
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.\n")
        return seed,bahan_bangunan
    else: # Jika merupakan prosedur batch kumpul
        return bahan_bangunan,pasir,batu,air,seed

#F08_1
def batchkumpul(users,bahan_bangunan,seed):
    total_pasir = 0
    total_batu = 0
    total_air = 0
    jumlah_jin_pengumpul = hitung_jumlah(users,102,["","",""],"Jin Pengumpul",2)
    # Mengecek setiap jin pengumpul pada users
    for i in range(102):
        if users[i][2] == "Jin Pengumpul":
            # Mengenerate jumlah pasir batu dan air secara random lalu menambahkan pada total bahan
            bahan_bangunan,pasir,batu,air,seed = kumpul(bahan_bangunan,seed,repeat=True) 
            total_pasir += pasir
            total_batu += batu
            total_air += air
    if jumlah_jin_pengumpul != 0: # Jika ada jin pengumpul maka berhasil dan bahan baku akan ditambahkan ke matriks bahan_bangunan
        print(f"Mengerahkan {jumlah_jin_pengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.\n")
    else: # Apabila tidak ada jin pengumpul maka gagal
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
    return seed,bahan_bangunan

#F08_2
def batchbangun(users,candi,bahan_bangunan,seed):
    total_pasir = 0
    total_batu = 0
    total_air = 0
    jumlah_jin_pembangun = hitung_jumlah(users,102,["","",""],"Jin Pembangun",2)
    list_pembangunan = ["","","","",""] 
    matriks_pembangunan = [["","","","",""] for i in range(100)] 
    # Mengecek setiap jin pembangun pada users
    for i in range(102):
        if users[i][2] == "Jin Pembangun": # Apabila ada jin pembangun maka akan dicatat entry pembangunan pada matriks sementara
            seed,list_pembangunan = bangun(candi,bahan_bangunan,users[i][0],seed,repeat=True)
            index_kosong = cari_index_kosong(matriks_pembangunan,100,["","","","",""])
            matriks_pembangunan[index_kosong] = list_pembangunan
    if jumlah_jin_pembangun != 0: # Apabila terdapat jin pembangun pada users
        for i in range(jumlah_jin_pembangun):
            # Menghitung total bahan yang diperlukan untuk semua candi
            total_pasir += int(matriks_pembangunan[i][2])
            total_batu += int(matriks_pembangunan[i][3])
            total_air += int(matriks_pembangunan[i][4])
        print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, {total_air} air.")
        is_bahan_cukup = cek_kecukupan_bahan(bahan_bangunan,total_pasir,total_batu,total_air)
        if is_bahan_cukup: # Apabila bahan cukup
            # Mengurangi bahan sesuai bahan yang diperlukan
            bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - total_pasir
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - total_batu
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - total_air
            for i in range(cari_index_kosong(matriks_pembangunan,100,["","","","",""])): # Mengisi indeks matriks_pembangunan agar sesuai dengan ID candi
                index_kosong = cari_index_kosong(candi,100,["","","","",""])
                matriks_pembangunan[i][0] = index_kosong+1 
                candi[index_kosong] = matriks_pembangunan[i]
            print(f"Jin berhasil membangun total {jumlah_jin_pembangun} candi.\n")
        else:
            # Intinya agar output menjadi bagus dan mengakomodasi berbagai situasi
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
            print("Bangun gagal. ",string_akhir,"\n")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.\n")
    return seed,candi,bahan_bangunan

#F09
def laporanjin(users,candi,bahan_bangunan):
    # Mencari berbagai nilai yang perlu di output pada laporan jin 
    jumlah_jin = hitung_jumlah(users,102,["","",""])-2
    jumlah_jin_pengumpul = hitung_jumlah(users,102,["","",""],"Jin Pengumpul",2)
    jumlah_jin_pembangun = hitung_jumlah(users,102,["","",""],"Jin Pembangun",2)
    jin_terajin = cari_jin(candi,tipe="rajin")
    jin_termalas = cari_jin(candi,tipe="malas")
    total_pasir = bahan_bangunan[0][2]
    total_batu = bahan_bangunan[1][2]
    total_air = bahan_bangunan[2][2]
    # Mengoutput nilai yang telah di cari
    print(f"\nTotal Jin: {jumlah_jin}")
    print(f"Total Jin Pengumpul: {jumlah_jin_pengumpul}")
    print(f"Total Jin Pembangun: {jumlah_jin_pembangun}")
    print(f"Jin Terajin: {jin_terajin}")
    print(f"Jin Termalas: {jin_termalas}")
    print(f"Jumlah Pasir: {total_pasir} unit")
    print(f"Jumlah Air: {total_air}")
    print(f"Jumlah Batu: {total_batu}\n")

#F10
def laporancandi(candi):
    jumlah_candi = hitung_jumlah(candi,100,["","","","",""])
    total_pasir_digunakan = 0
    total_batu_digunakan = 0
    total_air_digunakan = 0
    for i in range(100): # Mencari jumlah total masing-masing bahan yang telah dipakai membangun candi
        if candi[i] != ["","","","",""]:
            total_pasir_digunakan += int(candi[i][2])
            total_batu_digunakan += int(candi[i][3])
            total_air_digunakan += int(candi[i][4])
    list_harga_candi = generate_list_harga_candi(candi,jumlah_candi) # List harga candi per ID candi
    print(f"\nTotal Candi: {jumlah_candi}")
    print(f"Total Pasir yang digunakan: {total_pasir_digunakan}")
    print(f"Total Batu yang digunakan: {total_batu_digunakan}")
    print(f"Total Air yang digunakan: {total_air_digunakan}")
    if list_harga_candi != ["",0]:
        # Mencari nilai max dan min pada list harga candi
        id_candi_termahal = cari_index_maxmin(list_harga_candi,100,"max")+1 # karena dimulai dari 1
        id_candi_termurah = cari_index_maxmin(list_harga_candi,100,"min")+1 # karena dimulai dari 1
        harga_termahal = list_harga_candi[id_candi_termahal-1][1]
        harga_termurah = list_harga_candi[id_candi_termurah-1][1]
        print(f"ID Candi Termahal: {id_candi_termahal} (Rp {harga_termahal})")
        print(f"ID Candi Termurah: {id_candi_termurah} (Rp {harga_termurah})\n")
    else: # Apabila list harga candi kosong
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -\n")

#F11
def hancurkancandi(candi):
    ID_candi = input("Masukkan ID candi: ")
    konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID_candi} (Y/N)? ")
    if konfirmasi == "Y":
        for i in range(100): # Mengubah entry candi dengan indeks sama dengan ID_candi yang dihancurkan dengan nilai ["","","","",""] (dihapus) 
            if candi[i][0] == ID_candi:
                candi[i] = ["","","","",""]
                print("\nCandi telah berhasil dihancurkan.\n")
                return candi
        # Apabila tidak ada candi dengan indeks sama dengan ID_candi yang diberikan
        print("Tidak ada candi dengan ID tersebut.\n")
        return candi
    elif konfirmasi == "N": # Pembatalan oleh user
        print("Penghancuran candi dibatalkan.\n")
    else: # Input konfirmasi tidak dikenali (bukan Y atau N)
        print("Perintah tidak dikenali. Penghancuran candi dibatalkan.\n")

#F12
def ayamberkokok(candi):
    print("Kukuruyuk.. Kukuruyuk..")
    jumlah_candi = hitung_jumlah(candi,100,["","","","",""])
    print(f"\nJumlah candi: {jumlah_candi}")
    if jumlah_candi < 100: # Apabila candi < 100 maka Roro Jonggrang menang
        print("\nSelamat, Roro Jonggrang memenangkan permainan!")
        print("\n*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.\n")
        sys.exit(1) # Keluar program
    else: # Apabila terdapat 100 candi
        print("\nYah, Bandung Bondowoso memenangkan permainan!\n")
        sys.exit(1) # Keluar program

#F13
def load(users,candi,bahan_bangunan):
    parser = argparse.ArgumentParser(usage="python main.py <nama_folder>") 
    parser.add_argument("path")
    if len(sys.argv)==1: # Apabila tidak ada argumen folder yang diberikan
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1) # Keluar dari program
    args=parser.parse_args()

    if os.path.exists(args.path): # Apabila path folder yang diberikan ada
        print("\nLoading...")
        # Mengubah file csv menjadi list yang bisa digunakan selama program berjalan
        users=csv_toarray(users,f"{args.path}\\user.csv",separator=';')
        candi=perbaikan_numerasi(csv_toarray(candi,f"{args.path}\\candi.csv",separator=';'))
        bahan_bangunan=csv_toarray(bahan_bangunan,f"{args.path}/bahan_bangunan.csv",separator=';')
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda\n") 
        return users,candi,bahan_bangunan
    else: # Ketika path folder yang diberikan tidak ditemukan
        print(f"Folder “{args.path}” tidak ditemukan.")
        sys.exit(1) # Keluar dari program

#F14
def save(file,panjang_file,panjang_sub_item,folder,filename):
    if 'save' not in os.listdir(): # Apabila save tidak ditemukan pada directory maka dibuat
        print(f"Membuat folder save")
        os.mkdir('save') 
    if folder not in os.listdir('save\\'): # Apabila nama folder tidak terdapat dalam folder save maka dibuat
        print(f"Membuat folder save/{folder}...")
        os.mkdir(f'save\\{folder}')
    f = open(f'save\\{folder}\\{filename}', 'w') # Membuka file tempat penyimpanan
    if panjang_file == 102: # Apabila matriks users maka tuliskan header users
        f.write("username;password;role\n") 
    elif panjang_file == 100: # Apabila matriks candi maka tuliskan header candi
        f.write("id;pembuat;pasir;batu;air\n")
    elif panjang_file == 3: # Apabila matriks bahan_bangunan maka tuliskan header bahan_bangunan
        f.write("nama;deskripsi;jumlah\n")
    # Mengubah setiap anggota matriks menjadi line di csv yang tiap elemennya dipisahkan ;    
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
    f.close() # Menutup file

#F15
def help(role):
    print('=========== HELP ===========')
    if role == 'Bandung_Bondowoso':
        print('1.  logout\n    Untuk keluar dari akun yang digunakan sekarang')
        print('2.  summonjin\n    Untuk memanggil jin')
        print('3.  hapusjin\n    Untuk menghapus jin')
        print('4.  ubahjin\n    Untuk mengubah tipe(role) jin')
        print('5.  batchkumpul\n    Untuk melakukan perintah kumpul untuk setiap jin pengumpul')
        print('6.  batchbangun\n    Untuk melakukan perintah bangun untuk setiap jin pembangun')
        print('7.  laporanjin\n    Untuk menampilkan laporan jin')
        print('8.  laporancandi\n    Untuk menampilkan laporan candi')
    elif role == 'Roro_Jonggrang':
        print('1.  logout\n    Untuk keluar dari akun yang digunakan sekarang')
        print('2.  hancurkancandi\n    Untuk menghancurkan candi yang tersedia')
        print('3.  ayamberkokok\n    Untuk mengakhiri pembangunan candi dan menentukan pemenang')
    elif role == 'Jin Pengumpul':
        print('1.  logout\n    Untuk keluar dari akun yang digunakan sekarang')
        print('2.  kumpul\n    Untuk mengumpulkan resource candi')
    elif role == 'Jin Pembangun':
        print('1.  logout\n    Untuk keluar dari akun yang digunakan sekarang')
        print('2.  bangun\n    Untuk membangun candi')
    else:
        print('1.  login\n    Untuk masuk menggunakan akun')
        print('2.  exit\n    Untuk keluar dari program dan kembali ke terminal')
    print("")

#F16
def exit(users,candi,bahan_bangunan):
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while konfirmasi != "Y" and konfirmasi != "y" and konfirmasi != "N" and konfirmasi != "n": # Selama konfirmasi belum valid maka akan terus ditanya sampai valid
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if konfirmasi == "Y" or konfirmasi == "y": # Apabila di konfirmasi maka akan dilakukan prosedur save
        folder = input('Masukan nama folder: ')
        print("Saving...")
        save(users,102,3,folder,'user.csv')
        save(candi,100,5,folder,'candi.csv')
        save(bahan_bangunan,3,3,folder,'bahan_bangunan.csv')
    sys.exit(1) # Keluar dari program
