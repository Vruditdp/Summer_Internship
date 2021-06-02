# Que 10

class arith:
    o=0
    p=0
    def __init__(self):
        self.o=int(input('Enter the first number :'))
        self.p=int(input('Enter the second number :'))

    def add(self):
        return self.o+self.p 
    def subtract(self):
        return self.o-self.p 
    def multiply(self):
        return self.o*self.p 
a=arith()
print('Addition of two number is : ',a.add())                 
print('Substaction of two number is : ',a.subtract())                 
print('Multiplication of two number is : ',a.multiply())      