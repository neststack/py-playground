import random
import sys
sys.path.append('../dummy_data')
from data import five, eighth, ten_thousand, one_million

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

steps = 0

def selection_sort(values):
  sorted_list = []
  # print("%-30s %-30s" % (values, sorted_list))
  global steps 
  steps = 0
  for i in range(0, len(values)):
    index_to_move = index_of_min(values)
    sorted_list.append(values.pop(index_to_move))
    steps += 1
    # print("%-30s %-30s" % (values, sorted_list))
  print('steps:',steps)
  return sorted_list

def index_of_min(values):
  global steps 
  min_index = 0
  for i in range(1, len(values)):
    if values[i] < values[min_index]:
      min_index = i
    steps += 1
  return min_index

def calc_steps(length):
  n = length
  s = 0
  while n != 0:
    s += n
    n -= 1
  return s

# print(selection_sort(five))
# print(selection_sort(eighth))
selection_sort(ten_thousand)
# print(calc_steps(5),calc_steps(8),calc_steps(10000))