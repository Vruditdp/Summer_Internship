#Que. 1
class cal1:
    num1=0
    num2=0
    num3=0

    def setdata(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def display(self):
        print('The sum of three numbers is : ',self.num1+self.num2+self.num3)

o=cal1()
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
o.setdata(num1,num2,num3)
o.display()
