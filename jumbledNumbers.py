def main():
  num = input("Please enter a number: ")
  num.split()
  print(num)
  total = len(num)

  starting_value = 0
  for x in range (0,total-1):
    first = num[starting_value]
    second = num[starting_value+1]
    first=int(first)
    second=int(second)
    if first == second + 1 or first == second - 1:
      starting_value += 1
    else:
      print("It is not jumbled")
      return False
  print("It is jumbled")

main()
