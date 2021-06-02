# Take 2 number and find out smallest number
n1=int(input('Enter the 1st number:'))
n2=int(input('Enter the 2nd number:'))
if n1==n2:
    print('Both are equal.')
elif n1<n2:
    print(n1,' is les than ',n2)
else:
    print(n2,' is less than ',n1)    