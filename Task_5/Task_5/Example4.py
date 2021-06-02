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