'''
n=int(input('enter a nuum'))
tem=True
er=n//2
for i in range(2,er+1):
    if n%i==0:
        tem=False
        break
if tem==True and n>2:
    print('prime')
else:
    print('not a prime')        

'''


# def prime(n):
#     tem=True
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True and n>2:
#         print('prime')
#     else:
#         print('not')
# n=int(input('entr'))
# prime(n)                  
     
     
def Rang(n):
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            return False
    return True
sr=int(input('entr num'))    
er=int(input('entr num')) 
for i in range(sr,er+1):
    if i>1:
        res=Rang(i)
        print(res)  