def recursive_print_function(number:int):
        print(number)
        if (number<= 100):
         recursive_print_function(number + 1)

recursive_print_function(1)