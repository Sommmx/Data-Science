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
#print(simple_car.fuel_type())



# print(simple_car.genereal())
# print(my_car.brand)
# print(my_car.full_name())



# *args and **kwargs
def sample_function(*args, **kwargs):
    print(args)
    print(kwargs)


#sample_function(1,2,3,name = "Som",surname = "Pichewar")



#RECURSION
def recursion(n):
    if n==0 or n==1:
        return 1
    return n*recursion(n-1)

#print(recursion(5))


# ENCAPSULATION
class bank_acc:
    def __init__(self,account_number, owner, balance = 0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance   ## HIDDEN (ENCAPSULATION)
    def deposit(self,amount):
        if amount < 0:
            print("Please enter valid amount")
        else:
            self.__balance += amount
            print(f"Successfully added {amount} to your account")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount < 0:
            print("Please enter valid amount")
        else:
            self.__balance -= amount
            print(f"Successfully withdrawn {amount} from your account")
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f"Account number [{self.account_number}] - Owner: {self.owner}"





# account1 = bank_acc("12345", "somnath", 1000)

# print(account1)
# # print(account1.get_balance())
# account1.deposit(500)
# account1.withdraw(200)

# account1.withdraw(2000)





#DECORATOR
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@decorator
def Hello():
    print( "Hello")

# Hello()



#ABSTRACTION
#Example 1
from abc import ABC, abstractmethod


class notification(ABC):
    @abstractmethod
    def send(self,message, user):
        pass

class sms_notificatoin(notification):
     def send(self, message, user):
         print(f"Sending sms to {user}:{message}")

class email_notificatoin(notification):
     def send(self, message, user):
         print(f"Sending email to {user}:{message}")



notifications = sms_notificatoin()

notifications.send("Hi","Som")




# Example 2

from abc import ABC, abstractmethod
class document(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self):
        pass


class PDFDocument(document):
    def read(self):
        print("Reading the document")
    def save(self):
        print("Saving the document")



doc = PDFDocument()
doc.read()
doc.save()




k = 1
n=5
for i in range(n):
    for j in range(i+1):
        print(k, end=" ")
        k = k+1
    print("\n")