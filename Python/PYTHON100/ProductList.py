from functools import reduce


def product_list(my_list):
    result = reduce(lambda x, y:x*y,my_list)
    return result


print(product_list([1,2,3,4]))