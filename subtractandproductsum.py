def subtractProductAndSum(n):
  s = str(n)
  newArr = [int(i) for i in s]

  multi = 1
  addition = 0

  for i in newArr:
    multi *= i
    addition += i

  total = multi + addition
  return total


# a faster solution I found online

def subtractProductAndSum2(self, n: int) -> int:
  n_str = str(n)
  product = 1
  n_sum = 0

  for character in n_str:
    product *= int(character)
    n_sum += int(character)

  return product - n_sum



subtractProductAndSum(55)