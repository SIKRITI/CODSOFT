def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter the third number:"))
m = max(num1,num2,num3)
print("Max of {0} and {1} and {2} is {3};".format(num1,num2,num3,m))
