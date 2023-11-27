import sys
sys.path.append('../dummy_data')
from data import five, eighth, ten_thousand, one_million

def merge_sort(values):
  if len(values) <= 1:
    return values
  middle_index = len(values) // 2
  left_values = merge_sort(values[:middle_index])    
  right_values = merge_sort(values[middle_index:])
  sorted_values = []
  left_index = 0    
  right_index = 0    
  
  while left_index < len(left_values) and right_index < len(right_values):
    if left_values[left_index] < right_values[right_index]:
      sorted_values.append(left_values[left_index])
      left_index += 1
    else:
      sorted_values.append(right_values[right_index])
      right_index += 1
  sorted_values += left_values[left_index:]
  sorted_values += right_values[right_index:]
  return sorted_values
  

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True
  
numbers = one_million
# print(numbers)
sorted_numbers = merge_sort(numbers)
# print(is_sorted(sorted_numbers))