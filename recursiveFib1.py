from timeit import default_timer as timer
t0= timer()
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print(fib(40))

print("Time elapsed: ", timer() - t0)
