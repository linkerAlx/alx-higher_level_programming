def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]

my_list = [2,5,12,4,5]
idx = 2
print ("{}".format(element_at(my_list, idx)))
