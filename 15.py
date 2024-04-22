numbers_list = []

def average_numbers_in_list(num_list:list):
    if len (num_list) > 0:
        return sum(num_list) / len(num_list)
    else:
        return 0

avg = average_numbers_in_list( numbers_list )

print( avg )