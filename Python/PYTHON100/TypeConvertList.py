def list_string_to_int(list_m):
    int_list = list(map(int, list_m))
    return int_list

print(list_string_to_int(["1", "2", "3"]))