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