from functools import lru_cache

@lru_cache(maxsize = 100)
def fibonacci(n):
    # edge cases
    if type(n) != int:
        raise TypeError('Value must be a positive number.')
    if n < 1:
        raise ValueError('Number must be postive.')    

    #base case
    if n == 1:
        return 1
    elif n == 2:
        return 1 
    elif n > 2: 
        # recursive step
        return fibonacci(n - 1) + fibonacci(n - 2) 
# print(fibonacci('10'))

for n in range(1, 100):
  print(n, ':', fibonacci(n))




# solution with M
# fib_cache = {}
# def fibonacci(n):
#     if n in fib_cache:
#         return fib_cache[n]
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1    
#     elif n > 2:
#         value = fibonacci(n - 1) + fibonacci(n - 2)

#     fib_cache[n] = value
#     return value   

# for n in range(1, 100):
#     print(n, ':', fibonacci(n))             

