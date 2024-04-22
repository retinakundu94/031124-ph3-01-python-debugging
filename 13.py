dogs_list = ['Clifford', 'Scooby Doo', 'Balto']

def print_list_items(list_param:list):
    i = 0
    while i < len( dogs_list ):
        print(i)
        print(dogs_list[i])
        i += 1


print_list_items( dogs_list )