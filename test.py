import time

def random_number_generator(first_number,last_number,seed):
    a = 75
    c = 74
    m = 65537
    number = (a*seed+c) % m
    number_on_range = number % (last_number - first_number + 1) + first_number
    return number_on_range,number

def random_bahan(repeat=False,repeat_time=0):
    def generate_bahan(seed_1):
        pasir,seed_2 = random_number_generator(1,5,seed_1)
        batu,seed_3= random_number_generator(1,5,seed_2)
        air,seed_4 = random_number_generator(1,5,seed_3)
        return pasir,batu,air,seed_4
    seed = time.time_ns()
    if not repeat or repeat_time == 0:
        pasir,batu,air,seed = generate_bahan(seed)
        return pasir,batu,air
    else:
        list_bahan = [[0,0,0] for i in range(repeat_time)]
        for i in range(repeat_time):
            pasir,batu,air,seed = generate_bahan(seed)
            list_bahan[i] = [pasir,batu,air]
        return list_bahan
    
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

list = sort_leksikografis([["abcd",8],["crya",8],["brya",7],["erya",4],["abcde",9],["abcc",9],["",0]],7,False)
print(list)

