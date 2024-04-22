from faker import Faker

fake = Faker()

person = {
    'name': fake.name(),
    'address': fake.address(),
    'email': fake.email(),
    #'phone': fake.phone()
}

print( person )