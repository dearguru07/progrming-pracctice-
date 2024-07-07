def Fibb(n):
    n1=0
    n2=1
    for i in range(1,n+1):
        print(n1)
        n3=n1+n2
        n1,n2=n2,n3
n=int(input('entr'))        
Fibb(n)


# def Fibb(n):
#     n1=0
#     n2=1
#     for i in range(1,n+1):
#         print(n1)
#         n3=n1+n2
#         n1=n2
#         n2=n3
# n=int(input('entr'))        
# Fibb(n)


# n=int(input('entr a num'))
# n1=0
# n2=1
# for i in range(1,n+1):
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3