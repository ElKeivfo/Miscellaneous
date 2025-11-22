def double_factorial(num):
  product = num
  total = product
  while product > 2:
    product -= 2
    total = total * product
  return total 

num = int(input("Please enter a number: "))
print(double_factorial(num))
