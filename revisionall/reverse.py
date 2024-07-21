# def Revision(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return rev
# n=int(input('enter a number'))    
# res=Revision(n)
# print(res)


def Revision(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    return rev
sr=int(input('enter a number'))    
er=int(input('enter a number'))  
if sr>er:
    print('invalid range')
else:
    for i in range(sr,er+1):
        float=Revision(i)
        print(i,'revision is',float)
      