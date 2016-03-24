#递归必须要有停止条件
#斐波那契数列 0，1，1，2，3，5，8...

def fib(n):
  a,b = 0,1
  count = 1
  while count < n:
    a,b = b, a+b
    count = count + 1
  print a
  
#使用递归
def fib(n):
  if n == 0 or n == 1:
    return n
  else:
    return fib(n-1) + fib(n-2)
