steps = 0
def recursive_binary_search(list, target):
  """
  Returns the index position of the target if found, else returns None
  """
  global steps
  first = list[0]
  last = list[-1]
  midpoint = (first+last)//2
  print('steps',steps,'first',first,'last',last,'midpoint',midpoint)
  steps += 1  
  if len(list) == 0:
    result = {'found':False, 'steps':steps}
    steps = 0
    return result
  else:
    midpoint = len(list)//2
    midValue = list[midpoint]
    if midValue == target:
      result = {'found':True, 'steps':steps}
      steps = 0
      return result
    else:
      if midValue < target:
        return recursive_binary_search(list[midpoint + 1:], target)
      else:
        return recursive_binary_search(list[:midpoint], target)

def verify(result):
  found = result["found"]
  steps = result["steps"]
  print("Target found:",found,"Steps:",steps)
    
numbers = range(0,10000)
# result = recursive_binary_search(numbers, 12000)
# verify(result)

result = recursive_binary_search(numbers, 1200)
verify(result)