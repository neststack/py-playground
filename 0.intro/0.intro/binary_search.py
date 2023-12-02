def binary_search(list, target):
  """
  Returns the index position of the target if found, else returns None
  """
  steps = 0
  first = 0
  last = len(list) - 1
  
  while first <= last:
    midpoint = (first + last)//2
    # print('steps',steps,'first',first,'last',last,'midpoint',midpoint)
    steps += 1
    if list[midpoint] == target:
      return {'index': midpoint,'steps':steps}
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
    
  return {'index': None,'steps':steps}

def verify(result):
  index = result["index"]
  steps = result["steps"]
  if index is not None:
    print("Target found at index:",index,"Steps:",steps)
  else:
    print("Target not found in list.","Steps:",steps)
    
numbers = range(0,10000)
result = binary_search(numbers, 12000)
verify(result)

result = binary_search(numbers, 1200)
verify(result)