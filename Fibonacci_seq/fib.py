# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         print b,
#         a,b = b, a + b
#
# fib(100)

def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n


for i in range(40):
    print i, mem_fib(i)
