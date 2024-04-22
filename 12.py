from faker import Faker
from random import choice

fake = Faker()

def create_angry_bird():

    bird_dict = {
        'name': fake.name(),
        'anger_level': choice( range(5,11) )
    }

    return bird_dict


print( create_angry_bird() )