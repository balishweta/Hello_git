# Q.1 Create a circle class and initialize it with radius. Make two methods getArea and getCircumference
# inside this class.


class Circle():
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return self.radius ** 2 * 3.14

    def getCircumference(self):
        return 2 * self.radius * 3.14


NewCircle = Circle(8)
print(NewCircle.getArea())
print(NewCircle.getCircumference())

# Q.2  Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.


class Student():
    def __init__(self, sname, srollno):
        self.name = sname
        self.rollno = srollno


    def display(self):
        return str(self.name), str(self.rollno)


student_1 = Student('Shweta', 11)
print(student_1.display())

# 3- Create a Temperature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature(object):
    def _init_(self, fahrenheit=32):
        self._fahrenheit = fahrenheit
        self._celsius = self.convert_to_celsius(fahrenheit)

    def convert_to_celsius(self, f):
        return (f-32)*(5/9)

    def convert_to_fahrenheit(self, c):
        return (c*(9/5)) + 32

    def set_fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = self.convert_to_celsius(value)

    def set_celsius(self, value):
        self._fahrenheit = self.convert_to_fahrenheit(value)
        self._celsius = value

    def get_fahrenheit(self):
        return int(self._fahrenheit)

    def get_celsius(self):
        return int(self._celsius)

    fahrenheit = property(get_fahrenheit, set_fahrenheit)
    celsius = property(get_celsius, set_celsius)


t = Temperature()
t.fahrenheit = 212
print(t.celsius)


#**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.

class Movie():
    def __init__(self, smoviename, sartistname, syear, sratings):
        self.moviename = smoviename
        self.artistname = sartistname
        self.year = syear
        self.ratings = sratings

    def display(self):
        return str(self.moviename), str(self.artistname), str(self.year), str(self.ratings)

    def update(self):
        self.moviename = "Tiger Zinda hai"
        self.artistname = "Salman Khan"
        self.year = 2017
        self.ratings = 3



movies1 = Movie('Dishoom', 'John Abrahim', 2016, 4)
print(movies1.display())
movies1.update()
print(movies1.display())

#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary


class Expenditure:
    def __init__(self, sexpenditure, ssavings):
        self.expenditure = sexpenditure
        self.savings = ssavings

    def display(self):
        return str(self.expenditure), str(self.savings)

    def calsal(self):
        return self.expenditure+self.savings

    def displaysal(self):
        print("Total salary is " + str(self.calsal()))


Expenditure1 = Expenditure(10000, 50000)
print("Expenditure and savings are ", Expenditure1.display())
Expenditure1.displaysal()