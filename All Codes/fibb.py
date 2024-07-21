def Fibb(n):
    n1=0
    n2=1
    for i in range(1,n+1):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
n=int(input('enter a numb'))
res=Fibb(n)        
    
    
    
# def Leep(n):
#     if (n%100!=0 and n%4==0) or n%400==0:
#         print('leep')
#     else:
#         print('not a leep')   
# sn=int(input('entre a mun'))             
# en=int(input('entre a mun'))             
# res=True
# for i in range(sn,en+1):
#     if res==Leep(i):
#         print(i)


