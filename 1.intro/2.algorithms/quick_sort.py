import sys
sys.path.append('../dummy_data')
from data import five, eighth, ten_thousand, one_million

def quicksort(values):
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  pivot = values[0]
  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)

  # print("%20s %2s %-20s" % (less_than_pivot, pivot, greater_than_pivot))
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
      
  

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True
  
numbers = one_million
# print(numbers)
sorted_numbers = quicksort(numbers)
# print(is_sorted(sorted_numbers))