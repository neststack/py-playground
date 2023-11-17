def linear_search(list, target):
  """
  Returns the index position of the target if found, else returns None
  """
  steps = 0
  index = 0
  for i in range(0, len(list)):
    steps += 1
    if list[i] == target:
      return {'index': i,'steps':steps}
    
  return {'index': None,'steps':steps}

def verify(result):
  index = result["index"]
  steps = result["steps"]
  if index is not None:
    print("Target found at index:",index,"Steps:",steps)
  else:
    print("Target not found in list.","Steps:",steps)
    
numbers = [1,2,3,4,5,6,7,8,9]
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)