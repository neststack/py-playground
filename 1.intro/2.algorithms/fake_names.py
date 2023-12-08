from faker import Faker

fake = Faker()

random_names = [fake.name() for _ in range(10000)]

print(random_names)