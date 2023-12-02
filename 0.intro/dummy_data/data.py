import array
import random

# Set the seed for reproducibility (optional)
random.seed(42)

# Generate an array of 10,000 random numbers between 1 and 100
def random_list(length):
  return array.array('i', [random.randint(1, 10*length) for _ in range(length)])

five = random_list(5)
eighth = random_list(8)
ten_thousand = random_list(10000)
one_million = random_list(1000000)