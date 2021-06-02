# Take 3 numbers and check the greatest number using nested if else.

v1=int(input('Enter first number :'))        
v2=int(input('Enter second number :'))        
v3=int(input('Enter third number :'))        
if v1>v2 and v1>v3:
    print(v1, " is greatest number.")
else:
    if v2>v1 and v2>v3:
        print(v2, " is greatest number.") 
    else:
        print(v3, 'is greatest number.')