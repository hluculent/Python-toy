#1
def put_tag():
    f1 = open(path0)
    fn = f1.readlines()
    for i in range(0,len(fn)):
        fn[i] = str(i+1) + ' ' + fn[i]
    f1.close()
    f2 = open(path0,'w')
    f2.writelines(fn)
    f2.close()
    
#2
list = [1,2,3]
for index,text in enumerate(list):
   print index+1 ,text
