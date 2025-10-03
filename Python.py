#BASICS ARE COMPLETED
#OOPS CONCEPTS IN PYTHON

#CLASS
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand + "!"


    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):     #POLYMORPHISM 
        return "Petrol or Diesel"
    def genereal(self):
        return "Cars are means of transport"

#INHERITENCE
class Electric_car(Car):
    def __init__(self,brand,model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):    #POLYMORPHISM
        return "Battery recharge"




my_tesla = Electric_car("Tesla","Model S", "85KWH")
# print(my_tesla.fuel_type())


simple_car = Car("Tata", "Safari")
print(simple_car.fuel_type())



print(simple_car.genereal())
# print(my_car.brand)
# print(my_car.full_name())



# *args and **kwargs
def sample_function(*args, **kwargs):
    print(args)
    print(kwargs)


sample_function(1,2,3,name = "Som",surname = "Pichewar")



#RECURSION
def recursion(n):
    if n==0 or n==1:
        return 1
    return n*recursion(n-1)

print(recursion(5))



