
double_palindrome_list = []
while len(double_palindrome_list) != 20:
  num = input("Please enter a number: ")
  reverse = num[::-1]
  if num == reverse:
    bin_num = bin(int(num))[2:]
    bin_num_reverse = bin_num[::-1]
    if bin_num_reverse == bin_num: 
      double_palindrome_list.append(num)
      print(double_palindrome_list)
