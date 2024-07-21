# def LCM(n1,n2):
#     if n1>n2:
#         n1,n2=n2,n1
#     lcum=n2
#     while True:
#         if lcum%n1==0 and lcum%n2==0:
#             break
#         lcum+=n2
#     return lcum        
# n1=int(input('enter a number'))
# n2=int(input('enter a number'))
# res=LCM(n1,n2)
# print(res)




def LCM(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    lcm=n2
    while True:
        if lcm%n1==0 and lcm%n2==0:
            break
        lcm+=n2
    return lcm  
n1=int(input('enter a number'))      
n2=int(input('enter a number'))      
res=LCM(n1,n2)
print(res)