#  Swap two numbers without using third number.

a=int(input('Enter first number :')) 
b=int(input('Enter second number :')) 
print('x is ', a,' and y is', b)
a=a+b
b=a-b
a=a-b
print('x is ',a,' and y is ',b)