# def Prime(n):
#     tem=True
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True and n>1:
#         print('primw')
#     else:
#         print('not a prime')        
# n=int(input('enter a number'))        
# Prime(n)



def Prime(n):
    er=n//2
    for i in range(2,er):
        if n%i==0:
            return False
    return True
sr=int(input('enter a number'))    
enr=int(input('enter a number'))  
if sr>enr:
    print('invalid range')
for i in range(sr,enr+1):
    if i>1:
        float=Prime(i)
        if float==True:
            print(i) 