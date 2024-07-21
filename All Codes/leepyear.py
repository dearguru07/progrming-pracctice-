# def Yeaar(n):
#     if (n%100!=0 and n%4==0) or(n%400==0):
#         print('leeap')
#     else:
        
#         print('not')
# n=int(input('emter ayear'))            
# Yeaar(n)



def Year(n):
    if (n%100!=0 and n%4==0) or (n%400==0):
        print('leeep')
    else:
        print('not a leep') 
sr=int(input('enetr'))           
er=int(input('enetr'))
res=True 
for i in range(sr,er+1):
     if res==Year(i):
         print(i)



# n=int(input('entr'))
# if (n%400!=0 and n%4==0) or n%100==0:
#     print('leaap')
# else:
#     print('not a leep')       