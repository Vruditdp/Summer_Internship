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

#Que. 2

class cal2:
    r=0
    area=0
    def setdata(self):
        self.r=int(input('Enter the radius of circule : '))

    def area(self):
        self.area=2*3.14*self.r

    def display(self):
        print('The area of circle is : ',self.area)

ob=cal2()
ob.setdata()
ob.area()
ob.display()

# Que. 4

class cal4:
    num=0
    def setdata(self):
        self.num=int(input('Enter the number : '))
    def display(self):
        return self.num*self.num

obj=cal4()
obj.setdata()
print('The square of ',obj.num,' is ',obj.display())

#Que. 5

class employee:
    name=""
    designation=""
    def __init__(self,name,designation):
            self.name=name
            self.designation=designation
            print('Name and designation of employee are ',self.name,' and ',self.designation)

class salary(employee):
    salary=0
    def sel(self,salary):
        self.salary=salary
        print('salary is ',self.salary)
obje=salary("vrudit","manager")
obje.sel(1000000)

# Que 6

class cal5:
    len=0
    wid=0
    area=0
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def calArea(self):
        self.area=self.len*self.wid
    def display(self):
        print('The area of rectangle is ',self.area)

l=int(input('enter the length of rectangle :'))
w=int(input('enter the width of rectangle :'))
objec=cal5(l,w)
objec.calArea()
objec.display()

# vQue 7

class cal6:
    side = 0
    area = 0
    def setdata(self):
        self.side = int(input('Enter the length of square :'))
    def area(self):
        self.area = self.side*self.side
    def display(self):
        print("The area og the square is ", self.area)
object = cal6()
object.setdata()
object.area()
object.display()

# Que. 8

class publisher:
    title=""
    def title(self,title):
        self.title=title
        print('Title is ',self.title)
class book(publisher):
    page=0
    def page(self,page):
        self.page=page
        print('page is ',self.page)
class tape(book):
    time=0
    def time(self,time):
        self.time=time  
        print('Time is ',self.time)   
p=tape()
p.title("ABC")
p.page(90)
p.time(4)

# Que 9

class scheme:
    scheme_id=0
    scheme_name=""
    outgoing_rate=0
    message_charge=0
    def show(self,id,name,rate,charge):
        scheme_id=id
        scheme_name=name
        outgoing_rate=rate
        message_charge=charge
        print('Scheme id :',scheme_id,'scheme name', scheme_name,'rate : ',outgoing_rate,' charge :',message_charge)

class customer(scheme):
    cust_id=0
    name=""
    mobile_no=0
    def dis(self,id,name,no):
        cust_id=id
        self.name=name
        mobile_no=no
        print('Customer id :',cust_id,' name : ',name, ' mobile no : ',mobile_no)        
c=customer()
c.show(1,"abc",54,99)   
c.dis(5,"xyz",9087705632)     

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