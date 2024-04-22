one = 1
two = "2"

def compare_numbers(num_one:int, num_two:int):
    if num_one > int(num_two):
        return "Number one is greater"
    elif num_one < int(num_two):
        return "Number two is greater"
    else:
        return "The numbers are equal"

print( compare_numbers(one, two) )