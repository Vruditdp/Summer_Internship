# Displaying greatest number among 2 numbers.
             
n1=int(input("Please enter first num : "))
n2=int(input("Please enter second num : "))
if n1==n2:
    print('Numbers are equal.')
elif n1>n2 :
    print(n1,' is greater than ',n2)
else:
    print(n2,' is greater than ',n1)  