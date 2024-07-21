def Leep(n):
    if (n%400!=0 and n%4==0) or n%100==0:
        print('leep year')
    else:
        print('not a leep year')   
n=int(input('enter a number'))         
Leep(n)        