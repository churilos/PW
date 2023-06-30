class Worker:
  'doc class Worker'
  count = 0
 
  def __init__(self,name,surname):
    self.name = name
    self.surname = surname
    Worker.count += 1
 
  def display(self):
   print("Worker:")
   print("{} {}".format(self.name,self.surname))
w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)

class Animal:
  count = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Animal.count += 1
    self.count = Animal.count

  def display(self):
    print("Animal count: {}".format(self.count))
    print("Name: {}".format(self.name))
    print("Age: {}".format(self.age))

# Create three Animal objects with arbitrary name and age values
animal1 = Animal("Lion", 5)
animal2 = Animal("Tiger", 4)
animal3 = Animal("Bear", 3)

# Display information about the objects using the display() method
animal1.display()
animal2.display()
animal3.display()
