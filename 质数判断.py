def is_prime(x):
    if x < 0:
        return False
    #0，1不是质数，2，3是质数
    elif x == 0 or x == 1:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        for n in range(2, x-1):
            if x % n == 0 :
                return False
        else:
            return True
            
            
"""
ver.2
用户界面友好并且可以多次输入
"""
from math import sqrt
def isprime(x):
    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2, k+1):
        if x%j == 0:
            return False
    return True

if __name__ == "__main__":
    flag = 'y'
    while(flag == 'y'):
        num = input("Please input a number:")
        for i in range(2,num):
            if isprime(i) and num % i == 0:
                print i,
        flag = raw_input("\nIf you want to input another number, \
input y. Else input n.") #在引号内换行要顶格，不然空格也是字符串输出
