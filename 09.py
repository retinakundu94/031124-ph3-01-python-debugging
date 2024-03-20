people = []

def create_new_person(name_param:str, age_param:int):
    new_person = { 'name': name_param, 'age': age_param }
    people.append(new_person)
    return people

def remove_person(person:dict):
    people.remove(person)

sakib = create_new_person('Sakib', 15)
chett = create_new_person('Chett', 101)

remove_person(sakib)

print( people )