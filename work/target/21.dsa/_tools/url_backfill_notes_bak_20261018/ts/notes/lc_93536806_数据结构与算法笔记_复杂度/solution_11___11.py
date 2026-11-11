# 此项时间复杂度为以2为底的log(N) 即 log2(N)
def func(n):
 if n <= 1: return n
 return func(n // 2) + 1