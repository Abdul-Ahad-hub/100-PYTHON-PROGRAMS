def sum_list(*args):
    return sum(args)

def sum_values(**kwagrs):
    total = 0  
    for val in kwagrs.values():
        total += val
    return total


print(sum_list(1,2,3))
print(sum_values(a=1, b=2, c=3)) 

    