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