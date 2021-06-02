# Take 3 number and find smallest number using logcal operator.

a1=int(input('Enter 1st number :'))       
a2=int(input('Enter 2nd number :'))       
a3=int(input('Enter 3rd number :'))   

if a1<a2 and a1<a3 :
    print(a1, ' is smallest number.')
elif a2<a1 and a2<a3:
    print(a2,' is smallest number.')
else:
    print(a3,' is amallest number.')   