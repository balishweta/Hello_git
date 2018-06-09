# 1. Create a class Animal as a base class and define method animal_attribute.
# Create another class Tiger which is inheriting Animal and access the base class method


class Animal:

    def animal_attribute(self):
                print((str(self.name) + " " + str(self.noise) + " " + "and eats " + str(self.eat)))


class Tiger(Animal):
    def __init__(self, name, noise, eat):
        self.name = name
        self.noise = noise
        self.eat = eat


tony1 = Tiger("tony", "roar", "meat")
tony1.animal_attribute()

#2. What will bw the output


class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'


class B(A):
        def g(self):
            return 'B'


a = A()
b = B()
print(a.f(), b.f())

# ANSwer = A B

# 3. Create a class Cop.Initialize its name, age,work experience and designation.Define methods to add,display
# and update the following details.Create another class Mission which extends the class Cop.Define method add-mission_details
# select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission


class Cop:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def display_details(self):
        print(self.name, "cop is on duty with", self.exp, "years of experience")

    def update(self):
        self.name = 'Sherlock'
        self.exp = 7


class Mission(Cop):
    def __init(self):
        super(Mission, self).__init()

    def display_mission(self, mission):
        print("The active mission is", mission)

    def assign_cop(self, mission):
        print(self.name, "has been assigned", mission)


mission1 = Mission('sherlock', 4)
mission1.display_mission('Secret')
mission1.display_details()
mission1.assign_cop('Secret')

# 4. Create a class Shape.Initialize it with length and breadth.Create the method area.
# Create a class rectangle and square which inherits shape and access the method area.


class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super(Rectangle, self).__init__(length, breadth)


class Square(Shape):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


R1 = Rectangle(3, 4)
print("the area of the rectangle = ", R1.area())

S1 = Square(3)
print("the area of the square = ", S1.area())







