# Que 7

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