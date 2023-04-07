def length(x):
    length = 0
    for i in x:
        length += 1
    return length

def add(x,y):
    new_list = [0 for i in range(length(x)+1)]
    for i in range(length(x)):
        new_list[i] = x[i]
    new_list[-1] = y
    return new_list

def csv_toarray(x,separator):
    result_list = []
    with open(x) as files:
        files_length = length(files)
    with open(x) as files:
        j = 0
        for lines in files:
            j += 1
            sublist = []
            first_index = 0
            last_index = 0
            i = 0
            for w in lines:
                if w == separator and i != 0:
                    last_index = i
                    sublist = add(sublist,lines[first_index:last_index])
                    first_index = last_index + 1
                    i += 1
                elif w == separator and i == 0:
                    first_index = 1
                    i += 1
                elif length(lines) == i+1:
                    if j != files_length:
                        last_index = i
                    else:
                        last_index = i+1
                    sublist = add(sublist,lines[first_index:last_index])
                else:
                    i += 1
            result_list = add(result_list,sublist)
        return result_list
    
def array_tocsv():
    pass

def is_part_of(x,y):
    is_part_of = False
    flat_list = []
    for sublist in y:
        for item in sublist:
            flat_list = add(flat_list,item)
    for i in flat_list:
        if x == i:
            is_part_of = True
    return is_part_of

