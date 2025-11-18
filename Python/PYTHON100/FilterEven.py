def get_even_from_list(my_list):
    return list(filter(lambda x:x%2==0, my_list))

print(get_even_from_list([1,2,3,4,5,6]))