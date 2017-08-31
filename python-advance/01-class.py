class Employee:
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
    # called when object is recycled.
   def __del__(self):
        print ('Employee is destroied')
      
emp1 = Employee("Zara", 2000)
print ('name=', emp1.name)
emp1.displayCount()
emp1.displayEmployee()

# inner varible
print (Employee.__doc__)
print (Employee.__name__)
print (Employee.__module__)
print (Employee.__dict__)
print (Employee.__bases__)
