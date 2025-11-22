from timeit import default_timer as timer
t0= timer()
def fib(n):
  fibNumbers = [0,1]   
  for i in range(2, n+1):
    fibNumbers.append(fibNumbers[i-1]+fibNumbers[i-2])
  return fib[n]

print(fib(5))

print("Time elapsed: ", timer() - t0)
