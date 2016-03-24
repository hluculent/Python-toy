def foo(num, base):
    if num >= base:
        foo(num/base, base) #执行函数的时候会继续检查if条件，直至运行foo(3,2)时：
                            #if 3 > 2:
                            #foo(1,2)无返回值
                            #print 3
                            #print 1
                            #而foo(3,2)又是foo(7,2)中的一部分，执行完foo(3,2),print 7,print 1...
        print num,
        print num%base

numA = input()
numB = input()
foo(numA,numB)

"""
numA = 126
numB = 2
>>> 3 1 
7 1 
15 1 
31 1 
63 1 
126 0
"""

