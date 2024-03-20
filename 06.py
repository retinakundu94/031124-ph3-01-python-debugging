cats = ["Octavia", "Ursula"]

def cats():
    for cats in cats:
        cats.append(f"Meow my name is {cats}")
    return cats

print( cats() )