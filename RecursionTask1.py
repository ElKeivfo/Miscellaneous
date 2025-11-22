#Write a recursive function that, given a non-negative input n, sums up all non-negative integers up to and including n, and returns that value.


def sum(i, total):
	while i != N + 1:
		total += i
		i += 1
#		sum(i, total)
	return total


negative = True
while negative:
	N = int(input("Please enter a number: "))
	if N >= 0:
		negative = False

num = sum(0, 0)
print(num)
