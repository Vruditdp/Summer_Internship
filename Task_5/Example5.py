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