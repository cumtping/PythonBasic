class Parent:
    parentAttr = 100
    
    def __init__(self):
        print ('parent constructor')

    def __init__(self, attr):
        self.parentAttr = attr
        print ('parent constructor')
        
    def parentMethod(self):
        print ('parent method called')
        
    def setAttr(self, attr):
        self.parentAttr = attr
       
    def getAttr(self):
        print ('parentAttr', Parent.parentAttr)
        #return self.parentAttr
        
    def __add__(self, other):
        return Parent(self.parentAttr + other.parentAttr)

class Child(Parent):
    def __init__(self):
        print ('child constructor')
        
    def childMethod(self):
        print ('call child method')
    
    
    def parentMethod(self):
        print ('override, parent method called')

c = Child()
c2 = Child()
c2.setAttr(10000)

c.parentMethod()
c.childMethod()
c.setAttr(200)
c.getAttr()

c3 = c + c2
print ('c3.parentAttr=', c3.parentAttr)