bundt_cake_ingredients = ['flour', 'baking powder', 'baking soda', 'butter', 'sugar', 'eggs', 'buttermilk', 'vanilla']

def make_cake(name:str, ingredients_list:list):

    return f"Making a {name} with these ingredients: { ", ".join(ingredients_list) }"


bundt_cake = make_cake( bundt_cake_ingredients )

print( bundt_cake )