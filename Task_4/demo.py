# Example of functions

# def func():
#     print('This is function.')

# print(func())

# def fun(name):
#     print('My name is ',name)

# fun("Vrudit")

# def pub(a1,a2):
#     return a1+a2
# var1=int(input('Enter the first number:'))    
# var2=int(input('Enter the second number:'))   
# print('The sum is ',pub(var1,var2)) 

# def sum(*n1):
#     sum=0
#     for i in n1:
#         sum=sum+i
#     print('Ans is ',sum)

# sum(10,20)        
# sum(10,20,30)    

###################################################

# def myfun(**arg):
#     for i,j in arg.items():
#         print(i,j)
# myfun(name='Vrudit',roll=45)  

#################################################
# def myfunction():
#     x=10
#     print('value inside function is ',x)
# x=20
# myfunction()
# print('value outside function ',x)
# 
# ########################################
# 
def mysum(o,p):
    return o+p
def yoursum(*n2):
    sum=0
    for i in n2:
        sum=sum+i
    return sum    
