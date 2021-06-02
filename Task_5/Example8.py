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