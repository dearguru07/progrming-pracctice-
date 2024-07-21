# n=int(input('enter a num'))
# count=0
# while n!=0:
#     n=n//10
#     count+=1
# print(count)    


# def Digits(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# n=int(input('enter'))
# res=Digits(n)
# print(res)


# def Digits(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# sr=int(input('entr ')) 
# er=int(input('enter '))
# for i in range(sr,er+1):
#     res=Digits(i)
#     print(i,'digits',res)


# def Polu(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input('entr'))
# res=Polu(n)
# if n==res:
#     print("poly")
# else:
#     print('not ')   

# n=int(input('enter anum'))     
# rev=0
# tem=n
# while n!=0:
#     rem=n%10
#     rev=(rev*10)+rem
#     n=n//10
# print(n)
# print(tem)   
# if tem==rev:
#     print('poly')
# else:
#     print('not')        


# -------------------polyndrome range functions----------------


def poly(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
sr=int(input('enter'))    
er=int(input('enter'))
if sr>er:
    print('invalid range')
else:
    for i in range(sr,er+1):
        res=poly(i)
        if i==res:
            print(i)