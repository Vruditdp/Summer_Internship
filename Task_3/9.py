# Check number is less than 100 or not. if it is less than 100 than find whether it is odd or even .

num=int(input('Please enter any number :'))
if num < 100 :
    if num%2==0:
        print('Number is less than 100 and even.')
    else:
        print('Number is less than 100 and odd.')
else:
    print("As number is greater than 100, we can not proccess further.SORRY..!")