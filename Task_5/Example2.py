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