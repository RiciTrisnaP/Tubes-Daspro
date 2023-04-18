def remove_at_index(list,index):
    for i in range(index,len(list)-1):
        list[i] = list[i+1]
    list = remove_last(list)
    return list

def remove_last(x):
    new_list = [0 for i in range(len(x)-1)]
    for i in range(len(x)-1):
        new_list[i] = x[i]
    return new_list

users = [['username', 'password', 'role'], ['Bandung', 'Bondowoso', 'Bandung_Bondowoso'], ['Roro', 'Jonggrang', 'Roro_Jonggrang'], ['Ifrit', 'Ifrit123', 'Pengumpul']]
users = remove_at_index(users,3)
print(users)