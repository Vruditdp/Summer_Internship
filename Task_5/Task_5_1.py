class Bunty:

    def __init__(self,num):
        print('This is constructor...\n And my rollnumber is :  ',num)

    def fun(self):
        print("I am function of Bunty Class.")

    def fun1(self,name):
        print('I am ',name)    

f=Bunty(45) 
f.fun() 
f.fun1("Bunty")   

class Vrudit(Bunty):
    def __init__(self):
        print("This is constructor of Vrudit class.")

f1=Vrudit()
f1.fun1("patel")        
    
          