# Take 2 number and find out smallest number
# n1=int(input('Enter the 1st number:'))
# n2=int(input('Enter the 2nd number:'))
# if n1==n2:
#     print('Both are equal.')
# elif n1<n2:
#     print(n1,' is les than ',n2)
# else:
#     print(n2,' is less than ',n1)        

#######################################################
# Check number is less than 100 or not. if it is less than 100 than find whether it is odd or even .

# num=int(input('Please enter any number :'))
# if num < 100 :
#     if num%2==0:
#         print('Number is less than 100 and even.')
#     else:
#         print('Number is less than 100 and odd.')
# else:
#     print("As number is greater than 100, we can not proccess further.SORRY..!")   

############################################################
# Square the number if it is less than 10.

# m=int(input("Enter number :"))
# if m<10:
#     print('Square of number is :', m*m)
# else:
#     print('Number is greater than 10, so can not find square. SORRY...!')    
# 
##############################################################
# 
# Check the number is zero, positive or negative using nested if else.

# m1=int(input('Enter the number :'))
# if m1==0:
#     print('Number is 0 ;')
# else :
#     if m1>0:
#         print("Number is positive.")                 
#     else:
#         print('Number is negative.')    

####################################################################
# 
# Take 3 numbers and check the greatest number using nested if else.
# 
# v1=int(input('Enter first number :'))        
# v2=int(input('Enter second number :'))        
# v3=int(input('Enter third number :'))        
# if v1>v2 and v1>v3:
#     print(v1, " is greatest number.")
# else:
#     if v2>v1 and v2>v3:
#         print(v2, " is greatest number.") 
#     else:
#         print(v3, 'is greatest number.')
# 
# #####################################################################
# 
# Take 3 number and find smallest number using logcal operator.
# 
# a1=int(input('Enter 1st number :'))       
# a2=int(input('Enter 2nd number :'))       
# a3=int(input('Enter 3rd number :'))   

# if a1<a2 and a1<a3 :
#     print(a1, ' is smallest number.')
# elif a2<a1 and a2<a3:
#     print(a2,' is smallest number.')
# else:
#     print(a3,' is amallest number.')        

###########################################################################
# 
#  Swap two numbers without using third number.
# 
# a=int(input('Enter first number :')) 
# b=int(input('Enter second number :')) 
# print('x is ', a,' and y is', b)
# a=a+b
# b=a-b
# a=a-b
# print('x is ',a,' and y is ',b)

###############################################################################333
# Pattern printing.

o=int(input('Please Enter first number :'))
p=int(input('Please Enter second number :'))
if o>p:
    while (True):
        o=o-3
        if o<p:
            break
        print(o,"\n")
else:
    while(True):
        o=o+3
        if p<o:
            break
        print(o,'\n')        