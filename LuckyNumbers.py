import sys
def main():
  
  num = input("Please enter a number: ")
  num.split()
  print(num)
  total = len(num)
  number = str(num)


  i = 0
  for x in range (0,len(num)):
    starting_value = 0
    starting_value_next = 1
    for x in range (0,len(num)-1):
      first = num[starting_value]
      second = num[starting_value_next]
      first=int(first)
      second=int(second)
      if first != second:
        
        starting_value_next += 1
      else:
        print("It is not lucky because {0} is repeated.".format(first))
        sys.exit()
    i+= 1
    num = num[i:len(num)]
  if number[2:3] != number[3:4]:
    print("It is lucky")
  else:
    print("It is not lucky because {0} is repeated.".format(number[2:3]))

main()
