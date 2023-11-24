def sum(values):
  total = 0
  for num in values:
    total += num
  return total

def recursion_sum(values):
  if not values:
    return 0
  return values[0] + recursion_sum(values[1:])

print(sum([1,2,3,4,5,6]))
print(recursion_sum([1,2,3,4,5,6]))