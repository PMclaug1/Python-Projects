#create a sum function with unlimited positional arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5))


def calculate(n, **kwargs):
    print(type(kwargs))
#    print(kwargs["add"])
#    print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")
        self.color = kw.get("color")

my_car = Car(make="Honda", model="Civic", color="Grey")
print(my_car.model)
print(my_car.make)
print(my_car.year)
print(my_car.color)




