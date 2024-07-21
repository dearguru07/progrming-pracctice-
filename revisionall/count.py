# def CountD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# n=int(input('enter a number'))    
# res=CountD(n)
# print(res)



def CountD(n):
    count=0
    while n!=0:
        n//=10
        count+=1
    return count
sr=int(input('enter a number'))    
er=int(input('enter a number'))
if sr>er:
    print('invalid range') 
else:  
    for i in range(sr,er+1):
        float=CountD(i)
        print(i,'count is',float)  