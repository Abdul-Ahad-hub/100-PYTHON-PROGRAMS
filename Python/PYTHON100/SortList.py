def sort_list(list):
    sorted_list = sorted(list, key= lambda x: x[1])
    return sorted_list

print(sort_list([('Charlie', 19), ('Bob', 25), ('Alice', 32), ('Diana', 40)]))

