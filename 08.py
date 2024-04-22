street_fighter = {
    "name": "Ryu",
    "special_move": "Hadouken"
}

def print_street_fighters(fighters:list):
    for fighter in fighters:
        print(f"{fighter["name"]}'s special move is ${fighter["special_move"]}")

print_street_fighters( [ street_fighter ] )